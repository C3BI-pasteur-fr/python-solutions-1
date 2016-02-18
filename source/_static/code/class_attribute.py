class MyClass(object):

    class_attr = 'foo'

    def __init__(self, val):
        self.inst_attr = val




a = MyClass(1)
b = MyClass(2)

print a.inst_attr
1
print b.inst_attr
2

print a.class_attr == b.class_attr
True
print a.class_attr is b.class_attr
True

b.class_attr = 4

print a.class_attr
4
del a.class_attr

MyClass.class_attr = 4