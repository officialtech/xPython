**********************************************# STATIC VARIABLES *****************************************

# The variables which are declared inside the class and outside the 'method' are called static variable.

# Static variables will holds common values for every object.

# Static variables will get memory for one time.

# To call static variables we use class name.

# Static variable will get memory at class loading time.



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
                     # REMEMBER BELOW WE ARE CREATING TWO 'PYTHON FILES' OR MODULES
**********************************************************************************************************************

# Import a class to another class

--------------------# step 1: create a module, like

class Employee:
    name = "official tech"
    ctn = 1010
---------------------# step 2: save as whatever.py

---------------------# step 3: create annother module, like

from whatever import Employee
print(Employee.name)
print(Employee.ctn)

---------------------# step 4: save as what_so_ever.py and run


----------------------------------#  Program on instance and static variable  ----------------------------------------------


class Official_tech:
    # static block start
    
    comp_name = 'official tech Inc.'
    comp_c_no = 10010101000010
    
    # static block ends
    
    def team_member(self, id, name, salary = 00.00):   # Remember this is a method, not a function
        # Instance block
        
        self.i_d = id
        self.n_m = name
        self.sal = salary
        
    def mess_disp(self):
        print(Official_tech.comp_c_no) # printing Static variable using Class name
        
        print(self.i_d)  #  printing instance variable 
        print(self.sal)  
        print(self.n_m)
        
        print(Official_tech.comp_name)
        

obj_var = Official_tech()  # 1.creating object and storing to variable

obj_var.team_member(808, 'tppa', 400000.00) # giving arg's to parameters
obj_var.mess_disp()
print("~ " * 10)

obj_var1 = Official_tech()  # 2.creating another object and storing to variable
obj_var1.team_member(1010, 'sqst', 350000.00)
obj_var.mess_disp()
print("~ " * 10)

print(obj_var.comp_name)  # calling static variable
print("~ " * 10)

print(obj_var1.i_d)  # calling Instance variable
print(obj_var1.comp_c_no)

