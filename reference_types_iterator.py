'''
1) iterator
    def: it is object (traverse throguth all elements of a collection(list,tuple))
   2 methods:
       1) iter --> to convert list to iterator(iter)
       2) next --> to take elements individual one by one
    

'''
import sys # this package is used to exit function
mylist=[1,2,3,4,5]

it=iter(mylist)
print(next(it))
print(next(it))
print(next(it))

# or

for x in it:
    print(x,end=" ")

# or

mylist.append(6)
mylist.append(7)
mylist.append(8)

it=iter(mylist)
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
        




