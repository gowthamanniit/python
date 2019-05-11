'''
closure:
    a closure is a set of code and scope.

    (nested function: function inside function )
 

use of closure:
*) python user must have a nested function
*) the nested function must refer to a value defined in the enclosing tag
*) the enclosing function must return the nested function
'''

def startAt(start):
    def incrementBy(inc):
        return start+inc
    return incrementBy
f=startAt(10)  # meaning:  1) calling  2) startAt(start=10)
                # 3) return incrementBy to f (hide f(start)=10)
g=startAt(100)

print(f(1))  # meaning 1) f=10 2) f or incrementBy(1) 3) called incrementBy(1)
                          # 4.return 10+1
print(g(2))
