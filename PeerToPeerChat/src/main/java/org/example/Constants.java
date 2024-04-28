package org.example;

public enum Constants {
    CONNECT_MESSAGE("Enter the username and port number: "),
    MENU_0("0. Exit"),
    MENU_1("1. Connect to peers"),
    MENU_2("2. See peers"),
    OPTION_0("0"),
    OPTION_1("1"),
    OPTION_2("2"),
    PEERS("Peers: "),
    ERROR_MSG("Error: "),
    CONNECT_TO_PEERS("Enter the address and port number of the peer you want to connect to: "),
    SKIP("skip"),
    QUIT("q"),
    CHANGE("c"),
    CHATROOM_WELCOME("Welcome to the chatroom!"),
    USERNAME_KEY("username"),
    MESSAGE_KEY("message"),
    HAS_DISCONNECTED_MSG(" has disconnected."),
    DEFAULT_USERNAME("Anonymous"),
    ERROR_PENDING_CONNECTION("Error in adding pending connection: "),
    ERROR_ADDING_CONNECTION("Error in adding connection: "),
    START_CHAT_MESSAGE("You can now start chatting! Press q to quit, c to change."),
    YOU_DISCONNECTED("You have been disconnected from the persons in this chat! Press c to continue."),
    DISCONNECTED_FROM_EVERYONE("You have been disconnected from everyone!"),
    INVALID_OPTION("Invalid option!"),
    DISCONNECT("%disconnect%"),
    GOODBYE("Goodbye!"),
    CONNECT("%connect%");

    public final String value;
    Constants(String value) {
        this.value = value;
    }
}
