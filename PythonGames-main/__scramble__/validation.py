from domain import ScrambleException


class ValidatorException(ScrambleException):
    pass


class Validator:
    def validate_swap(self, word_1, letter_1, word_2, letter_2, sentence):
        sentence = sentence.split()
        errors = ""
        if word_1 < 0 or word_2 < 0 or word_1 >= len(sentence) or word_2 >= len(sentence):
            errors += "Error!!! Word inexistent!!!\n"
        if letter_1 == letter_2 and word_1 == word_2:
            errors += "Error!!! Please insert a valid move!!!\n"
        if letter_1 <= 0 or letter_2 <= 0:
            errors += "Error!!! Letters inexistent!!!\n"
        else:
            for i in range(0, len(sentence)):
                if i == word_1:
                    if letter_1 >= len(list(sentence[i])):
                        errors += "Error!!! Letter out of word!!!\n"
                if i == word_2:
                    if letter_2 >= len(list(sentence[i])):
                        errors += "Error!!! Letter out of word!!!\n"
        if errors != "":
            raise ValidatorException(errors)