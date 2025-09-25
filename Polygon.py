import turtle
num_of_sides=int(input("Enter number of sides:  "))
screen=turtle.Screen()
turtle.Screen().bgcolor("light blue")
screen.setup(500,500)

for i in range(num_of_sides):
    turtle.forward(100)
    turtle.right(360/num_of_sides)
turtle.done()