package org.example;

import org.example.exceptions.AddConnectionException;
import org.example.exceptions.AddPendingConnectionException;

import javax.json.Json;
import java.io.IOException;
import java.io.StringWriter;
import java.net.Socket;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

import static org.example.Constants.DEFAULT_USERNAME;
import static org.example.Constants.DISCONNECT;
import static org.example.Constants.DISCONNECTED_FROM_EVERYONE;
import static org.example.Constants.ERROR_ADDING_CONNECTION;
import static org.example.Constants.ERROR_PENDING_CONNECTION;
import static org.example.Constants.MESSAGE_KEY;
import static org.example.Constants.USERNAME_KEY;
import static org.example.Constants.YOU_DISCONNECTED;

public class ConnectionManager {

    private static ConnectionManager instance = null;
    private final ExecutorService executorService;
    private final Map<Socket, MessageReader> connections;
    private final Map<MessageReader, Future<?>> activeConnections;
    private String username;


    public static ConnectionManager getInstance() {
        if (instance == null)
            instance = new ConnectionManager();
        return instance;
    }

    private ConnectionManager() {
        executorService = Executors.newFixedThreadPool(10);
        connections = new HashMap<>();
        username = DEFAULT_USERNAME.value;
        activeConnections = new HashMap<>();
    }

    public void addPendingConnection(Socket socket) throws AddPendingConnectionException {
        try {
            MessageReader messageReader = new MessageReader(socket);
            connections.put(socket, messageReader);

        } catch (IOException e) {
            throw new AddPendingConnectionException(ERROR_PENDING_CONNECTION.value + e.getMessage());
        }
    }

    public void addConnection(Socket socket) throws AddConnectionException {
        try {
            MessageReader messageReader = new MessageReader(socket);
            connections.put(socket, messageReader);

            Future<?> future = executorService.submit(messageReader);
            activeConnections.put(messageReader, future);

        } catch (IOException e) {
            throw new AddConnectionException(ERROR_ADDING_CONNECTION.value + e.getMessage());
        }
    }

    public boolean awakeConnection(String address, int port) {
        for (Socket socket : connections.keySet()) {
            if (socket.getPort() == port) {
                Future<?> future = executorService.submit(connections.get(socket));
                activeConnections.put(connections.get(socket), future);

                return true;
            }
        }
        return false;
    }

    public void writeMessage(String message) {
        StringWriter stringWriter = new StringWriter();
        Json.createWriter(stringWriter).writeObject(Json.createObjectBuilder()
                .add(USERNAME_KEY.value, username)
                .add(MESSAGE_KEY.value, message)
                .build());

        for (MessageReader messageReader : activeConnections.keySet()) {
            if (messageReader.isAlive()) {
                messageReader.getPrintWriter().println(stringWriter);
            }
        }

        if (message.equals(DISCONNECT.value)) {
            for (MessageReader messageReader : activeConnections.keySet()) {
                removeConnection(messageReader.getSocket());
            }

            activeConnections.clear();

            System.out.println(YOU_DISCONNECTED.value);
        }
    }
    public void pauseConnection(Socket socket) throws IOException {
        MessageReader messageReader = connections.get(socket);
        if (messageReader.isAlive()) {

            connections.remove(socket);
            connections.put(socket, new MessageReader(socket));
        }
    }

    public void pauseAllConnections() throws IOException {
        for (Socket socket : connections.keySet()) {
            pauseConnection(socket);
        }
    }

    public void removeConnection(Socket socket) {
        MessageReader messageReader = connections.get(socket);

        if (messageReader != null) {
            Future<?> future = activeConnections.get(messageReader);
            if (future != null) {
                future.cancel(true);
            }
        }

        connections.remove(socket);
    }

    public void disconnectFromAll() {
        for (Socket socket : connections.keySet()) {
            awakeConnection(socket.getInetAddress().getHostAddress(), socket.getPort());
        }

        writeMessage(DISCONNECT.value);
        connections.clear();
        activeConnections.clear();

        System.out.println(DISCONNECTED_FROM_EVERYONE.value);
    }

    public List<Socket> getConnections() {
        return new ArrayList<>(connections.keySet());
    }

    public void setUsername(String username) {
        this.username = username;
    }
}
