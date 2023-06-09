print("welcome to master program in cse")
name = "ram"
age = 29

print(" I am " + name + "of age " + str(age))
print(type(name))
print(f"my name is {name} and i am {age} years old")

a,b = [int(x) for x in input("enter the no:").split(',')]
print(f"a is {a} and b is {b}")

a = 1
print(bin(a))
print(oct(a))
print(hex(a))


l = [1,2,3]
b = bytes(l)
ba = bytearray(l)
s = set(l)
print(s)
d = {1:"one",2:"two"}
print(d)
# b[0]=5
ba[0]=6
print(b[0])
for i in b:
    print(b)

for i in ba:
    print(ba)

gv = 1
def fun(a,b):
    lv = 2
    print(f"fun args are  {a}, {b} and local and global vales are {gv}  and {lv}")

fun(3,4)
# print(lv)
print(gv)

l,b = [int(x) for x in input("enter length and breadth of rectangle").split(',')]
print("area of rectangle is ", l*b)
