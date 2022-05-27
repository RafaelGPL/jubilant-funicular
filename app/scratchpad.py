

# Class attributes are simply variables that belong to a class.
# this means, you can access them through the "." operator.
class MyClass:
    zvalue = None

    def __init__(self, xvalue, yvalue):
        self.xvalue = xvalue                # this and yvalue are now class attributes.
        self.yvalue = yvalue

    def square_x_value(self):               # this is a method
                                            # a method is a function that belongs to a class.
        return self.xvalue**2               # you can access this method via the dot operator.


if __name__ == "__main__":
    myobject = MyClass(5, 10)               # myobject is an instance of MyClass.
                                            # an instance of class is said to be an object
    print("%s squared is: " % (myobject.xvalue))
    print(myobject.square_x_value())
