even_odd = int(input ("Enter a number: "))

#if needs the ':' to work
if ((even_odd % 2) == 0):
    print("The number {number} is even".format(number = even_odd))
else:
    print("The number {number} is odd".format(number = even_odd))