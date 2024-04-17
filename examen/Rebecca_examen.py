"""
A production facility needs an iterable object to keep track product assembly times.
A class called "KeyboardProductionTimes" that will store the information needs to be created.
Each keyboard will have a string serial number "KBXXXXXX" and timedelta for production time
Iterating objects created with KeyboardProductionTimes will return all keyboards that had production
time greater than 2000s
1) 40p: Definition
    a) 10p: Basic class structure of KeyboardProductionTimes
    b) 10p: Basic class structure of iterator
    c) 10p: Method to add produced keyboards with serial, production start and production stop
    d) 10p: Method that returns average keyboard production time
2) 40p: Execution:
    a) 10p: Create instance of KeyboardProductionTimes
    b) 10p: Call method to add keyboard <add_keyboard(serial, start_time, end_time>)>
        - KB023871, datetime(any) datetime(any)
        - KB023873, datetime(any) datetime(any)
        - KB023875, datetime(any) datetime(any)
    c) 10p: Call method to return average production time <average_production_time()>
    d) 10p: Iterate the created object and write each keyboard serial with production
            time greater then 2000s in a file on a new line
3) 20p: Documenting:
   a) 5p: type hints for arguments
   b) 5p: module documentation
   c) 5p: class documentation for all classes
   d) 5p: method documentation for all methods
"""
from datetime import datetime, timedelta


class KeyboardProductionTimes:
    ''' this is a docstring'''

    def __init__(self):
        self.depozit_k = {}

    def __iter__(self):
        return Iterator(self.depozit_k)

    def add_keyboard(self, seria: str, start: datetime, stop: datetime):
        ''' This method will add keyboards to the depozit'''
        prod_time = stop - start
        self.depozit_k.update({seria: prod_time})

    def average_product_time(self):
        t = 0
        for seria, prod_time in self.depozit_k.items():
            t += prod_time.seconds
        return t / len(self.depozit_k)


class Iterator:

    def __iter__(self):
        return self

    def __init__(self, depozit_k: dict):
        self.depozit_k = depozit_k

    def __next__(self):
        for seria, prod_time in self.depozit_k.copy().items():
            if prod_time.seconds < 2000:
                del self.depozit_k[seria]
                return seria
            else:
                del self.depozit_k[seria]
        else:
            raise StopIteration


k = KeyboardProductionTimes()
k.add_keyboard(
    seria="KB023871",
    start=datetime(2019, month=1, day=20, hour=10, minute=50, second=32),
    stop=datetime(2019, month=1, day=20, hour=11, minute=20, second=30))
k.add_keyboard(
    seria="KB023873",
    start=datetime(2019, month=1, day=20, hour=11, minute=31, second=33),
    stop=datetime(2019, month=1, day=20, hour=12, minute=30, second=25))

print(k.depozit_k)
print(k.average_product_time())

with open('out.log', 'x') as file:
    for value in k:
        file.write(value)