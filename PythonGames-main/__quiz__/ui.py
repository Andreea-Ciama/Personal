'''
This is the User Interface module, the only part of the program which interracts with
the user.
'''
from sys import exit
from errors import ValidError
from domain import Question
from random import randint


class Console(object):

    def __ui_exit(self, parameters):
        '''
        This function exits the program.
        '''
        print("The program will be terminated now. Bye !")
        exit(0)

    def __ui_add(self, parameters):
        '''
        This function checks whether the number of the parameters of the add command is 7.
        Then it passes to the service the parameters if their number is correct.
        '''
        if len(parameters) != 7:
            print("Invalid number of parameters !")
            return
        self.__service.add_question(parameters)

    def __ui_create(self, parameters):
        '''
        This function check whether the number of the parameters off create command is 3.
        Then it passes to the service the parameters if their number is correct.
        '''
        if len(parameters) != 3:
            print("Invalid number of parameters !")
            return

        difficulty = ["easy", "hard", "medium"]
        if parameters[0] not in difficulty:
            print('Invalid difficulty input !')
            return

        try:
            number = int(parameters[1])
        except ValueError as ve:
            print(str(ve))
            return

        result = []
        try:
            f = open("master.txt", "r")
            line = f.readline().strip()
            while len(line) > 0:
                line = line.split(";")
                result.append(Question(int(line[0]), line[1], line[2], line[3], line[4], line[5], line[6]))
                line = f.readline().strip()
            f.close()

            contor = 0
            for x in result:
                if x.get_difficulty() == parameters[0]:
                    contor += 1

            if contor < number // 2:
                print("Insufficient questions of that difficulty !")
                return

            # easy_list = []
            # for x in result:
            #     if x.difficulty == "easy":
            #         easy_list.append(x)
            #
            # medium_list = []
            # for x in result:
            #     if x.difficulty == "medium":
            #         medium_list.append(x)
            # hard_list = []
            # for x in result:
            #     if x.difficulty == "hard":
            #         hard_list.append(x)
            hard_list = []
            for x in result:
                if x.difficulty == parameters[0]:
                    hard_list.append(x)

            new_list = []
            for x in range(0, len(hard_list)):
                new_list.append(hard_list[randint(0, len(hard_list)-1)])
            for x in range(0, number // 2):
                new_list.append(result[randint(0, len(result) - 1)])

            f = open(parameters[2], "w")
            try:
                for el in new_list:
                    f.write(str(el) + '\n')
                f.close()
            except Exception as e:
                print("An error appeared -" + str(e))
            # print(new_list)

        except FileNotFoundError as error:
            print("An error occured : " + str(error))



    def __ui_start(self, parameters):
        '''
        This function check whether the number of the parameters off create command is 2.
        '''
        if len(parameters) != 1:
            print("Invalind number of parameters ! Give only quizz name !")
            return

        result = []
        try:
            f = open(parameters[0], "r")
            line = f.readline().strip()
            while len(line) > 0:
                line = line.split(";")
                result.append(Question(int(line[0]), line[1], line[2], line[3], line[4], line[5], line[6]))
                line = f.readline().strip()
            f.close()

            '''
            Here we sort the list in such a way that the easier questions appear first.
            '''
            easy_list = []
            for x in result:
                if x.difficulty == "easy":
                    easy_list.append(x)
            medium_list = []
            for x in result:
                if x.difficulty == "medium":
                    medium_list.append(x)
            hard_list = []
            for x in result:
                if x.difficulty == "hard":
                    hard_list.append(x)

            result = []
            result += easy_list
            result += medium_list
            result += hard_list

            '''
            Now the quizz properly starts.
            '''

            points = 0
            for x in result:
                print(x.text + "?" + "\n" + x.choice_a + " " + x.choice_b + " " + x.choice_c)
                user_choice = input("Enter choice >> ")
                if user_choice == x.correct_choice:
                    if x.difficulty == "easy":
                        points += 1
                    if x.difficulty == "hard":
                        points += 3
                    if x.difficulty == "medium":
                        points += 2
                else:
                    print("Wrong")
            print("Quizz finished. Your score is : " + str(points))
        except FileNotFoundError as error:
            print("An error occured : " + str(error))

    def __init__(self, service):
        self.__service = service
        self.__commands = {"exit": self.__ui_exit,
                           "add": self.__ui_add,
                           "create": self.__ui_create,
                           "start": self.__ui_start
                           }

    def run(self):
        '''
        The main function of the console. It will be run untill the user will introduce
        the command "exit".
        '''
        while True:

            raw_command = input('Enter command >> ')
            raw_command = raw_command.strip()
            if "add" not in raw_command:
                command = raw_command.split(' ')
            else:
                command = raw_command.split(';')
                string = command[0]
                string = string.split(' ')
                command[0] = string[1]
                list = []
                string = "add"
                list.append(string)
                list += command
                command = list

            try:
                if command[0] in self.__commands:
                    self.__commands[command[0]](command[1:])
            except ValueError as ve:
                pass
            except ValidError as ve:
                print(ve)