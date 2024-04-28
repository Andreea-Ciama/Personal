class ScrambleException(Exception):
    pass

from random import randint


class Sentence(object):
    def __init__(self, sentence):
        self.__id = sentence
        self.__sentence = list(sentence)
        self.__scramble = self.__convert_to_scramble(list(sentence))
        self.__score = self.__get_score()

    def __get_score(self):
        x = 0
        for letter in self.__sentence:
            if letter != " ":
                x += 1
        return x

    @property
    def id(self):
        return self.__id

    @property
    def sentance(self):
        return self.__sentence[:]

    @property
    def scramble(self):
        return self.__scramble[:]

    def _set_scramble(self):
        self.__scramble = self.__sentence

    @property
    def score(self):
        return self.__score

    def dec_score(self, value):
        self.__score = self.__score - value

    def inc(self):
        self.__score += 1

    def __convert_to_scramble(self, sentance):
        n = randint(10, 15)
        while n:
            x = randint(1, len(sentance) - 2)
            y = randint(1, len(sentance) - 2)
            if self.__check(x, sentance) and self.__check(y, sentance):
                sentance[x], sentance[y] = sentance[y], sentance[x]
                n -= 1
        return sentance

    def __check(self, x, sentance):
        if sentance[x - 1] == " " or sentance[x + 1] == " " or sentance[x] == " ":
            return False
        return True

    def __find(self, word, letter):
        cword = 0
        index = 0
        if word == cword:
            return letter
        else:
            for i in range(0, len(self.__scramble)):
                if self.__scramble[i] == " ":
                    cword += 1
                    index = i + 1
                if cword == word:
                    return index + letter

    def swap(self, word_1, letter_1, word_2, letter_2):
        x = self.__find(word_1, letter_1)
        y = self.__find(word_2, letter_2)
        self.__scramble[x], self.__scramble[y] = self.__scramble[y], self.__scramble[x]

    def __str__(self):
        to_print = ""
        for letter in self.__scramble:
            to_print += letter
        to_print += "   [ score is: {} ]".format(self.__score)
        return to_print