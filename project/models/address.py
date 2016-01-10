"""The address module contains models for an address and a city"""


class Address(object):
    """Represents an address"""
    def __init__(self):
        """Initializes a new address

        :returns: self
        :rtype: Address"""

        self._street = ""
        self._zip = ""
        self._city = None

    def set_street(self, new_street):
        """Sets the street of the address

        :param new_street: Street of the address
        :type new_street: string
        :returns: self
        :rtype: Address
        """

        self._street = new_street
        return self

    def get_street(self):
        """Returns the street of the address

        :returns: the street name
        :rtype: str
        """

        return self._street

    def set_zip(self, new_zip):
        """Sets the street of the address

        :param new_zip: Street of the address
        :type new_zip: string
        :returns: self
        :rtype: Address
        """

        self._zip = new_zip
        return self

    def get_zip(self):
        """Returns the zip of the address

        :returns: the zip
        :rtype: str
        """

        return self._zip

    def set_city(self, new_city):
        """Sets the city of the address

        :param new_city: Street of the address
        :type new_city: string
        :returns: self
        :rtype: Address
        """

        if isinstance(new_city, City):
            self._city = new_city

        return self

    def get_city(self):
        """Returns the city of the address

        :returns: the city
        :rtype: City
        """

        return self._city

    def __str__(self):
        """Returns the full address as a string

        :returns: the full string
        :rtype: str
        """

        return "%s\n%s %s" % (self.get_street(), self.get_zip(), self.get_city())


class City(object):
    """Represents a city with its name"""
    def __init__(self):
        """Initializes a new city

        :returns: self
        :rtype: City"""

        self._name = ""

    def set_name(self, new_name):
        """Sets the name of the city

        :param new_name: Name of the city
        :type new_name: string
        :returns: self
        :rtype: City
        """

        self._name = new_name
        return self

    def get_name(self):
        """Returns the name of the city

        :returns: self
        :rtype: City
        """

        return self._name

    def __str__(self):
        """Returns the name of the city as string

        :returns: the full string
        :rtype: str
        """

        return self.get_name()
