from datetime import timedelta


class KeyboardProductionTimes:
    """
    Class for storing information about keyboard production times.

    Attributes:
        keyboards (dict): Dictionary to store keyboards with their serial numbers and production times.
    """

    def _init_(self):
        """Initialize an instance of KeyboardProductionTimes."""
        self.keyboards = {}

    def add_keyboard(self, serial: str, production_time: timedelta):
        """
        Add a produced keyboard with its serial number and production time.

        Args:
            serial (str): The serial number of the keyboard.
            production_time: The production time of the keyboard.
        """
        self.keyboards.update({serial: production_time})

    def average_production_time(self):
        """
        Calculate the average production time of all keyboards.

        Returns:
            float: The average production time in seconds.
        """
        total_time_seconds = sum((prod_time.total_seconds() for prod_time in self.keyboards.values()), 0)
        total_time = timedelta(seconds=total_time_seconds)
        num_keyboards = len(self.keyboards)
        return total_time.total_seconds() / num_keyboards if num_keyboards > 0 else 0

    def _iter_(self):
        """
        Iterate over keyboards with production times greater than 2000s.

        Yields:
            str: The serial number of each keyboard with production time greater than 2000s.
        """
        for serial, production_time in self.keyboards.items():
            if production_time > timedelta(seconds=2000):
                yield serial


# Create an instance of KeyboardProductionTimes
keyboard_times = KeyboardProductionTimes()

# Add keyboards with their production times
keyboard_times.add_keyboard("KB023871", timedelta(seconds=3210))
keyboard_times.add_keyboard("KB023873", timedelta(seconds=1890))
keyboard_times.add_keyboard("KB023875", timedelta(seconds=1982))
print(keyboard_times.keyboards)

# Call method to return average production time
average_time = keyboard_times.average_production_time()
print(f"Average production time: {average_time} seconds")

# Iterate over the created object and write each keyboard serial with production time greater than