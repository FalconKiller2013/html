lower_limit=int(input("Enter lower limit:  "))
upper_limit=int(input("Enter upper limit:  "))
print("Prime numbers between ", lower_limit,"and",upper_limit,"are: ")
for num in range(lower_limit, upper_limit+1):
  if num>1:
    for i in range(2, num):
     if (num%i)==0:
      break
    else:
      print(num)