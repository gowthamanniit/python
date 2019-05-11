'''
Generator --> yield (return all values to generator)

use:
    1) easy to implements
    2) memory efficient
    3) represent infinite system
    4) pipeline generator


'''

# method 1
def createGene():
    mylist=range(5)
    for i in mylist:
        yield i*i
    

mygen=createGene()
print(type(mygen)) # genrator type
for i in mygen:
    print(i)

#method 2

def createGene():
    for i in range(10,0,-1):
        yield i*i    
mygen=createGene()
for i in mygen:
    print(i)
