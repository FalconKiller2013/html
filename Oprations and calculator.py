def add(p,q):
    return p+q
def sub(p,q):
    return p-q
def mul(p,q):
    return p*q
def div(p,q):
    return p/q
print("Please select your choice:  ")
print("a. Add")
print("b. Sub")
print("c. Mul")
print("d. Div")
Choice=input("Enter your choice: a/b/c/d ")
num1=int(input("Enter the number:  "))
num2=int(input("Enter the number:  "))
if Choice == "a":
    print("The addition of num1 and num2 is",add(num1,num2))
elif Choice == "b":
    print("The subtracttion of num1 and num2 is",sub(num1,num2))
elif Choice == "c":
    print("The multiplication of num1 and num2 is",mul(num1,num2))
elif Choice == "d":
    print("The division of num1 and num2 is",div(num1,num2))
else:
    print("invalid choice")