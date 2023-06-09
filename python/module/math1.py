import math as m
import os as o
import random as  r
import datetime

mydate = datetime.datetime.now()

print("__str__() Built-in: ", mydate.__str__())
print("str() Built-in: ", str(mydate))

print("__repr__() Built-in: ", mydate.__repr__())
print("repr() Built-in: ", repr(mydate))


l = dir(m)
for i in l:print(i)

print(m.e)
print(m.pi)
print(m.inf)
print(m.sqrt(5))
print(m.pow(2,3))
print(m.gcd(40,4))
print(m.lcm(2,3))
print(m.sin(90))
print(m.log(1,10))

print(o.getcwd())


#finding the unrepeated elements in list

a = [1, 2, 3, 4, 5, 1, 2]

print(a.count(1))
print(a.count(2))
print(a.count(3))

print("using loop")
for i in a:
    if(a.count(i)==1):
        print(i)

sample_list = [1, 2, 3, 4, 5, 1, 2]

def countOccurrence(a):
  k = {}
  for j in a:
    if j in k:
      k[j] +=1
    else:
      k[j] =1
  return k

print(countOccurrence(sample_list))


t1 = (1,2,3,[4,5,6],7)
print(t1)
t1[3][1] = 10
print(t1)

#
# a = [1,2,3,4]
# s = ["one","two","three","four"]
#
# d = {}
# # c =  {1:"one",2:"two"}
#
# for i in range(len(a)):
#     for j in range(len(s)):
#         print(i+  ":" +j)






a = [10, -5, 30, 4, 3, 25, -1]

print(len(a))
b = a.sort
print(b)
for i in range(len(b)):
    max1 = a[0]
    if(b[i] >  max1):
        max1 = b[i]

print(max1)












