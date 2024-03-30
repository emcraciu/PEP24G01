from typing import Union, List
from datetime import timedelta


class KeyboardProductionTime:
    """
    Class to keep track of keyboard production time.
    """

    def __init__(self):
        """
        Initializes KeyboardProductionTime with an empty list to store keyboard production data.
        """
        self.keyboards = []

    def add_keyboard(self, serial: str, production_time: Union[int, timedelta]):
        """
        Add a keyboard with its serial number and production time to the list.

        Args:
        :param serial:The serioal number of the keyboard
        :param production_time: Production time of the beyboard
        :return:
        """
        self.keyboards.append((serial, production_time))

    def averege_production_time(self) -> Union[float, None]:
        """
        Calculates the averege production time of all keyboards
        :return:
            Union[float, None]: The averege production time in seconds, or None if no keyboards heve been added.
        """
        if not self.keyboards:
            return None
        total_time = sum(production_time.total_seconds() if isinstance(production_time, timedelta) else production_time
                         for _, production_time in self.keyboards)
        return total_time / len(self.keyboards)

    def __iter__(self):
        """
        Returns an iterator object
        :return:
        iter:An iterator object.
        """
        return KeyboardIterator(self.keyboards)


class KeyboardIterator:
    """
    Iterator class to iterate over keyboards with production time greater the 2000s
    """

    def __init__(self, keyboards: List[tuple]):
        """
        The list of keyboards
        :param keyboards:  a list of tuples containing keyboard ser. numb. and production time.
        """
        self.keyboards = keyboards
        self.index = 0

    def __iter__(self):

        return self

    def __next__(self) -> str:

        while self.index < len(self.keyboards):
            serial, production_time = self.keyboards[self.index]
            self.index += 1
            if isinstance(production_time, int) and production_time > 2000:
                return serial
            elif isinstance(production_time, timedelta) and production_time.total_seconds() > 2000:
                return serial
            raise StopIteration


if __name__ == "__main__":
    keybord_time = KeyboardProductionTime()

    keybord_time.add_keyboard("KB023871", 3210)
    keybord_time.add_keyboard("KB023873", 1890)
    keybord_time.add_keyboard("KB023875", 1982)

    average_time = keybord_time.averege_production_time()
    print("Avrage production time:", average_time)

    with open('keyboards.txt', 'w') as file:
        for keybord_serial in keybord_time:
            file.write(keybord_serial)
