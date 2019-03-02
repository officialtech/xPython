#######################################################  self  ########################################################

# self

> self is a ddefault parameter in instance methods and constructor

> In a class 'self' represents 'current class object reference' 

> we can rename the self word

##############################################################################

class Employee:
    
    def __init__(self, idno, name, contact):
        self.idno = idno
        self.name = name
        self.contact = contact
        
    def show(self):
        print("ID NO", self.idno)
        print("Name", self.name)
        print("Contact Number", self.contact)
        
eo = Employee(980, "official tech", 320)
eo.show()

################################################################################

class Employee:
    
    def __init__(whatever, idno, name, contact):
        whatever.idno = idno
        whatever.name = name
        whatever.contact = contact
        
    def show(hereToo):
        print("ID NO", hereToo.idno)
        print("Name", hereToo.name)
        print("Contact Number", hereToo.contact)
        
eo = Employee(980, "official tech", 320)
eo.show()
