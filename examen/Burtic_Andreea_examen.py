"""
This module is created because a production facility needs an iterable object to keep track product assembly times.
A class called "KeyboardProductionTimes" that will store the information needs to be created.
Each keyboard will have a string serial number "KBXXXXXX" and timedelta (or int) for production time
Iterating objects created with KeyboardProductionTimes will return all keyboards that had production
time greater than 2000s.
"""


class KeyboardIter:
    """
        This is the class of iterator.
        This class has methods like the constructor, __init__,
        and the generator __iter__ and __next__ because it helps to iterate the objects.
    """

    def __init__(self, keyboards: dict):
        self.keyboards = keyboards

    def __iter__(self):
        return self

    def __next__(self):
        for serial, time in self.keyboards.copy().items():
            if time < 2000:
                del self.keyboards[serial]
                continue
            else:
                value = self.keyboards.pop(serial)
                return serial, value
        else:
            raise StopIteration


class KeyboardProductionTimes:
    """
        This is the object class.
        The main methods are add_keyboards and average_production_time.
        add_keyboards is a method to add produced keyboards with serial and time.
        average_production_time is a method that returns average keyboard production time.
    """
    keyboards = None

    def __init__(self):
        self.keyboards = {}

    def __iter__(self):
        return KeyboardIter(self.keyboards)

    def add_keyboards(self, serial: str, time: int) -> None:
        """
        This method is used to add produced keyboards with serial and time.
        :param serial: serial number of the keyboard, type:str
        :param time: production time of the keybord, type:int
        :return: None
        """
        self.keyboards.update({serial: time})

    def average_production_time(self) -> float:
        """
        This method is used to calculate the average of the production time for all keyboards.
        :return: type:float
        """
        times = []
        for s, t in self.keyboards.items():
            times.append(t)
        average = sum(times) / len(times)
        return average


k = KeyboardProductionTimes()
k.add_keyboards('KB023871', 3210)
k.add_keyboards('KB023873', 1890)
k.add_keyboards('KB023875', 1982)
k.add_keyboards('KB023878', 3240)
print(k.keyboards)
av = k.average_production_time()
print(f'Average for times is: {av}')

with open('exam.log', 'x') as file:
    for keyboard in k:
        file.write(f'{str(keyboard[0])}\n')
