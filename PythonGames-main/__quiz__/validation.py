'''
This module validates various data in the program.
'''
from errors import ValidError


class Validator(object):

    def validate_question(self, parameters):
        '''
        This function determines whether the parameters are suitable for creating a question.
        Input : parameters, a list of parameters that are checked
        Output : error if the parameters are not right
        '''
        errors = ""

        try:
            id = int(parameters[0])
            text = parameters[1]
            chuice_a = parameters[2]
            choice_b = parameters[3]
            choice_c = parameters[4]
            correct_choice = parameters[5]
            difficulty = parameters[6]
        except ValueError as ve:
            errors += "Invalid id input number !\n"

        difficulty = ["easy", "hard", "medium"]

        if parameters[6] not in difficulty:
            errors += "Invalid difficulty value !"

        if errors != "":
            raise ValidError(errors)

    def validate_quizz(self, parameters):
        '''
        This function determines whether the parameters are suitable for creating a quiz.
        Input : parameters, a list of parameters that are checked
        Output : error if the parameters are not right
        '''
        errors = ""

        difficulty = ["easy", "hard", "medium"]

        if parameters[0] not in difficulty:
            errors += "Invalid difficulty value !\n"

        try:
            id = int(parameters[1])
        except ValueError as ve:
            errors += "Invalid number of questions input !"

    def test_validate_question(self):
        '''
        This function tests the validate_question function.
        '''
        test_question = ["asdasd", 1, 2, 3, 4, 5, "hard"]
        assert self.validate_question(test_question) == 0
        test_question = [2, 1, 2, 3, 4, 5, 6]
        assert self.validate_question(test_question) == 0