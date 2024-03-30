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


class KeyboardIter:  # class of iterator
    """
    Iterator class for iterating through keyboard with production time greater than 2000 seconds
    """

    def __init__(self, keyboards):
        self.keyboards = keyboards
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.keyboards):
            keyboard = self.keyboards[self.index]  # obtinem tastatura de la indexul curent din lista de tastaturi
            self.index = self.index + 1
            if keyboard[1] > 2000:  # daca timpul de prod al tastaturii actuale e mai mare e 2000s
                return keyboard
            else:
                return self.__next__()  # se trece la urmatoarea tastatura prin apelarea recursiva a metodei __next__
        else:
            raise StopIteration


class KeyboardProductionTimes:  # clasa obiectului iterabil
    """
    This is a docstring. Class for storing keyboard production times.
    """

    def __init__(self):
        self.keyboards = []

    def __iter__(self):
        return KeyboardIter(self.keyboards)

    def add_keyboard(self, serial: str, production_time: int) -> None:
        """
        This method adds a produced keyboard with serial number and produced time.
        :param serial: serial number of the keyboard
        :param production_time: production time of the keyboard
        :return: None
        """
        self.keyboards.append((serial, production_time))

    def average_production_time(
            self) -> float:  # calculam timpul mediu de prod al tuturor tastaturilor din lista self.keyboards
        """
        This method calculates the average production time of all keyboards.
        :return: average production time.
        """
        return sum(time for _, time in self.keyboards) / len(self.keyboards)


c = KeyboardProductionTimes()  # instanta cu obiectul iterabil
c.add_keyboard("KB023871", 3210)
c.add_keyboard("KB023873", 1890)
c.add_keyboard("KB023875", 1982)
print("Average production time: ", c.average_production_time())
print(c.__doc__)

with open('keyboards_greatest_than_2000sec.txt', 'w') as file:
    for serial in c:
        file.write(f"{serial}\n")
