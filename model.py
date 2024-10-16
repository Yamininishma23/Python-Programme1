class A:
    def feature1(self):
        print("feature 1 is working")


class B:
    def feature2(self):
        print("feature2 is working")


class C(A, B):
    def feature3(self):
        print("feature 3 is wokring")


c = C()
c.feature3()
# decorator code
# small example

def smart_div(func):
    def inner(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)
    return inner

@smart_div
def div(a,b):
    print(a/b)

div(2,4)
