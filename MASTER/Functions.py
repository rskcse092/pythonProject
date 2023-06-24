def sum_number(*argss):
    return sum(argss)

sum1 = sum_number(1,2,3,4)
print("sum of nos are:",sum1 )

def print_keyval(**kargs):
    for key,val in kargs.items():
        print(f"key and values are : {key} {val}")

print_keyval(one=1,two=2)


feet1= 50
feet2 = 50
inch1=1
inch2 = 3

def convert_into_feetandinch():
    f = feet2+feet1
    i = inch1+inch2
    nf = int(i%12)
    ff = int(i/12)
    print(f"nf is {nf}")
    if(i>=12*ff):
        i = nf
        f = f+ff
    print(f"converted feet and inch is:{f},{i}")

convert_into_feetandinch()


class pyclass():
    t = 1
    age = 2

ob1 = pyclass()
ob2 = pyclass()
print(ob1.t)
print(ob1.age)
ob1.t = 10
ob1.age = 20
print(ob1.t)
print(ob1.age)
ob2.t = 100
ob2.age = 200
print(ob2.t)
print(ob2.age)


