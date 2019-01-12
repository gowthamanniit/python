try:
    l=[1,2,3,4]
    print(l[0])
    print(l[1])
    print(l[2])
    print(l[3])
    print(l[4])

except IndexError:
    print("There is no more list")

finally:
    print("the program as been completed")
