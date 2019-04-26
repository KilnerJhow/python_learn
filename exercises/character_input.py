user_name = input("Enter your name: ")
user_age = int (input("Enter your age: ")) #Get the age then convert into int

#Python print out the int as string
print("Hello {name}, the year that you'll have 100 years is {age}".format(name = user_name, age = (2019 - user_age) + 100))