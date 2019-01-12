try:
    a=int(input("Enter 1st value:"))
    b=int(input("Enter 2nd value:"))
    c=a/b
    print("the div value is:",c)
    
except ZeroDivisionError:
    print("Can,t div value 0")

finally:
    print("The program as been completed")

    
