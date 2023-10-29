"""
CONDITIONALS
"""

userReply = input("Do you need to ship a package? (Enter Yes or No) ")
userReply = userReply.lower()

if userReply == "yes":
    print("We can help you ship that package!")
elif userReply == "envelope":
    print("Why you enter envelope. It's Yes or No")
elif userReply == "copies":
    copies = input("How many copies would you like? (NUMBER) ")
    print('Here are {} copies.'.format(copies))
else:
    print("Please come back when you need to ship da package!!!")