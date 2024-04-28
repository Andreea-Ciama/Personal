package org.example;

import java.io.BufferedReader;
import java.net.Socket;

import static org.example.Constants.CHANGE;
import static org.example.Constants.CONNECT_TO_PEERS;
import static org.example.Constants.ERROR_MSG;
import static org.example.Constants.GOODBYE;
import static org.example.Constants.INVALID_OPTION;
import static org.example.Constants.MENU_0;
import static org.example.Constants.MENU_1;
import static org.example.Constants.MENU_2;
import static org.example.Constants.PEERS;
import static org.example.Constants.QUIT;
import static org.example.Constants.SKIP;
import static org.example.Constants.START_CHAT_MESSAGE;

public class Peer {

    public Peer(){}

    public void chooseAction(BufferedReader bufferedReader, String username, Server server) {

        while (true) {
            System.out.println(MENU_0.value);
            System.out.println(MENU_1.value);
            System.out.println(MENU_2.value);

            try {
                String option = bufferedReader.readLine();

                switch (option) {
                    case "0":
                        ConnectionManager.getInstance().disconnectFromAll();
                        System.out.println(GOODBYE.value);
                        System.exit(0);
                    case "1":
                        updateListenToPeers(bufferedReader, username, server);
                        break;
                    case "2":
                        System.out.println(PEERS.value);
                        for (Socket socket : ConnectionManager.getInstance().getConnections()) {
                            System.out.println(socket.getInetAddress() + ":" + socket.getPort());
                        }
                        break;
                    default:
                        System.out.println(INVALID_OPTION.value);
                }
            } catch (Exception e) {
                System.out.println(ERROR_MSG.value + e.getMessage());
            }
        }
    }

    public void updateListenToPeers(BufferedReader bufferedReader, String username, Server server)
            throws Exception {

        System.out.println(CONNECT_TO_PEERS.value);
        String input = bufferedReader.readLine();
        String[] inputValues = input.split(" ");

        if (!input.equals(SKIP.value)) {
            for (String peer : inputValues) {
                String[] peerInfo = peer.split(":");

                Socket socket = null;
                try {
                    if (!ConnectionManager.getInstance().awakeConnection(peerInfo[0], Integer.parseInt(peerInfo[1]))) {
                        socket = new Socket(peerInfo[0], Integer.parseInt(peerInfo[1]));
                        ConnectionManager.getInstance().addConnection(socket);
                    }

                } catch (Exception e) {
                    if (socket != null) {
                        socket.close();
                    } else {
                        System.out.println(ERROR_MSG.value + e.getMessage());
                    }

                    System.out.println("Could not connect to " + peerInfo[0] + ":" + peerInfo[1]);
                }
            }

            communicate(bufferedReader, username, server);
        }
    }

    public void communicate(BufferedReader bufferedReader, String username, Server server) {
        try {
            System.out.println(START_CHAT_MESSAGE.value);

            while (true) {
                String message = bufferedReader.readLine();

                if (message.equals(QUIT.value)) {
                    ConnectionManager.getInstance().disconnectFromAll();
                    break;
                } else if (message.equals(CHANGE.value)) {
                    ConnectionManager.getInstance().pauseAllConnections();
                    chooseAction(bufferedReader, username, server);
                } else {
                    ConnectionManager.getInstance().writeMessage(message);
                }
            }

            System.exit(0);

        } catch (Exception e) {
            System.out.println(ERROR_MSG.value + e.getMessage());
        }
    }
}