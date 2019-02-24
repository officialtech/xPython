# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

     # # # # # # # # # # # # # # # # # # # # #  Reffered Object # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     

Using reffered object we can call multiple methods for multiple time



example



class _anything:
    
    def assign(self, idno, name, fee = 100):
        self.idno = idno
        self.name = name
        self.fee = fee
        
    def show(self):
        print("ID NO:", self.idno)
        print("NAME:", self.name)
        print("FEE:", self.fee)
        
_any = _anything() # creating object and assigninng to variable
# _anything() object is reffered to '_any' 
_any.assign(808, 'Ben', 1000)
_any.show()



# # # # # # # # # # # # # # # # # # # # # Unreffered Object # # # # # # # # # # # # # # # # # # # # #

Using unreffered onject we can call one method for one time


example


class _anything:
    
    def assign(self, idno, name, fee = 100):
        self.idno = idno
        self.name = name
        self.fee = fee
        
    def show(self):
        print("ID NO:", self.idno)
        print("NAME:", self.name)
        print("FEE:", self.fee)
        
_anything().assign(1010, 'Ravi') # you can only do this
#if you call show() method it will give error
#_anything.show()




****************************************************************************************************

AttributeError                            Traceback (most recent call last)
<ipython-input-2-8bff9dce9daa> in <module>
     12 
     13 _anything().assign(1010, 'Ravi')
---> 14 _anything().show()

<ipython-input-2-8bff9dce9daa> in show(self)
      7 
      8     def show(self):
----> 9         print("ID NO:", self.idno)
     10         print("NAME:", self.name)
     11         print("FEE:", self.fee)

AttributeError: '_anything' object has no attribute 'idno'   # because another object is created when we write "_anything()"

***************************************************************************************************




