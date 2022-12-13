from Warrior import Warrior
import random
import time

def suffix ():
    names = ['The Slayer', 'The Great', 'The Chosen One', 'The Mighty', 'The Forgetful', 'The Fierce', 'The Clinically Insane', 'The Insurance Salesman', 'The Average', 'The Strange', 'The Science Guy']
    return names[random.randint(0, len(names)-1)]

def intro(warrior_1, warrior_2):
    print("\n\n\n--------------------WELCOME TO THE THUNDERDOME!-------------------- \n\n\n\n\n")
    print("MEET OUR WARRIORS!")
    time.sleep(2)

    print((warrior_1.name + " " + suffix()).upper())
    time.sleep(2)

    print((warrior_2.name + " " + suffix()).upper())
    time.sleep(2)

    starter = random.randint(0,1)
    print("A coin is being flipped to see who starts...")
    time.sleep(2)

    if starter == 0:
        print(f"{warrior_1.name} you have been chosen to start!")
        return [warrior_1, warrior_2]
    else:
        print(f"{warrior_2.name} you have been chosen to start!")
        return [warrior_2, warrior_1]


def stamina_increase(warrior):
    if(warrior.stamina < 90):
        print(f"{warrior.name} readies themself and gains 10 stamina!")
        warrior.stamina += 10

def fight(warrior_1, warrior_2):
    warrior_1_move = ""
    warrior_2_move = ""
    warrior_1_direction = ""
    warrior_2_direction = ""

    # while (warrior_1_move == 'attack' and warrior_1.stamina < 15) or warrior_1_move != 'block' or warrior_1_move != 'attack' :
    while warrior_1_move != 'attack' and warrior_1_move != 'block':
        warrior_1_move = input(f"{warrior_1.name} would you like to attack or block?")

        while warrior_1.stamina < 15 and warrior_1_move == "attack":
            warrior_1_move = input(f"{warrior_1.name} would you like to attack or block?")
            print("Your stamina may be too low to execute this move")

    while warrior_1_direction != 'high' or warrior_1_direction != 'low':
        
        warrior_1_direction = input(f"{warrior_1.name} would you like to {warrior_1_move} high or low?")
        # if warrior_1_move == "attack" and warrior_1_direction == "high":
        #     print("Your stamina is too low, consider attacking")

    while warrior_2_move != 'attack' and warrior_2_move != 'block':
        warrior_2_move = input(f"{warrior_2.name} would you like to attack or block?")

        while warrior_2.stamina < 15 and warrior_2_move == "attack":
            warrior_2_move = input(f"{warrior_2.name} would you like to attack or block?")
            print("Your stamina may be too low to execute this move")

    while warrior_2_direction != 'high' or warrior_2_direction != 'low':
        if warrior_2.stamina < 30 and warrior_2_move == "attack":
            warrior_2_direction = "low"
        warrior_2_direction = input(f"{warrior_2.name} would you like to {warrior_2_move} high or low?")

    if((warrior_1_move == 'attack' and warrior_1_direction == 'high') and (warrior_2_move == 'attack' and warrior_2_direction == 'high')):
        warrior_1.stamina -= 30
        warrior_1.health -= 10
        warrior_2.stamina -= 30
        warrior_2.health -= 10

    elif((warrior_1_move == 'attack' and warrior_1_direction == 'low') and (warrior_2_move == 'attack' and warrior_2_direction == 'low')):
        warrior_1.stamina -= 15
        warrior_1.health -= 5
        warrior_2.stamina -= 15
        warrior_2.health -= 5

    elif(warrior_1_move == 'block') and (warrior_2_move == 'block'):
        print("Both warriors blocked!")
    
    elif((warrior_1_move == 'attack' and warrior_1_direction == 'high') and (warrior_2_move == 'attack' and warrior_2_direction == 'low')):
        warrior_1.stamina -= 30
        warrior_1.health -= 15
        warrior_2.stamina -= 15
        warrior_2.health -= 30
    
    elif((warrior_2_move == 'attack' and warrior_2_direction == 'high') and (warrior_1_move == 'attack' and warrior_1_direction == 'low')):
        warrior_2.stamina -= 30
        warrior_2.health -= 15
        warrior_1.stamina -= 15
        warrior_1.health -= 30
    
    elif((warrior_1_move == 'attack' and warrior_1_direction == 'high') and (warrior_2_move == 'block' and warrior_2_direction == 'high')):
        warrior_1.stamina -= 50
        warrior_2.stamina += 10 if warrior_2.stamina < 90 else 0
    
    elif((warrior_2_move == 'attack' and warrior_2_direction == 'high') and (warrior_1_move == 'block' and warrior_1_direction == 'high')):
        warrior_2.stamina -= 50
        warrior_1.stamina += 10 if warrior_1.stamina < 90 else 0

    elif((warrior_1_move == 'attack' and warrior_1_direction == 'high') and (warrior_2_move == 'block' and warrior_2_direction == 'low')):
        warrior_1.stamina -= 30
        warrior_2.health -= 30
    
    elif((warrior_2_move == 'attack' and warrior_2_direction == 'high') and (warrior_1_move == 'block' and warrior_1_direction == 'low')):
        warrior_2.stamina -= 30
        warrior_1.health -= 30

    elif((warrior_1_move == 'attack' and warrior_1_direction == 'low') and (warrior_2_move == 'block' and warrior_2_direction == 'high')):
        warrior_1.stamina -= 15
        warrior_2.health -= 15
    
    elif((warrior_2_move == 'attack' and warrior_2_direction == 'low') and (warrior_1_move == 'block' and warrior_1_direction == 'high')):
        warrior_2.stamina -= 15
        warrior_1.health -= 15
    
    elif((warrior_1_move == 'attack' and warrior_1_direction == 'low') and (warrior_2_move == 'block' and warrior_2_direction == 'low')):
        warrior_1.stamina -= 15
        warrior_2.stamina += 10 if warrior_2.stamina < 90 else 0
    
    elif((warrior_2_move == 'attack' and warrior_2_direction == 'low') and (warrior_1_move == 'block' and warrior_1_direction == 'low')):
        warrior_2.stamina -= 15
        warrior_1.stamina += 10 if warrior_1.stamina < 90 else 0
    
    print(f"{warrior_1.name} {warrior_1_move}s {warrior_1_direction} and {warrior_2.name} {warrior_2_move}s {warrior_2_direction}")

    check_winner(warrior_1, warrior_2)

    stamina_increase(warrior_1)
    stamina_increase(warrior_2)

    return warrior_1, warrior_2

    


