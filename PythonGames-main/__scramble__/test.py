from unittest import TestCase

from controller import Controller, ControllerException
from repository import Repository
from domain import *


class TestController(TestCase):
    def setUp(self):
        self.controller = Controller("test.txt")

    def test_dead(self):
        self.assertEqual(self.controller.win_or_lose(), True)
        x = self.controller._get_scramble()
        x.dec_score(x.score)
        self.assertEqual(self.controller.win_or_lose(), "You Lose!")
        x.inc()
        x._set_scramble()
        self.assertEqual(self.controller.win_or_lose(), "You Win!")

    def test_swap(self):
        x = self.controller._get_scramble()
        l1 = x.scramble[1]
        l2 = x.scramble[2]
        self.controller.swap(0, 1, 0, 2)
        x = self.controller._get_scramble()
        self.assertEqual(x.scramble[1], l2)
        self.assertEqual(x.scramble[2], l1)

    def test_undo(self):
        with self.assertRaises(ControllerException):
            self.controller.undo()
        x = self.controller._get_scramble()
        l1 = x.scramble[1]
        l2 = x.scramble[2]
        self.controller.swap(0, 1, 0, 2)
        x = self.controller._get_scramble()
        self.assertEqual(x.scramble[1], l2)
        self.assertEqual(x.scramble[2], l1)
        self.controller.undo()
        x = self.controller._get_scramble()
        self.assertEqual(x.scramble[1], l1)
        self.assertEqual(x.scramble[2], l2)

    def test_list_scramble(self):
        x = self.controller._get_scramble()
        y = self.controller._get_scramble().scramble
        to_print = ""
        for letter in y:
            to_print += letter
        to_print += "   [ score is: {} ]".format(x.score)
        self.assertEqual(self.controller.list_scramble(), to_print)


class TestRepository(TestCase):
    def setUp(self):
        self.repo = Repository("test.txt")

    def test_get_scramble(self):
        self.assertEqual(self.repo.get_scramble().id, "Arthur")

    def test_IOError(self):
        with self.assertRaises(ScrambleException):
            repo = Repository("no.txt")