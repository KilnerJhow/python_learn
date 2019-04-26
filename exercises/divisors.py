x = int(input("Enter a number :"))

y = range(1,x) #Creates a list from 1 to x

dividers = []

for z in y:
    if (x % z) == 0:
        dividers.append(z)

print dividers