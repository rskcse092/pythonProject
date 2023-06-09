s = "Ram"
print(s[2])
s1 = ["ram","shyam","mohan"]
print(s1[2])
t1 = ("hi","hello","tank")
print(2)
y = "computer"
print(y[1:3])
print(y[1:6])
print(y[1:6:2])
print(y[:5])
print(y[-1])
print(y[-2])
print(y[-3])

X = 'RAM'+'SHANKAR'
Y = ['RAM','SHANKAR','KUMAR']+['DEV']
Z = ('RAM','SHYAM') + ('SUNDAR', 'MEN')
print(X)
print(Y)
print(Z)

str = 'bug'*3
print(str)

lst = [1,2,3,4,5]*3
print(lst)

tup = (1,2,3)*4
print(tup)

string  = 'RAMSHANKARKUMAR'
print('RAM' in string)
print("length of Built-in" , len(string))
print(max(string))
print(min(string))
print(sorted(string))
print("count", string.count('R'))
print(string.index('KAR'))


list = [1,2,3,4,5]
list1 = ['python','scala','java','python']
print(5 not in list)
print("length of list :" , len(list))
print(max(list))
print(min(list))
print(sum(list))
print(sorted(list1))
print("Sorting list by second letter", sorted(list1, key = lambda k: k[1]))
print("count", list1.count('python'))
print(list1.index('scala'))
a,b,c,d = list1
print("unpacking list:", a,b,c,d)


tuple = ('BACK','STREET','BOYS')
tuple1 = (1,2,3,4,5,100000,100000,100000,5000000000)
print("Sorting tuple by second letter", sorted(tuple, key = lambda k: k[1]))

print('Boys' in tuple)
print("length of tuple" , len(tuple))
print(max(tuple))
print(min(tuple))
print(sum(tuple1))
print(sorted(tuple))
print('count', tuple1.count(100000))
print(tuple1.index(5000000000))
a,b,c = tuple
print("unpacking tuple:", a,b,c)

lst = [1,2,3,4,5]
for item in lst:
    print(item)

for index , item in enumerate(lst):
    print(index,item)

print("//creating new list//")

el = []
print(el)

elwe = [1,2,'one','two']
print(elwe)

etwe = (1,2,3,4,5)
print([i for i in etwe])
print([*etwe])

def createListFromTuple(etwe):
    return [*etwe]

def createListFromTuple1(etwe):
    return [i for i in etwe]

print("function to create list from a tuple")
print(createListFromTuple(etwe))
print(createListFromTuple1(etwe))


lc = [i*i for i in range(10) if i>=5]
print(lc)

#del

a = [1,2,3,4]
b = [5,6,7,8]

print(a.__delitem__(0))
del(a[1])
print(a)
del(b)


#append

a.append(10)
print(a)
#extend

b = [100,200]
a.extend(b)
print(a)

#insert
a1  = [10,20,30,40,50]
print(a1)
a1.insert(5,300)
print(a1)
a1.insert(6,['RAM','SHANKAR'])
print(a1)

#pop

a1.pop()
print(a1)

a1.pop(0)
print(a1)


b1 = a1.pop(0)
print(b1)

print(a1.pop())

#remove

a1 = ['ram','a',1,3,2,4]
print(a1)
a1.remove('a')
print(a1)

#reverse and sort

b3 = [90,80,60,30,40,50]
b3.reverse()
print(b3)
b3.sort()
print(b3)
print(type(b3.sort()))
print(type(sorted(b3)))
print(sorted(b3))

b3.sort(reverse=True)
print(b3)

b3.sort(reverse=False)
print(b3)

#creating new tuple

t1 = ()
t2 = (1,2,3)
t3 = 1,2,3,4,5
t4 = 6,
l1 = [7, 8, 9]
print(t1)
print(t2)
print(t3)
print(t4)
#t5 = tuple(l1)
#print(t5)

t5 = (1,3,5,7,2,4,[8,9,10])
print(t5)
del(t5[6][2])
print(t5)
t5 += 10,
print(t5)
t5[6].append(12)
print(t5)

#creating set and add,remove,pop,len,in,clear

set1 = {}
print(set1)
s1 = {1,2,3,4,5,6}
print(s1)

s2 = set(l1)
print(s2)

s2.add(10)
print(s2)

s2.pop()
print(s2)

s2.remove(7)
print(s2)

print(len(s2))

print(10 in s2)

print(s2.clear())
print(s2)

s3 = {1,2,3,4,5}
s4 = {5,6,7,8,9,10}
print(s3)
print(s4)
print(s3 & s4)
print(s3 ^ s4)
print(s3 | s4)
print(s3 > s4)
print(s3 < s4)
print( s3 == s4)
print(s3 >=s4 )
print( s4<=s4 )

# creating dict

d = {1,2,3,4,5,6,7,8,9}
print(d)
d1 = dict(x=30,y=40,z=50)
print(d1)
d2 = dict([(1,'one'),(2,'two')])
print(d2)
d1['w']=60
print(d1)

dict1 = dict([(1,'ONE')])
print(dict1)

del(dict1)

d2.clear()
print(d2)


dict2 = dict([(1,'ONE'),(2,'TWO')])
print(len(dict2))
print(dict2)

for key in d1:
    print(key, d1[key])

for key,val in d1.items():
    print(key,val)

#list comprehensions

import random

under_10 = [i for i in range(10)]
print(under_10)

under_10_sq= [i*i for i in range(10)]
print(under_10_sq)

under_10_even=[i for i in range(10) if i%2==0]
print(under_10_even)

under_10_odd=[i for i in range(10)  if i%2==1]
print(under_10_odd)

s = "i have 1500000 rupees salary and i spend 500000 for daily expanses"
num = [i for i in s if s.isnumeric()]
print(num)

lis = ['shambhu' , 'ram','shiv','bhagwan',]
idx = [k for k , v in enumerate(lis) if v=='shambhu']
print('index of shambhu is :', (idx))

S1 = [i for i in 'ABCDEFGH']
random.shuffle(S1)
S2 = [i for i in 'ABCDEFGH' if i!= 'C' ]
print(S1)
print(S2)

LIST = [4,5,6,7,8,9,10]

a = [i if i%2==0 else i*10 for i in LIST]
print(a)

list_of_list = [[1,2],[3,4],[5,6]]
e = [i for b in list_of_list for i in b ]
print(e)

























