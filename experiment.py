class A(object):
    _test = '1'
    __test = '2'

class B(A):

    def _print(self):
        print(self._test)

    def __print(self):
        print(self)


a = A()
a._
print(a._test)
print(a._A__test)

b = B()
b.print_()
b.print__()