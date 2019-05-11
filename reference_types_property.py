'''
property

def: to use getter and setter function.


'''

class student:
    def __init__(self):
        self.a=0
    def getvalue(self):
        return self.a
    def setvalue(self,a):
        self.a=a

s1=student()   # a = 0
s1.setvalue(100)  # a=100
print(s1.getvalue()) # a=100

s2=student()   # a = 0
#use set method
print(s2.getvalue()) # a=400


