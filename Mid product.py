num=int(input("Enter a number:  "))
temp=num
count=0
while temp >0:
    temp //=10
    count= count+1
print("number of digits in ",num, "are", count)
if count %2==0:
        print("you have even number count")
        mid1=count//2
        mid2=mid1+1
else:
        mid1 = count//2+1
        mid2 = mid1
temp = num    
for i in range(count, 0, -1): # outer loop for each position
     digit = temp // (10**(i-1)) # take leftmost digit
     temp = temp % (10**(i-1)) # remove extracted digit
     for j in range(mid1, mid2+1): # inner loop → check mid positions
      if i == j:
       print("Middle digit:", digit)