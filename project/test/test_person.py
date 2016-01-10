"""Tests for the person module"""

import unittest

from models.person import Person


class TestPerson(unittest.TestCase):
    """Tests the person class"""
    def setUp(self):
        self._person = Person()

    def test_first_name(self):
        """Tests setter and getter of first name of a person"""
        first_name = "Firstname"
        self._person.set_first_name(first_name)
        self.assertEqual(self._person.get_first_name(), first_name)

    def test_last_name(self):
        """Tests setter and getter of last name of a person"""
        last_name = "Lastname"
        self._person.set_last_name(last_name)
        self.assertEqual(self._person.get_last_name(), last_name)


if __name__ == '__main__':
    unittest.main()
