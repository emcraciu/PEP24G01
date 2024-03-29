"""
A production facility needs an iterable object to keep track employ working hours.
Each worker have a string name and datetime object for when he arrives to work or timedelta after he left work
Iterating the object will return all workers that have worked less than 8h (name, <timedelta>)
1) 40p: Definition
    a) 10p: Basic class structure of objects
    b) 10p: Basic class structure of iterator
    c) 10p: Method to set time when arriving to workplace
    d) 10p: Method to set time when leaving from workplace
2) 40p: Execution:
    a) 10p: Create instance of your shop
    b) 10p: Add arrival time (arrive(name, <datetime>))
        - John, 1 Jan 2022 10:30:32
        - Ana, 1 Jan 2022 9:20:25
        - Bob, 1 Jan 2022 9:10:30
    c) 10p: Set working hours (leave(name, <datetime>))
        - John, 1 Jan 2022 18:20:00
        - Ana, 1 Jan 2022 17:30:00
        - Bob, 1 Jan 2022 9:10:30
    d) 10p: Iterate the created object and write each worker with less than 8h worked in a file
3) 20p: Documenting:
   a) 5p: type hints for arguments
   b) 5p: module documentation
   c) 5p: class documentation for all classes
   d) 5p: method documentation for all methods
"""
from datetime import datetime, timedelta


class Pontaj:

    def __init__(self):
        self.caiet_pontaj = {}

    def __iter__(self):
        return IteratorPontaj(self.caiet_pontaj)

    def sosire(self, nume: str, data: datetime):
        self.caiet_pontaj.update({nume: data})

    def plecare(self, nume, data):
        self.caiet_pontaj.update({nume: data - self.caiet_pontaj[nume]})


class IteratorPontaj:
    def __iter__(self):
        return self

    def __init__(self, caiet_pontaj: dict):
        self.caiet_pontaj = caiet_pontaj

    def __next__(self):
        for nume, timp in self.caiet_pontaj.copy().items():
            timp: timedelta
            if timp.seconds < 28800:
                del self.caiet_pontaj[nume]
                return nume
            else:
                del self.caiet_pontaj[nume]
        else:
            raise StopIteration


p = Pontaj()
p.sosire(nume='John', data=datetime(2022, 1, 1, 10, 30, 32))
p.sosire(nume='Ana', data=datetime(2022, 1, 2, 12, 45, 50))
p.sosire(nume='Bob', data=datetime(2022, 1, 3, 8, 20, 15))

print(p.caiet_pontaj)

p.plecare(nume="John", data=datetime(2022, 1, 1, 18, 30, 32))
p.plecare(nume="Ana", data=datetime(2022, 1, 2, 17, 30, 32))
p.plecare(nume="Bob", data=datetime(2022, 1, 3, 16, 30, 32))
print(p.caiet_pontaj)

with open("Out.Log", "x") as file:
    for user in p:
        file.write(user)
