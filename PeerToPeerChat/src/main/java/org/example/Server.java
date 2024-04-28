package org.example;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class Server extends Thread {

    private ServerSocket serverSocket;

    public Server(int port) throws IOException {
        this.serverSocket = new ServerSocket(port);
    }

    public void run() {
        try {
            while (true) {
                Socket socket = serverSocket.accept();
                ConnectionManager.getInstance().addPendingConnection(socket);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
