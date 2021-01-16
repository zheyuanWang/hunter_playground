def wrapClass(cls):
    def inner(a):
        print('修饰器发动! class name:', cls.__name__)
        return cls(a)
    return inner

@wrapClass
class Foo():
    def __init__(self, a):
        self.a = a
    #@wrapClass
    def fun(self):
        print('未被修饰? self.a =', self.a)


m = Foo('xiemanR')
print("------")
m.fun()