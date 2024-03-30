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


class KeyboardIter:
    """
    Class for iterating keyboard objects
    """

    def __init__(self, keyboards: dict):
        """
        Class constructor. Takes dictionary containing created keyboards
        :param keyboards: Dictionary with previously created keyboards
        """
        self.keyboards = keyboards

    def __iter__(self):
        """
        Iter method required for making this class an iterator
        :return: self
        """
        return self

    def __next__(self):
        """
        Method required for iteration.
        :return: str : Serial number of keyboards that took more than 2000s to make
        """
        for serial, time in self.keyboards.copy().items():
            if time > 2000:
                del self.keyboards[serial]
                return serial
        else:
            raise StopIteration


class KeyboardProductionTimes:
    """
    Class for storing the information about created keyboards
    """
    keyboards = None

    def __init__(self):
        """
        Class constructor. Prepares dictionary containing serial and production time
        """
        self.keyboards = {}

    def __iter__(self):
        """
        Sending created keyboards for iteration
        :return: str : serial of keyboards that took longer than 2000s to produce
        """
        return KeyboardIter(self.keyboards)

    def add_keyboard(self, serial: str, prod_time: int):
        """
        Method for adding keyboards with their serial and production time
        :param serial: Keyboard's serial
        :param prod_time: Keyboard's production time in seconds
        :return: None
        """
        self.keyboards.update({serial: prod_time})

    def average_production_time(self):
        """
        Method that calculates the average production time of a keyboard
        :return: float : number representing average time for production per keyboard
        """
        i = 0
        result = 0
        for time in self.keyboards.values():
            result += time
            i += 1
        return result / i


instance = KeyboardProductionTimes()

instance.add_keyboard("KB023871", 3210)
instance.add_keyboard("KB023873", 1890)
instance.add_keyboard("KB023875", 1982)
# instance.add_keyboard("KB023877", 2100)

print(instance.average_production_time())

with open("examen.out", "w") as file:
    for i in instance:
        file.write(f"{str(i)}\n")
