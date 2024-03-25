"""
A production facility needs an iterable object to keep track off car warranty.
Each car have an int serial and datetime object for when the car was produced
Iterating the object will return all cars that are still covered by 3 years warranty (serial, <timedelta>)
1) 40p: Definition
    a) 10p: Basic class structure of objects
    b) 10p: Basic class structure of iterator
    c) 10p: Method to add sold care
    d) 10p: Method to print cars not covered by warranty
2) 40p: Execution:
    a) 10p: Create instance of your shop
    b) 10p: Call method to add (sell) car (serial, <datetime>))
        - 1588, 20 Jan 2019 10:30:32
        - 1692, 20 Jan 2021 9:20:25
        - 1994, 20 Jan 2022 9:10:30
    c) 10p: Call method to return expired warranty (serial, <datetime>))
    d) 10p: Iterate the created object and write each care covered by warranty in a file
3) 20p: Documenting:
   a) 5p: type hints for arguments
   b) 5p: module documentation
   c) 5p: class documentation for all classes
   d) 5p: method documentation for all methods
"""
from datetime import datetime


class CarIter:

    def __iter__(self):
        return self

    def __next__(self):
        pass


class CarShop:
    """
    This is a docstring
    """
    warranty = None

    def __init__(self):
        self.warranty = {}

    def __iter__(self):
        return CarIter()

    def sell_car(self, serial: int, date: datetime) -> None:
        """
        This method will sel  one car  and record date and serial number
        :param date: Date the care was sold, type: datetime
        :param serial: serial number of sold car
        :return: None
        """
        self.warranty.update({serial: date})

    def get_expired_warranty(self):
        pass


c = CarShop()
c.sell_car(1588, datetime(2019, month=1, day=20, hour=10, minute=30, second=32))
c.sell_car(1692, datetime(2021, month=1, day=20, hour=9, minute=20, second=25))
c.sell_car(1994, datetime(2022, month=1, day=20, hour=9, minute=20, second=30))
c.get_expired_warranty()
print(c.warranty)
print(c.__doc__)
