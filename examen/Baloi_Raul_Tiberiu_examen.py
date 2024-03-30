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
    Class that stores information
    """

    def __init__(self):
        """
        Constructor for keyboardproductiontimes
        """
        self.keyboard = []

    def add_keyboard(self, serial: str, production_time: int):
        """
        add keyboard with serial number and production time
        """
        self.keyboard.append((serial, production_time))

    def average_keyboard_production_time(self):
        """
        Calculate and return the average production time
        """
        total_time = sum(prod_time for serial, prod_time in self.keyboard)
        num_keyboards = len(self.keyboard)
        if num_keyboards == 0:
            return 0
        else:
            return total_time / num_keyboards

    def __iter__(self):
        """
        return an iterator
        """
        return KeyboardIterator(self.keyboard)


class KeyboardIterator:
    """
    Iterator for Keyboard production Times class that select only above 2000
    """

    def __init__(self, keyboards):
        self.keyboards = keyboards
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.keyboards):
            serial, production_time = self.keyboards[self.index]
            self.index += 1
            if production_time > 2000:
                return serial, production_time
            else:
                raise StopIteration

    """
    Executie
    """


keyboardpt = KeyboardProductionTimes()
keyboardpt.add_keyboard("KB023871", 3210)
keyboardpt.add_keyboard("KB023873", 1890)
keyboardpt.add_keyboard("KB023875", 1982)
"""
Crearea unui fisier cu continut si printare
"""
with open("Keyboard_production_times.txt", "w") as file:
    keyboard_info = []
    for serial, time in keyboardpt:
        file.write(f"{serial}\n")
        keyboard_info.append((serial, time))
        print("Keyboards above 2000:")
    for serial, time in keyboard_info:
        print(f"Serial:{serial}")
average_time = keyboardpt.average_keyboard_production_time()
print(f"Average Production Time : {average_time}seconds")
