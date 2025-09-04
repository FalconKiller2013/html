medical_cause=input("Do you have any medical cause Yes or No:  ")
attendance=int(input("Enter your attendance:  "))
if medical_cause=="Y":
    print("You are eligile to write the exam")
else:
    if attendance>75:
        print("You are eligile to write the exam")
    else:
        print("Not eligile to write the exam")