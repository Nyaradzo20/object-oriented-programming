class dog:
     def __init__(self, name):
         self.name = name #its means we have created an attribute of dog with a name name
         print(name)
         pass
     def add(self, x):
         return 9 + 1
     def bark(self):
         print('bark')
d = dog("beans") 
d2 = dog("gile")
print(d.add(8))
d.bark 
##############################################
