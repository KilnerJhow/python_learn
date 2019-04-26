import random #Needed for generate random number

a = range(random.randint(2, 40), random.randint(2, 100))
b = range(1, random.randint(2, 10))

print ("A {list}".format(list = a))
print "B: {list}".format(list = b)

commom = []

for x in a:

    #Check if a number is the list
    if x in b:
        commom.append(x)

# print commom

print (set (a) & set (b))