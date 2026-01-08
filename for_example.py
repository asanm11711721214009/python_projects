'''
for a in range(10):
    print(a)
    '''
'''
for a in range(1,16):
    print(a)

for a in range(1,16,3):
    print(a)
'''
'''
n=int(input("Enter the no of student:"))
for a in range(1,n+1):
      print(f"Student-details of {a}")
      print("*"*30)
Student_id=int(input('Enter the id:'))
Student_name=(input('Enter the name:'))
m1=int(input('Enter the mark1'))
m2=int(input('Enter the mark2'))
m3=int(input('Enter the marks3'))
total=m1+m2+m3
avg=total/3
if total>270:
    grade='A'
elif total>=250:
    grade='B'
else:
    grade='C'
print(Student_id,Student_name,m1,m2,m3,total,avg,grade)

'''
'''
for a in range(1,11):
    print(a,end=" ")
print()
for b in range(20,25):
    print(b,end=" ")

'''
'''
for a in range(1,11):
    for b in range(1,11):
        print(f"{a}*{b}={a*b}",end=" ")
    print()

r=int(input('Enter the no of rows:'))
c=int(input('Enter the no of columns:'))
for a in range(1,r+1):
    for b  in range(1,c+1):
        print(f"{a}*{b}={a*b}",end=" ")
    print()
   '''
'''
for a in range(1,6):
    for b in range(1,a+1):
        print(b,end=" ")
    print()
'''
'''
for a in range(1,6):
    for b in range(1,a+1):
        print(a,end=" ")
    print()
'''
'''
for a in range(1,6):
    for b in range(1,a+1):
        print(a*b,end=" ")
    print()
'''
'''
for a in range(1,10):
    if a==5:
        for b in range(1,5):
            print('*',end=" ")
        print()
else:
    for b in range(1,5):
        if b in(1,4):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()
'''
'''
for a in range(1,10):
    if a in(1,5):
        for b in range(1,5):
            print('*',end=" ")
        print()
    elif a in(2,3,4):
        for b in range(1,5):
            if b in(1,4):
                print('*',end=" ")
            else:
                print('',end=" ")
        print()
    else:
        for b in range(1,5):
            if b==1:
                print('*',end=" ")
            else:
                print('',end=" ")
        print()
'''
'''
for a in range(1,10):
    if a in range(1,5,9):
        for b in range(1,5):
            print('*',end=" ")
        print()
    elif a in
'''
