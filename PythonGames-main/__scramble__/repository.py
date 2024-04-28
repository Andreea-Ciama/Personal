from random import randint

from domain import *


class Repository:
    def __init__(self, filename):
        """
        Initialize the repository
        :param filename:the filename where we store the sentences
        """
        self.__elems = []
        self.__filename = filename
        try:
            file = open(self.__filename, "r")  # open the file in read mode
            for l in file:  # take line by line
                self.__elems.append(Sentence(l.strip("\n")))  # edit the sentence and append as a Sentence object
            file.close()
        except IOError:  # if we have a file opening error we pass it to the upper layers
            raise ScrambleException("We can't open the dile!\n")

    def get_scramble(self):
        """
        Returns a randomly picked sentence from the list of sentences
        """
        return self.__elems[randint(0, len(self.__elems) - 1)]


