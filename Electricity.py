units=int(input("Enter the units consumed by you:  "))
if units < 50:
    amount=units*2.60
    print("Your bill is: ",amount)
elif units < 100:
    amount=(units*3.25)+130
    print("Your bill is: ",amount)
elif units < 200:
    amount=130+162.50+((units-200)*8.45)
    print("Your bill is: ",amount)
else:
    amount=130+162.50+526+((units-200)*8.45)
    print(amount)