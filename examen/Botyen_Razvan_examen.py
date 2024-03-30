from typing import Union, List
from datetime import datetime, timedelta


class KeyboardProductionTimes:

    def __init__(self):
        self.keyboards = []

    def add_keyboard(self, serial: str, production_time: Union[timedelta, int]):
        self.keyboards.append((serial, production_time))

    def average_production_time(self) -> Union[float, None]:
        if not self.keyboards:
            return None
        total_time = sum(time.total_seconds() if isinstance(time, timedelta) else time for _, time in self.keyboards)
        return total_time / len(self.keyboards)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self) -> List[str]:
        while self.index < len(self.keyboards):
            serial, time = self.keyboards[self.index]
            self.index += 1
            if isinstance(time, timedelta):
                time_seconds = time.total_seconds()
            else:
                time_seconds = time
            if time_seconds > 2000:
                return [serial, str(time)]
        raise StopIteration


if __name__ == "__main__":
    keyboard_times = KeyboardProductionTimes()

    keyboard_times.add_keyboard("KBO23871", timedelta(seconds=3210))
    keyboard_times.add_keyboard("KBO23873", timedelta(seconds=1890))
    keyboard_times.add_keyboard("KBO23875", timedelta(seconds=1982))

    average_time = keyboard_times.average_production_time()
    print("Average production time:", average_time, "seconds")

    with open("keyboard_production_greater_than_2000s.txt", "w") as file:
        for serial in keyboard_times:
            file.write(f"{serial}:/n")
