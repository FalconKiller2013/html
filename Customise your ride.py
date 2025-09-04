print("Choose a vehicle bike or a car:  ")
print("1.Bike")
print("2.Car")
choice=int(input("Enter your choice 1 or 2:  "))
if choice == 1:
    print("You have selected Bike")
    print("You have selected bike, choose your bike")
    print("1.Scooter")
    print("2.Super bike")
    choice1=int(input("Enter your choice:  "))
    if choice1 ==1:
        print("You have selected scooter")
    else:
        print("You have selected super bike")
else:
    print("You have selected Car")
    print("You have selected Car, choose your car")
    print("1.Super car")
    print("2.Hyper car")
    choice1=int(input("Enter your choice:  "))
    if choice1 ==1:
        print("You have selected Super car")
    else:
        print("You have selected hyper car")