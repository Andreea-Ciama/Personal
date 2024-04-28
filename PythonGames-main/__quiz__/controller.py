from domain import Question

'''
This is the service module. Here are the objects created and then passed to the repository
to store or work with them.
'''


class Service(object):

    def __init__(self, repository, validator):
        '''
        This is the constructor of the service.
        It requires 2 input parameters, a repository and a validator
        It creates the service.
        '''
        self.__repository = repository
        self.__validator = validator

    def create_question(self, parameters):
        '''
        This function creates a question.
        Input : parameters, a list of strings
        Output : new_question, a question object
        '''
        new_question = Question(int(parameters[0]), parameters[1], parameters[2], parameters[3], parameters[4],
                                parameters[5], parameters[6])
        return new_question

    def add_question(self, parameters):
        '''
        This function checks whether the parameters given are suitable for creating a question.
        If they are it creates a question which is passed to the repository too add.
        Input : parameters, a list of strings
        '''
        self.__validator.validate_question(parameters)
        question = self.create_question(parameters)
        self.__repository.add_question(question)


from repo import Repository
from validation import Validator


def test_service():
    '''
    This function tests the service
    '''
    repository = Repository()
    validation = Validator()
    test_service = Service(repository, validation)
    len1 = len(test_service.repository.list)
    test_question = Question(1, "Largest number", 1, 2, 3, 3, "Easy")
    test_service.repository.add_question(test_question)
    assert len(test_service.repository.list) == len1 + 1