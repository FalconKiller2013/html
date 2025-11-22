weather=(1,0,0,0,1,0,0)
sunny=0
Rainy=0
for i in range(0,7):
    if (weather[i]==0):
        Rainy+=1
    else:
        sunny+=1 
if(sunny<Rainy):
    print("Good weather")
else:
    print("Bad weather")
