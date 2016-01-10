"""This is an example script to show the use of the classes"""
from models.address import Address, City
from models.person import Person

def main():
    """Main function to be called when executing the script"""

    franks_city = City().set_name('City')
    franks_address = Address()\
        .set_street('Sample street')\
        .set_zip('01234')\
        .set_city(franks_city)

    frank = Person().set_first_name('Frank')\
        .set_last_name('Lastname')\
        .set_address(franks_address)

    print str(frank)

if __name__ == "__main__":
    main()
