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

from datetime import timedelta


class KeyboardProductionTimes:
    """
  A class to track keyboard production times.
  """

    def __init__(self):
        self.keyboards = []  # List to store keyboard data

    def add_keyboard(self, serial_number, production_time):
        """
    Adds a keyboard to the list with its serial number and production time.
    """
        if not isinstance(serial_number, str) or not serial_number.startswith("KB"):
            raise ValueError("Serial number must be a string starting with KB")
        self.keyboards.append((serial_number, production_time))

def average_production_time(self):
    """
Calculates the average production time of all keyboards.
"""
    total_time = sum(time for _, time in self.keyboards)
    return total_time / len(self.keyboards) if self.keyboards else 0

def _iter_(self):
    """
Defines iterator to return keyboards with production time exceeding 2000s.
"""
    return LongProductionKeyboardIterator(self.keyboards)

class LongProductionKeyboardIterator:
    """
  Iterator class to return long production time keyboards.
  """

    def _init_(self, keyboards):
        self.keyboards = keyboards
        self.index = 0

    def _next_(self):
        """
    Returns the next keyboard with production time exceeding 2000s or raises StopIteration.
    """
        while self.index < len(self.keyboards):
            serial, time = self.keyboards[self.index]
            if time > 2000:
                self.index += 1
                return f"{serial}: {time}s"
            self.index += 1
        raise StopIteration
# Execution Example
production_tracker = KeyboardProductionTimes()
production_tracker.add_keyboard("KB023871", 3210)
production_tracker.add_keyboard("KB023873", 1890)
production_tracker.add_keyboard("KB023875", 1982)

# Calculate and print average time
average_time = production_tracker.average_production_time()
print(f"Average_Production_Time: {average_time:.2f}s")

# Write long production keyboards to a file
with open("long_production_keyboards.txt", "w") as file:
    for keyboard in production_tracker:
        file.write(f"{keyboard}\n")
print("Long production time keyboards written to 'long_production_keyboards.txt'")