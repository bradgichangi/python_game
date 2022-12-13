from Warrior import Warrior
import random

def intro(warrior_1, warrior_2):
    print("Welcome to the Thunder Dome! First we shall choose who will start")
    starter = random.randint(0,1)
    if starter == 0:
        print(f"{warrior_1.name} you have been chosen!")
    else:
        print(f"{warrior_2.name} you have been chosen!")

def move_set (warrior_1, warrior_2):
    if(warrior_1_move == 'attack' and warrior_1_direction == 'high'):
        if(warrior_2_move == 'attack' and warrior_2_direction == 'high'):
            warrior_1.stamina -= 30
            warrior_1.health -= 10
            warrior_2.stamina -= 30
            warrior_2.health -= 10
            return warrior_1, warrior_2

        if(warrior_2_move == 'attack' and warrior_2_direction == 'low'):
            warrior_1.stamina -= 30
            warrior_1.health -= 15
            warrior_2.stamina -= 15
            warrior_2.health -= 30
            return warrior_1, warrior_2

        if(warrior_2_move == 'block' and warrior_2_direction == 'high'):
            warrior_1.stamina -= 50
            warrior_2.health += 10
            return warrior_1, warrior_2

        if(warrior_2_move == 'block' and warrior_2_direction == 'low'):
            warrior_1.stamina -= 30
            warrior_2.health -= 30
            return warrior_1, warrior_2

def fight(warrior_1, warrior_2):
    warrior_1_move = input(f"{warrior_1.name} would you like to attack or block?")
    warrior_1_direction = input(f"{warrior_1.name} would you like to {warrior_1_move} high or low?")
    warrior_2_move = input(f"{warrior_2.name} would you like to attack or block?")
    warrior_2_direction = input(f"{warrior_2.name} would you like to {warrior_2_move} high or low?")

    if((warrior_1_move == 'attack' and warrior_1_direction == 'high') and (warrior_2_move == 'attack' and warrior_2_direction == 'high')):
            warrior_1.stamina -= 30
            warrior_1.health -= 10
            warrior_2.stamina -= 30
            warrior_2.health -= 10
            return warrior_1, warrior_2
    
    elif((warrior_1_move == 'attack' and warrior_1_direction == 'low') and (warrior_2_move == 'attack' and warrior_2_direction == 'low')):
            warrior_1.stamina -= 15
            warrior_1.health -= 5
            warrior_2.stamina -= 15
            warrior_2.health -= 5
            return warrior_1, warrior_2

    elif(warrior_1_move == 'block') and (warrior_2_move == 'block'):
        print("Both warriors blocked!")
        return warrior_1, warrior_2
    
    elif((warrior_1_move == 'attack' and warrior_1_direction == 'high') and (warrior_2_move == 'attack' and warrior_2_direction == 'low')):
        warrior_1.stamina -= 30
        warrior_1.health -= 15
        warrior_2.stamina -= 15
        warrior_2.health -= 30
        return warrior_1, warrior_2
    
    elif((warrior_2_move == 'attack' and warrior_2_direction == 'high') and (warrior_1_move == 'attack' and warrior_1_direction == 'low')):
        warrior_2.stamina -= 30
        warrior_2.health -= 15
        warrior_1.stamina -= 15
        warrior_1.health -= 30
        return warrior_1, warrior_2
    
    elif((warrior_1_move == 'attack' and warrior_1_direction == 'high') and (warrior_2_move == 'block' and warrior_2_direction == 'high')):
        warrior_1.stamina -= 50
        warrior_2.stamina += 10
        return warrior_1, warrior_2
    
    elif((warrior_2_move == 'attack' and warrior_2_direction == 'high') and (warrior_1_move == 'block' and warrior_1_direction == 'low')):
        warrior_2.stamina -= 50
        warrior_1.stamina += 10
        return warrior_1, warrior_2

    

        if(warrior_2_move == 'block' and warrior_2_direction == 'high'):
            warrior_1.stamina -= 50
            warrior_2.health += 10
            return warrior_1, warrior_2

        if(warrior_2_move == 'block' and warrior_2_direction == 'low'):
            warrior_1.stamina -= 30
            warrior_2.health -= 30
            return warrior_1, warrior_2

def check_winner(warrior_1, warrior_2):
    if warrior_1.health <= 0:
        print(f"{warrior_2.name} you are the victor!")
    elif warrior_2.health <= 0:
        print(f"{warrior_1.name} you are the victor!")
    else:
        return



warrior_1 = Warrior('Bob', 'Woo')
warrior_2 = Warrior('Pat', 'Yeah')
print(f"{warrior_1.health} + {warrior_1.stamina}")
print(f"{warrior_2.health} + {warrior_2.stamina}")
fight(warrior_1, warrior_2)
print(f"{warrior_1.health} + {warrior_1.stamina}")
print(f"{warrior_2.health} + {warrior_2.stamina}")




# warrior_1_name = input("What is your name Warrior 1?")
# warrior_1_phrase = input("What is your battle cry Warrior 1?")
# warrior_2_name = input("What is your name Warrior 2?")
# warrior_2_phrase = input("What is your battle cry Warrior 2?")

# warrior_1 = Warrior(warrior_1_name, warrior_1_phrase)
# warrior_2 = Warrior(warrior_2_name, warrior_2_phrase)

# print(intro(warrior_1, warrior_2))
# print("It is now time to duel!")

