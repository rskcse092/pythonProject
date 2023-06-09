import sys
import stat
import subprocess
import os
import math
import random
from datetime import datetime


#sys module
print(sys.version)
print(sys.argv)
print(sys.stdin)
print(sys.stdout)


#os module
print(os.curdir)
print(os.getcwd())
# print(os.mkdir("C:\\Users\\CSC\\PycharmProjects\\pythonProject\\pythonscripting2"))
# print(os.rmdir("C:\\Users\\CSC\\PycharmProjects\\pythonProject\\pythonscripting1"))
print(os.path)
print(os.chmod('C:\\Users\\CSC\\PycharmProjects\\pythonProject\\pythonscripting1',stat.S_IWRITE))
# print(os.remove('C:\\Users\\CSC\\PycharmProjects\\pythonProject\\pythonscripting1'))
print(os.path.join("C:\\Users\\CSC\\PycharmProjects\\pythonProject","pythonscripting3"))
print(os.path.split("C:\\Users\\CSC\\PycharmProjects\\pythonProject\\pythonscripting1"))
print(os.path.exists("C:\\Users\\CSC\\PycharmProjects\\pythonProject\\pythonscripting1"))


#to list dir using subprocess as it interacts with os
result = subprocess.run(["dir"], shell=True, capture_output=True, text=True)
print(result.stdout)

#calling other python file with stdout and stderr

result = subprocess.run(["python", "demo.py"], capture_output=True, text=True)

print(result.stdout)

#os.chmod("C:\\Users\\CSC\\PycharmProjects\\pythonProject",stat.S_IREAD)
#result = subprocess.run(["C:\\Users\\CSC\\PycharmProjects\\pythonProject", "-c", "print('This is directly from a subprocess.run() function')"], capture_output = True, text = True)

#print(result.stdout)

#calling other python file with stdout and stderr
result = subprocess.run(["python", "demo.py"], capture_output=True, text=True, check=True)

print(result.stdout)

print(result.stderr)

#popen
p = subprocess.Popen(["python", "--help"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

output, errors = p.communicate()

print(output)

#subprocess
return_code = subprocess.call(["python", "--version"])

if return_code == 0:

    print("Command executed successfully.")

else:

    print("Command failed with return code", return_code)

#math module
print(math.sqrt(4))
print(math.sin(90))
print(math.pi)
print(math.log(10,10))

#random

print(random.randrange(0,50,10))
print(random.randint(0,20))

#datetime

print("datetime usage")


now = datetime.now() # current date and time

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)

#using timestamp

from datetime import datetime

timestamp = 1528797322
date_time = datetime.fromtimestamp(timestamp)

print("Date time object:", date_time)

d = date_time.strftime("%m/%d/%Y, %H:%M:%S")
print("Output 2:", d)

d = date_time.strftime("%d %b, %Y")
print("Output 3:", d)

d = date_time.strftime("%d %B, %Y")
print("Output 4:", d)

d = date_time.strftime("%I%p")
print("Output 5:", d)

#json
import json

emp_data = '''
{  
    "employee": {  
        "name":       "Ram",   
        "salary":      1000000,   
        "married":    true  
    }  
} 
'''

print(emp_data)
a = json.loads(emp_data)
print(a)
load_data = json.loads('emp_data')
print(load_data)