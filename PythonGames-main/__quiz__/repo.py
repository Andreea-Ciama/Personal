from domain import Question

'''
This module contains the repository, which stores all the data both from files and console.
'''


class Repository(object):

    def __init__(self):
        '''
        The constructor of the class.
        '''
        self.__list = self.readFile("master.txt")

    def print_repo(self):
        '''
        This function prints the elements on the display.
        '''
        for x in self.__list:
            print(x)

    def add_question(self, new_question):
        '''
        This function adds a new question to the list.
        Input : new_question, a question
        Output : the initial list + new_question
        '''
        self.__list.append(new_question)
        # self.print_repo()
        self.writeFile("master.txt")

    def writeFile(self, fileName):
        '''
        This function updates the file whenever we add a new question, by writing
        all the list into the file.
        Input : fileName, a string
        Output : error is it doesn't work
                 updated file if it worked
        '''
        f = open(fileName, "w")
        try:
            for el in self.__list:
                f.write(str(el) + '\n')
            f.close()
        except Exception as e:
            print("An error appeared -" + str(e))

    def readFile(self, fileName):
        '''
        This function reads a file and stores the questions into a list.
        '''
        result = []
        try:
            f = open(fileName, "r")
            line = f.readline().strip()
            while len(line) > 0:
                line = line.split(";")
                result.append(Question(int(line[0]), line[1], line[2], line[3], line[4], line[5], line[6]))
                line = f.readline().strip()
            f.close()
        except IOError as error:
            print("An error occured - " + str(error))
            raise error

        return result


def test_repository():
    '''
    This function tests the repository.
    '''
    repo = Repository()
    len1 = len(repo.list)
    test_question = Question(1, "Largest number", 1, 2, 3, 3, "Easy")
    repo.add_question(test_question)
    len2 = len(repo.list)
    assert len1 + 1 == len2
    assert repo.list[len(repo.list) - 1] == test_question