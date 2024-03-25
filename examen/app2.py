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