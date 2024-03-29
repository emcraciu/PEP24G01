class A():
    test1 = 1

    def test_m1(self):
        print('in A')

    def fail(self):
        print('in A fail')


class D(A):

    def test_m2(self):
        print('in D')


class B(A):
    test2 = 2

    def test_m1(self):
        print('in B')


class C(A, B, D):
    test3 = 3

    def test_m1(self):
        super().test_m1()
        # super(B, self).test_m1()

    def test_m2(self):
        super().test_m2()

    def fail(self):
        super().fail()


c = C()
print(c.test1, c.test2, c.test3)
c.test_m1()
c.test_m2()
c.fail()
