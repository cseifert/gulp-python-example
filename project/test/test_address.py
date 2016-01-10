"""Tests for the address module"""

import unittest

from models.address import Address, City


class TestAddress(unittest.TestCase):
    """Tests the address class"""
    def setUp(self):
        self._address = Address()

    def test_street(self):
        """Tests setter and getter of street of an address"""
        street = "Mystreet 1"
        self._address.set_street(street)
        self.assertEqual(self._address.get_street(), street)

    def test_zip(self):
        """Tests setter and getter of zip of an address"""
        zip_number = "12345"
        self._address.set_zip(zip_number)
        self.assertEqual(self._address.get_zip(), zip_number)

    def test_city(self):
        """Tests setter and getter of city of an address"""
        city = City()
        self._address.set_city(city)
        self.assertIsInstance(self._address.get_city(), City)

    def test_string_casting(self):
        """Tests casting of an Address object"""
        street = "Mystreet 1"
        zip_number = "12345"
        city = City().set_name("City")

        self._address.set_street(street)
        self._address.set_zip(zip_number)
        self._address.set_city(city)

        expected_output = "%s\n%s %s" % (
            self._address.get_street(),
            self._address.get_zip(),
            self._address.get_city()
        )

        self.assertEqual(str(self._address), expected_output)


class TestCity(unittest.TestCase):
    """Tests the city class"""
    def setUp(self):
        self._city = City()

    def test_name(self):
        """Tests setter and getter of name of a city"""
        name = "City"
        self._city.set_name(name)
        self.assertEqual(self._city.get_name(), name)

if __name__ == '__main__':
    unittest.main()