def check_winner(warrior_1, warrior_2):
    if warrior_1.health <= 0:
        print(f"{warrior_2.name} you are the victor!")
        print(f"{warrior_2.name} screams {warrior_2.phrase}!")
        exit()
    elif warrior_2.health <= 0:
        print(f"{warrior_1.name} you are the victor!")
        print(f"{warrior_1.name} screams {warrior_1.phrase}!")

        exit()
    else:
        print(f"{warrior_1.name} Health: {warrior_1.health} Stamina: {warrior_1.stamina}")
        print(f"{warrior_2.name} Health: {warrior_2.health} Stamina: {warrior_2.stamina}")


warrior_1_name = ""
warrior_2_name = ""
warrior_1_phrase = ""
warrior_2_phrase = ""

while warrior_1_name == "":
    warrior_1_name = input("What is your name Warrior 1?")

while warrior_1_phrase == "":
    warrior_1_phrase = input("What is your battle cry Warrior 1?")

while warrior_2_name == "":
    warrior_2_name = input("What is your name Warrior 2?")

while warrior_2_phrase == "":
    warrior_2_phrase = input("What is your battle cry Warrior 2?")

warrior_1 = Warrior(warrior_1_name, warrior_1_phrase)
warrior_2 = Warrior(warrior_2_name, warrior_2_phrase)

fight_order = intro(warrior_1, warrior_2)

while True:
    fight(fight_order[0], fight_order[1])

