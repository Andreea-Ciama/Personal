package org.example;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import static org.example.Constants.CONNECT_MESSAGE;
import static org.example.Constants.ERROR_MSG;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.println(CONNECT_MESSAGE.value);
        String[] input = reader.readLine().split(" ");

        ConnectionManager.getInstance().setUsername(input[0]);

        try {
            Server server = new Server(Integer.parseInt(input[1]));
            server.start();
            new Peer().chooseAction(reader, input[0], server);

        } catch (Exception e) {
            System.out.println(ERROR_MSG.value + e.getMessage());
        }
    }
}
