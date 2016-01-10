"""The person module contains a Person model"""
from models.address import Address


class Person(object):
    """Represents a person"""
    def __init__(self):
        """Initializes a new person"""
        self._first_name = ""
        self._last_name = ""
        self._address = None

    def set_first_name(self, new_first_name):
        """Sets the first name of the person

        :param new_first_name: The new first name
        :type new_first_name: str
        :returns: self
        :rtype: Person"""

        self._first_name = new_first_name
        return self

    def get_first_name(self):
        """Returns the first name of the person

        :returns: self
        :rtype: Person"""

        return self._first_name

    def set_last_name(self, new_last_name):
        """Sets the last name of the person

        :param new_last_name: The new last name
        :type new_last_name: str
        :returns: self
        :rtype: Person"""

        self._last_name = new_last_name
        return self

    def get_last_name(self):
        """Returns the last name of the person

        :returns: self
        :rtype: Person"""

        return self._last_name

    def set_address(self, new_address):
        """Sets the address of the person

        :param new_address: The person's new address
        :type new_address: Address
        :returns: self
        :rtype: Person"""

        if isinstance(new_address, Address):
            self._address = new_address

        return self

    def get_address(self):
        """Returns the address of the person

        :returns: self
        :rtype: Address"""

        return self._address

    def __str__(self):
        return "%s %s\n%s" % (self.get_first_name(), self.get_last_name(), self.get_address())
