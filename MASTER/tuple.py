
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
