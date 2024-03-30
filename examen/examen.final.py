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

    def __iter__(self):
        """
        Defines iterator to return keyboards with production time exceeding 2000s.
        """
        return LongProductionKeyboardIterator(self.keyboards)


class LongProductionKeyboardIterator:
    """
    Iterator class to return long production time keyboards.
    """

    def __init__(self, keyboards):
        self.keyboards = keyboards
        self.index = 0

    def __next__(self):
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
print(f"Average Production Time: {average_time:.2f}s")

# Write long production keyboards to a file
with open("long_production_keyboards.txt", "w") as file:
    for keyboard in production_tracker:
        file.write(f"{keyboard}\n")

print("Long production time keyboards written to 'long_production_keyboards.txt'")
