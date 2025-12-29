age=int(input("Enter the age:"))
print("vote"if age>=18 else "no-vote")

no=int(input("Enter the no:"))
print("less than zero" if no<0 else "0" if no==0 else "+ve")