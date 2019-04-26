#Integer division round down for both positive and negative numbers

# Ex: 5 // 3 = 1     5.0//3.0 = 1

#Exponentiation x ** y = x ^ y
# Ex 5 ** 2 = 25


# the word "is" is reserved to check if two variables refer to same object
# == check if two objects have same value
#Ex

a = [1,2,3,4]
b = a
b is a          #True, because b point to a
b == a          #True, becausa a and b have same values
b = [1,2,3,4]
b is a          #False, a and b are separated objects
b == a          #True, a and b have same values


#You can interpolate strings like
"{} can be {}".format("Strings", "Interpolated") #Results in "Strings can be Interpolated"

#You can repeat some arguments putting a name on the brackets or numbers

"{0} beatiful {1}, {0} wonderful {1}".format("Hello", "Wolrd") #Results in "Hello Beatiful World, Hello Wonderful World"
#or
"{arg1} beatiful {arg2}, {arg1} wonderful {arg2}".format(arg1 = "Hello", arg2 = "World")

#but the strings format runs only in python 3, if need to run on python 2.5 or lower use
"%s can be %s the %s way" % ("Strings", "interpolated", "old") 

#get input data from console

input_string_var = input("Enter some data: ")

#convention for variables is use lower cases with underscore