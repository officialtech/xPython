********************************************** STATIC VARIABLES *****************************************

The variables which are declared inside the class and outside the 'method' are called static variable.

Static variables will holds common values for every object.

Static variables will get memory for one time.

To call static variables we use class name.

Static variable will get memory at class loading time.



class Employee:
    c_name = "official tech"
    c_cno = 10010101000010
    
print(Employee.c_name)
print(Employee.c_cno)

*******************************************************************************************************************

# Using global and static variable in function

a = 1010
print(a)
class Employee():
    c_name = "official tech"
    c_cno = "10010101000010"

print(a)
print(Employee.c_name)
print(Employee.c_cno)

def function():
    print(a)
    print(Employee.c_name)
    print(Employee.c_cno)

function()

**********************************************************************************************************************
                     REMEMBER BELOW WE ARE CREATING TWO 'PYTHON FILES' OR MODULES
**********************************************************************************************************************

# Import a class to another class

--------------------step 1: create a module, like

class Employee:
    name = "official tech"
    ctn = 1010
---------------------step 2: save as whatever.py

---------------------step 3: create annother module, like

from whatever import Employee
print(Employee.name)
print(Employee.ctn)

---------------------step 4: save as what_so_ever.py and run


