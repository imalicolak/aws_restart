myString = "this is a string"
print(myString)
print(type(myString))

print(myString + " is of the data type " + str(type(myString)))

firstString = "water" 
secondString = "fall" 
thirdString = firstString + secondString
print(thirdString)

name = input("What is ur name? ") 
print(name)
color = input("What's ur color?" )
animal = input("What is ur fav hobby? ")

print("{}, you like a {} {}!".format(name, color, animal))