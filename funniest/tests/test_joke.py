from unittest import TestCase

import funniest
from funniest.command_line import main


class TestJoke(TestCase):
    def test_is_string(self):
        s = funniest.joke()
        self.assertTrue(isinstance(s, basestring))


class TestConsole(TestCase):
    def test_basic(self):
        main()
