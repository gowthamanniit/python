'''
Decorator

def: different names can be bound to the same function object.



'''
def sriram(msg):
    print(msg)

sriram("good person")
rubasankar=sriram  # decorator
rubasankar("nice person") # do not write called function for rubasankar
gowthaman=rubasankar # or sriram
gowthaman("teaching person")
