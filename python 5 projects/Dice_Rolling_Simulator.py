"""concept of random
#random float number
import random
random_float =random.random()
print(random_float)
random_integer =random.randint(1,6)
print(random_integer)

myList=["cherry","berry","grapes","strawberry"]
random_choice=random.choice(myList)
print(random_choice)
"""
import random
print("Hey welcome to Dice Rolling")

random_number=random.randint(1,6)
print(random_number)
while True:
    roll_again=input("Hey buddy!Do you want to roll again!! ")
    if roll_again == "yes":
        print(random.randint(1,6))
    else:
        print("Thank you for playing!! ")
        exit()
