# https://github.com/toadereandreas/Babes-Bolyai-University/tree/master/1st%20semester/Fundamentals-of-programming/PracticalExam

class Question(object):
    '''
    This is the question entities with the given atributes: id, text, choiches,
    the correct choice and its difficulty.
    '''

    def __init__(self, id, text, choice_a, choice_b, choice_c, correct_choice, difficulty):
        '''
        This is the constructor of the class.
        '''
        self.__id = id
        self.__text = text
        self.__choice_a = choice_a
        self.__choice_b = choice_b
        self.__choice_c = choice_c
        self.__correct_choice = correct_choice
        self.__difficulty = difficulty

    def __str__(self):
        return str(
            self.__id) + ";" + self.__text + ";" + self.__choice_a + ";" + self.__choice_b + ";" + self.__choice_c + ";" + self.__correct_choice + ";" + self.__difficulty

    '''
    Setters and getters of the class.
    '''

    def get_id(self):
        return self.__id

    def get_text(self):
        return self.__text

    def get_choice_a(self):
        return self.__choice_a

    def get_choice_b(self):
        return self.__choice_b

    def get_choice_c(self):
        return self.__choice_c

    def get_correct_choice(self):
        return self.__correct_choice

    def get_difficulty(self):
        return self.__difficulty

    def set_id(self, value):
        self.__id = value

    def set_text(self, value):
        self.__text = value

    def set_choice_a(self, value):
        self.__choice_a = value

    def set_choice_b(self, value):
        self.__choice_b = value

    def set_choice_c(self, value):
        self.__choice_c = value

    def set_correct_choice(self, value):
        self.__correct_choice = value

    def set_difficulty(self, value):
        self.__difficulty = value

    id = property(get_id, set_id, None, None)
    text = property(get_text, set_text, None, None)
    choice_a = property(get_choice_a, set_choice_a, None, None)
    choice_b = property(get_choice_b, set_choice_b, None, None)
    choice_c = property(get_choice_c, set_choice_c, None, None)
    correct_choice = property(get_correct_choice, set_correct_choice, None, None)
    difficulty = property(get_difficulty, set_difficulty, None, None)


def test_question_class():
    test_question = Question(1, "Largest number", 1, 2, 3, 3, "Easy")
    assert test_question.get_choice_a() == 1
    assert test_question.get_choice_b() == 2
    assert test_question.get_choice_c() == 3
    assert test_question.get_correct_choice() == 3
    assert test_question.get_difficulty() == "Easy"
    assert test_question.get_id() == 1
    assert test_question.get_text() == "Largest number"
    test_question.set_choice_a(2)
    assert test_question.get_choice_a() == 2
    test_question.set_choice_b(7)
    assert test_question.get_choice_b() == 7
    test_question.set_choice_c(10)
    assert test_question.get_choice_c() == 10
    test_question.set_correct_choice(10)
    assert test_question.get_correct_choice() == 10
    test_question.set_difficulty("Medium")
    assert test_question.get_difficulty() == "Medium"
    test_question.set_id(9)
    assert test_question.get_id() == 9
    test_question.set_text("Vaszi")
    assert test_question.get_text() == "Vaszi"


test_question_class()