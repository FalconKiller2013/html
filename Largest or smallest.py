number=int(input("Enter a number: "))
number2=int(input("Enter a number: "))
if number>number2:
    print(f"{number} is greater than {number2}")
elif number == number2:
    print(f"{number} and {number2} are equal")
else:
    print(f"{number} is less than {number2}")  