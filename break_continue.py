l=[1,2,9,10,-4,18,91,92]
print(l)
print(l[3])
print(l[6])
print(l[-4])
print(len(l))

for a in range(len(l)):
    print(a,l[a])

for a in range(len(l)):
    if l[a]<0:
        break
    else:
        print(a,l[a])

for a in range(len(l)):
    if l[a]<0:
        continue
    else:
        print(a,l[a])