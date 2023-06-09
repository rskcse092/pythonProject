class Employee:
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal
        # class variable
        Employee.company = "XYZ"

    def __str__(self): "this is  EMP doc Built-in"

    def disp(self):
        print(" emp id is:", self.id)
        print("emp name is :", self.name)
        print("emp sal is :", self.sal)
        print("company name is:", self.company)


#  Creating two objects with args
emp1 = Employee("1", "Ram", "100000000")
emp2 = Employee("2", "Shyam", "6000000")

# calling the disp method for diff objects

emp1.disp()
emp2.disp()

# using for loop displaying the emp details

list_of_emp = [Employee("3", "Shiv", "7000000"),
               Employee("4", "Shankar", "8000000")]

for i in list_of_emp:
    i.disp()


class Employee1:
    def __init__(self):
        self.id = 100
        self.name = "abc"
        self.sal = "123456789"
        print("init method is initializing the emp values")

#calling  the __init__ method explicitly
print("calling init explicitly")

emp3 = Employee1()
print(emp3.__init__())
print(emp3.__str__())

#to understand __str__ and __repr__

# it returns a  human - friendly Built-in, while the repr() function calls __repr__()
# and returns a more information-rich Built-in that can be used to recreate the object
class Ocean:

    def __init__(self, sea_creature_name, sea_creature_age):
        self.name = sea_creature_name
        self.age = sea_creature_age

    def __str__(self):
        return f'The creature type is {self.name} and the age is {self.age}'

    def __repr__(self):
        return f'Ocean(\'{self.name}\', {self.age})'

c = Ocean('Jellyfish', 5)

print(str(c))
print(repr(c))







