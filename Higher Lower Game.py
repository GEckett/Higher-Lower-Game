#To Do

#logo should remain on console while game is running
#while loop that continues while user guesses correctly - yes
#Random selection of first pair - yes
#A description of both people with thier Name,Job and where they live shoud appear after first pair is selected - yes
#Need to keep track of score, adding to it as correct guesses are made - yes
#On correct guesses, B=A and a new random person should be added to B
#Game should end if incorrect answer is given and show score - yes


#Imports
import os
import random
from art import logo
from art import vs
from game_data import data

#Functions
def random_A():
    pick = random.randint(0,49)
    return data[pick]

def random_B():
    pick = random.randint(0,49)
    return data[pick]

def game():
    end = False
    a = random_A()
    b = random_B()
    points = 0
    while not end:
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
        print(vs)
        print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")
        Choice = input("Who has more followers? Type 'A' or 'B':").lower()
        if Choice == "a":
            Choice = a
            if Choice['follower_count'] > b['follower_count']:
                points += 1
                b=a
                b=random_B()
                os.system('cls||clear')
            else:
                os.system('cls||clear')
                print(logo)
                print(f"Sorry that's wrong.Your final score is: {points}")
                end = True  
        elif Choice == "b":
            Choice = b
            if Choice['follower_count'] > a['follower_count']:
                points += 1
                b=a
                b=random_B()
                os.system('cls||clear')
                print(logo)
            else:
                os.system('cls||clear')
                print(logo)
                print(f"Sorry that's wrong.Your final score is: {points}")
                end = True  

#Gameplay Loop
print(logo)
while input("Do you want to play Higher Lower? y(yes) or n(no): ") == "y":
    os.system('cls||clear')
    game()