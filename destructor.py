# # # # # # # # # # # # # # # # # # # # # # # # # #  DESTRUCTOR  # # # # # # # # # # # # # # # # # # # # # # # # # # #


DESTRUCTOR IS A SPECIAL TYPE OF METHOD WHICH IS USED TO DELETE THE OBJECT OF A CLASS

DESTRUCTOR IS CALL WHEN OBJECT GET DESTROYED

DESTRUCTOR IS CALLED ONE FOR ONE OBJECT

DESTUCTOR WILL TAKE 'self' AS A DEFAULT PARAMETER

TO DEFINE A DESTRUCTOR WE USE 'def' KEYWORD

DESTRUCTOR NAME MUST BE '__del__'

THE OBJECT DELETION DONE AUTOMATICALLY IN 'PYCHARM'

WHEREAS IN IDLE WE NEED TO DO MANUALLY USING 'del' KEYWORD


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Student:
    
    def __init__(self):
        print("I am constructor!")
        
    def display(self):
        print("I am Display!!")
        
    def __del__(self):
        print("I am destructor!!!")
        
s = Student()
s.display()
del s
