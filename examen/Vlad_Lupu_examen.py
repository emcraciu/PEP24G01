"""
A production facility needs an iterable object to keep track product assembly times.
A class called "KeyboardProductionTimes" that will store the information needs to be created.
Each keyboard will have a string serial number "KBXXXXXX" and timedelta (or int) for production time
Iterating objects created with KeyboardProductionTimes will return all keyboards that had production
time greater than 2000s
1) 40p: Definition
    a) 10p: Basic class structure of KeyboardProductionTimes
    b) 10p: Basic class structure of iterator
    c) 10p: Method to add produced keyboards with serial and time
    d) 10p: Method that returns average keyboard production time
2) 40p: Execution:
    a) 10p: Create instance of KeyboardProductionTimes
    b) 10p: Call method to add keyboard <add_keyboard(serial, <timedelta | int>)>
        - KB023871, 3210s
        - KB023873, 1890s
        - KB023875, 1982s
    c) 10p: Call method to return average production time <average_production_time()>
    d) 10p: Iterate the created object and write each keyboard serial with production
            time greater then 2000s in a file on a new line
3) 20p: Documenting:
   a) 5p: type hints for arguments
   b) 5p: module documentation
   c) 5p: class documentation for all classes
   d) 5p: method documentation for all methods
"""


class KeyboardProductionTimes:
    """
    A class which will store the information about the new created keyboards
    """
    produced_keyboards = None

    def __init__(self):
        """Constructor method"""
        self.produced_keyboards = {}

    def __iter__(self):
        """Returns the iterator class KeyboardIter"""
        return KeyboardIter(self.produced_keyboards)

    def add_produced_keyboards(self, serial: str, production_time: int) -> None:
        """
        This method will add each keyboard and keep track of the serial number and production time.
        :param serial: Serial number for each keyboard
        :param production_time: Production time
        :return: None
        """
        self.produced_keyboards.update({serial: production_time})

    def calculate_average_prod_time(self) -> float:
        """Returns the average keyboard production time"""
        total = 0
        for kb, prod_time in self.produced_keyboards.items():
            total += prod_time
        return total / len(self.produced_keyboards)


class KeyboardIter:
    """
    Iterator class for keyboards
    """
    def __init__(self, produced_keyboards: dict):
        """Constructor method for the iterator class"""
        self.produced_keyboards = produced_keyboards

    def __iter__(self):
        return self

    def __next__(self):
        """
        :return: Keyboards with production time greater than 2000s
        """
        for serial, prod_time in self.produced_keyboards.copy().items():
            if prod_time > 2000:
                del self.produced_keyboards[serial]
                return serial
            else:
                del self.produced_keyboards[serial]
        else:
            raise StopIteration


k = KeyboardProductionTimes()
k.add_produced_keyboards("KB023871", 3210)
k.add_produced_keyboards("KB023873", 1890)
k.add_produced_keyboards("KB023875", 1982)
print(k.calculate_average_prod_time())
print(k.produced_keyboards)

with open("keyboards.txt", "w") as f:
    for keyboard in k:
        f.write(str(keyboard))
