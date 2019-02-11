
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> INSTANCE VARIABLES <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


1.The variables which are declared inside the method using self word is called instance variable.
      2. The variables which holds the unique values for every object. 
             3. Instance variables will get memory for every object. 
                         4. To call instance variables we use object variable.
                               5. Instance variables will get memory after object creation. 


Syntax:-
          class_name()



$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  OBJECT  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$      Object is an instance of a class. Instance means allocating sufficient memory for a instance variable of a class.     $
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$



___________________________________________   Program on instance variables   _________________________________________________

class Student:  # class
    
    def assignment(self):  # instance method
        self.id = 1010   # instance variable
        self.name = 'jin'   # instance variable
        self.contact = 10010101000010   # instance variable
    
    def display(self):
        print(self.id)
        print(self.name)
        print(self.contact)


s = Student()
s.assignment()
s.display()



****************************************** WE CAN CREATE 'n' NUMBERS OF OBJECT************************************************


class Employee:
    def assign(self, id, na, sal = 0.0):
        self.idno = id
        self.name = na
        self.salary = sal
        
    def display(self):
        print(self.idno)
        print(self.name)
        print(self.salary)
        
e1 = Employee() # first object
e1.assign(100, 'jb')
e1.display()

print("---------")

e2 = Employee()
e2.assign(1010, 'Mr.chao', 250000.00)
e2.display()

print("---------")

e1.salary = 180000.00
e1.name = 'kim zong yang'
e1.display()

print("---------")

e2.salary = 3750000.00
e2.display()


##############################################################################################################################

x:- INSTANCE VARIABLES
      
      
class Employee:
    def assign(self, idno, name, salary):
        self.idno = idno
        self.name = name
        self.salary = salary
        
    def disp(self):
        print(self.idno)
        print(self.name)
        print(self.salary)
        
def show():
    e = Employee()   # local variable 'e'
    e.assign(1010, 'jb', 2564000.00)
    e.disp()
    print("outside class")

show()      


################################### Example on declaring object as local and global #############################################


class Em:
    def name_(self, idno, name, salary):
        self.idno = idno
        self.name = name
        self.salary = salary
        
    def dp(self):
        print(self.idno)
        print(self.name)
        print(self.salary)
        
f_o = Em()    # global var

def sh():
    s_o = Em()    # local var
    s_o.name_(100, 'me', 98032000.00)
    s_o.dp()
    
sh()    # function call

f_o.name_(1001010, 'class Em', 5404000.00)
f_o.dp()



