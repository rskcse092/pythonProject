

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



























