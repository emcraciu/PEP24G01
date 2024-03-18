txt = 'sajd.\nlfjas'

txt_iter = txt.__iter__()
for letter in txt_iter:
    print(letter)
    if letter == '.':
        if next(txt_iter) == '\n':
            print('new text')


class oj():
     def __iter__(self):
         return IterObj([1,2])


x = oj()

for i in x:
    print(i)
class IterObj():

    def __init__(self, get_from_obj):
        self.list1 = get_from_obj

    def __iter__(self):
        return self

    def __next__(self):
        if not self.list1:
            raise StopIteration
        return self.list1.pop()