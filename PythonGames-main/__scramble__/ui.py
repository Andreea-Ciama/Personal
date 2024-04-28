from controller import Controller
from domain import ScrambleException


class UI:
    def __init__(self):
        self.__controller = Controller("input.txt")

    def run(self):
        while self.__controller.win_or_lose() == True:
            try:
                print(self.__controller.list_scramble())
                command = input("Your command: ").split()
                if not command:
                    print("Where is the command?\n")
                elif command[0] == "undo":
                    self.__controller.undo()
                elif command[0] == "swap":
                    if len(command) != 6:
                        print(" You have to insert a valid command! swap word1 letter1 - word2 letter2\n")
                    else:
                        self.__controller.swap(int(command[1]), int(command[2]), int(command[4]), int(command[5]))
                elif command[0] == "exit":
                    return
                else:
                    print("--Invalid command--\n")
            except ValueError:
                print("Error!\n")
            except ScrambleException as ex:
                print(ex)
        print(self.__controller.win_or_lose())
