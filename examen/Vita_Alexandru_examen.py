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


class IterKeyboard:
    """
    This is an iterator for iterating keyboards with production time
    """

    def __init__(self, keyboards):
        self.keyboards = keyboards
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.keyboards):
            keyboard = self.keyboards[self.index]
            self.index += 1
            if keyboard[1] > 2000:
                return keyboard
            raise StopIteration

    # def __init__(self, keyboards_filter):
    #     self.keyboards_filter = []
    #
    #     for key_boards in self.keyboards_filter:
    #         if key_boards[1] > 2000:
    #             self.keyboards_filter.append(key_boards)
    #
    # def __iter__(self):
    #     return self
    #
    # def __next__(self):
    #     return self.keyboards_filter


class KeyboardProductionTime:
    """
    This class add keyboards and will return average keyboard production time
    """

    def __init__(self):
        self.keyboards = []

    def __iter__(self):
        return IterKeyboard(self.keyboards)

    def add_keyboards(self, serial: str, time: int):
        """
        This method will add keyboards and will record (serial and time )
        :param serial: serial for keyboard
        :param time: production time
        :return: a list of created keyboards
        """
        self.keyboards.append((serial, time))
        # self.add_keyboards.append({'serial': serial, 'time': time})

    def average_production_time(self):
        """
        This method return average production time
        :return: average_time
        """
        total_time = 0

        if len(self.keyboards) > 0:
            for serial, time in self.keyboards:
                total_time += time

            # calculate average time
            average_time = total_time / len(self.keyboards)
            return average_time
        else:
            return 0


keyboard_prod = KeyboardProductionTime()

keyboard_prod.add_keyboards('KB023871', 3210)
keyboard_prod.add_keyboards('KB023873', 1890)
keyboard_prod.add_keyboards('KB023875', 1982)

print(f'This represent serial + time of : {keyboard_prod.keyboards}')
print(f"This represent average time : {keyboard_prod.average_production_time()} sec")

with open('keyboards_over_2000s.txt', 'w') as file:
    for serial, time in keyboard_prod:
        file.write(f"{serial} \n")
print("Keyboards with production time greater than 2000s have beem writen to keyboards_over_2000s.txt ")
