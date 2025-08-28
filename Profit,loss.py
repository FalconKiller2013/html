Selling_price=int(input("enter the amount: "))
cost_price=int(input("Enter th amount: "))
Profit=Selling_price-cost_price
loss=cost_price-Selling_price
if Selling_price>cost_price:
    print(" :) You earned a profit of ",Profit)
else:
    print(" :( You had a loss of ",loss)