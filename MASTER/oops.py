#class(bluprint) ,oject(instace of class) and encapsulation(wrapping data and method into a single unit and accessing through same objects called class Person)
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f"name and age is :{self.name},{self.age}")

p1 = Person("RAM",35)
p2 = Person("Shyam",45)
p1.show()
p2.show()


class Person1:
    def __init__(self):
        self.name=''
        self.age=0
    def get(self):
        self.name = input("enter the name:")
        self.age = input("enter the age:")

    def show(self):
        print(f"name and age is :{self.name},{self.age}")


p11 = Person1()
p11.get()
p11.show()

p11 = Person1()
p11.get()
p11.show()

#inheritance

#single
class A():
    a = 5
    b = 10

    def disp(self):
        print("this is A")
        print(f"value of a and b are:{self.a},{self.b}")

class B(A):
    def show(self):
        print("this is B")

ob = B()
ob.disp()
# by using child class object we can access the parent class data member and method


# multilevel
class A():
    a = 5

    def dispA(self):
        print("this is A")
        print(f"value of a IS are:{self.a}")

class B(A):
    b = 10

    def dispB(self):
        print("this is B")
        print(f"value of B is {self.b}")
class C(B):
    def dispC(self):
        print("this is C")


ob = C()
ob.dispA()
ob.dispB()
ob.dispC()

# by using child class object we can access both two parent class properties


# multiple
class A():
    a = 5

    def dispA(self):
        print("this is A")
        print(f"value of a IS are:{self.a}")

class B():
    b = 10

    def dispB(self):
        print("this is B")
        print(f"value of B is {self.b}")
class C(A,B):
    def dispC(self):
        print("this is C")


ob = C()
ob.dispA()
ob.dispB()
ob.dispC()

# by using child class object we can access both two parent class properties

#polymorphism