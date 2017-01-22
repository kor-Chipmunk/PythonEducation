# !/usr/bin/python
# coding: utf-8

class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.end:
            current = self.current
            self.current += 1
            return current
        else:
            raise StopIteration()

# for i in MyRange(0, 5):
#     print(i)

def YourRange(start, end):
    current = start
    while current < end:
        yield current
        current += 1
    return

# for i in YourRange(0, 5):
#     print(i)
count = 0

class MyClass:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        print(self.count)

# myclass = MyClass()
# myclass.increment()
# myclass.increment()
# myclass.increment()

class A:
    def method(self):
        print("A")

class B(A):
    def method(self):
        print("B")

class C(A):
    def method(self):
        print("C")

class D(B, C):
    pass

d = D()
d.method()