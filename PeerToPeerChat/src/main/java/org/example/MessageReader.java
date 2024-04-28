package org.example;

import javax.json.Json;
import javax.json.JsonObject;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

import static org.example.Constants.CHATROOM_WELCOME;
import static org.example.Constants.DISCONNECT;
import static org.example.Constants.HAS_DISCONNECTED_MSG;
import static org.example.Constants.MESSAGE_KEY;
import static org.example.Constants.USERNAME_KEY;

public class MessageReader implements Runnable {

    private final Socket socket;
    private final BufferedReader bufferedReader;
    private PrintWriter printWriter = null;

    public MessageReader(Socket socket) throws IOException {
        this.socket = socket;
        this.bufferedReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
    }

    public PrintWriter getPrintWriter() {
        return printWriter;
    }

    public boolean isAlive() {
        return printWriter != null;
    }

    @Override
    public void run() {
        boolean flag = true;

        try {
            this.printWriter = new PrintWriter(socket.getOutputStream(), true);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        while (flag) {
            try {
                JsonObject jsonObject = Json.createReader(bufferedReader).readObject();

                if (Thread.interrupted())
                    break;

                if (jsonObject.containsKey(USERNAME_KEY.value)) {
                    String message = jsonObject.getString(MESSAGE_KEY.value);
                    if (message.equals(DISCONNECT.value)) {
                        flag = false;
                        System.out.println(jsonObject.getString(USERNAME_KEY.value) + HAS_DISCONNECTED_MSG.value);
                        ConnectionManager.getInstance().removeConnection(socket);
                    } else {
                        System.out.println(jsonObject.getString(USERNAME_KEY.value) + ": " + message);
                    }
                }
            } catch (Exception e) {
                flag = false;
                ConnectionManager.getInstance().removeConnection(socket);
                return;
            }
        }

        ConnectionManager.getInstance().removeConnection(socket);
    }

    public Socket getSocket() {
        return socket;
    }
}
