# 1,3,4,8,9,10
#
# 2,5,7,10,12

a = [1,3,4,8,9,10]
b = [2,5,7,10,12]

c = []
for i in range(len(a)):
    if(a[i] not in b):
            c.append(a[i])

for j in range(len(b)):
    c.append(b[j])

print(c)
print(len(c))

for k in range(len(c)-1):
    if(c[k]<c[k+1]):
        pass
    else:
        temp=c[k]
        c[k]=c[k+1]
        c[k+1]=temp

print("pass1 to sort")
print(c)

for k in range(int(len(c)/2)):
    if(c[k]<c[k+1]):
        pass
    else:
        temp=c[k]
        c[k]=c[k+1]
        c[k+1]=temp

print("pass2 to sort")
print(c)

for k in range(len(c)-1):
    if(c[k]<c[k+1]):
        pass
    else:
        temp=c[k]
        c[k]=c[k+1]
        c[k+1]=temp

print("pass3 to sort")
print(c)

for k in range(len(c)-1):
    if(c[k]<c[k+1]):
        pass
    else:
        temp=c[k]
        c[k]=c[k+1]
        c[k+1]=temp

print("pass4 to sort")
print(c)