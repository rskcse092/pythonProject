numr=int(input("Enter range:"))

print("Prime numbers:",end=' ')
count = 0
for n in range(1,numr):

    for i in range(2,n):

        if(n%i==0):

            break

    else:

        print(n,end=' ')
        count = count + 1

print("no of prime no in range of given no is :", count)