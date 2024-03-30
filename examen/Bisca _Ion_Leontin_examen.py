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
# 3b.Acest string este documentatia care se cere la punctul 3b in care documentatia moduluilui este afisata intr-un sting

from datetime import timedelta
from typing import List, Tuple


class KeyboardProductionTimes:
    """
    This app. keep the trak of the production time in Keyboard factory.
    """

    def __init__(self):
        """
        Aceasta functie initializeaza procucerea unui nou obiect in clasa KeyboardProductionTimes.
        """
        self.keyboards: List[tuple[str, timedelta]] = []

    # 1C Aceasta metoda add_keyboard adauga o tastatura
    def add_keyboard(self, serial: str, production_time: timedelta):
        """
        Aceasta metoda adauga o noua tastatura la lista
        :param serial: Se afiseaza serialul
        :param production_time: Timpul de productie
        :return:
        """
        self.keyboards.append((serial, production_time))

    # 1D Aceasta metoda average_production_time este pentru returnarea timpului de productie.
    def average_production_time(self) -> timedelta:
        """
        Returneaza timpul mediu de productie.
        :return:Media

        """
        return sum(production_time for keyboards, production_time in self.keyboards) / len(self.keyboards)


class KeyboardProductionTimesIter:
    """
    Clasa iterator asupra KeyboardProductionTimes
    """

    def __init__(self, keyboards: List[Tuple[str, timedelta]]):
        """
        Initializeaza o noua productie
        :param keyboards:
        """
        self.keyboards = keyboards
        self.index = 0

    def __iter__(self,keybords):
        return self

        """
        Returneaza noua tastatura din iterator
        :return: Noua tastatura din iterator
        """

    def __next__(self):
        if self.index >= len(self.keyboards):
            raise StopIteration
        keyboard, production_time = self.keyboards[self.index]
        self.index += 1
        return keyboard, production_time


# Puntul 3a in care documentatia ne cere type hints for aruments :


k = KeyboardProductionTimes()

k.add_keyboard("KB023871", timedelta(seconds=3210))
k.add_keyboard("KB023873", timedelta(seconds=1890))
k.add_keyboard("KB023875", timedelta(seconds=1982))
# average_production_time = keyboards.average_production_time()
print(k.keyboards)

#with open("keyboards.txt", "w") as file:
 #   for keyboard, production_time in k:
   #     file.write(f"{keyboard}, {production_time}\n")

#with open("keyboards.txt", "w") as file:
    #for keyboard in k:
        #if production_time.total_seconds() > 2000:
          #  f.write(f'{keyboard},{production_time}\n')