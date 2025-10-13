try:
    num1,num2=eval(input("Enter any number seperated buy comma:  "))
    result=num1/num2
    print(result)
except ZeroDivisionError:
    print("Cannot divide with zero:   ")
except SyntaxError:
    print("Seprate numbers with comma:  ")
except:
    print("WRONG INPUT!")
finally:
    print("I will execute ANY HOW.")                