from domain import ScrambleException
from repository import Repository
from validation import Validator


class ControllerException(ScrambleException):
    pass


class Controller:
    def __init__(self, filename):
        self.__undo = None
        self.__valid = Validator()
        self.__repository = Repository(filename)
        self.__scramble = self.__repository.get_scramble()

    def list_scramble(self):
        """
        We return the string format for printing
        """
        return str(self.__scramble)

    def _get_scramble(self):
        """
        We use this function for testing
        """
        return self.__scramble

    def swap(self, word_1, letter_1, word_2, letter_2):
        """
        Swapping the letters
        """
        self.__valid.validate_swap(word_1, letter_1, word_2, letter_2,
                                   self.__scramble.id)  # check if the input is correct
        self.__scramble.swap(word_1, letter_1, word_2,
                             letter_2)  # swap the elements using the swap function from the Sentence class
        self.__scramble.dec_score(1)  # decrease the score by one
        self.__undo = [word_1, letter_1, word_2, letter_2]  # add the move to undo

    def undo(self):
        """
        Undo the last operation
        """
        if self.__undo is None:  # if we can not undo anymore we raise an error
            raise ControllerException("Error! You can't undo!\n")
        else:  # otherwise we simply do the swap from the undo list once more
            self.__scramble.swap(self.__undo[0], self.__undo[1], self.__undo[2], self.__undo[3])
            self.__undo = None  # undo becomes None because we don't want the user to do multiple undo operations


    def win_or_lose(self):
        """
        We verify if the game si won or lost or we continue to play the game
        :return:
        """
        if self.__scramble.score == 0:  # if the score is 0 it's a lose
            return "Sorry, you lost! Your score is-> 0"
        elif self.__scramble.sentance == self.__scramble.scramble:  # if the scramble sentence is solved it's a win
            return "You Won!" + "Your score is-> "+str(self.__scramble.score)
        else:
            return True