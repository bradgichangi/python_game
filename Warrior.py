class Warrior:
    def __init__(self, name, phrase):
        self.name = name
        self.phrase = phrase
        self.health = 100
        self.stamina = 100

    def attack(self, direction, opponent, opponent_move, opponent_direction):

        if direction == 'high':
            self.stamina -= 30
            if opponent_move == 'block' and opponent_direction == 'high':
                self.stamina -= 20
                opponent.stamina += 10 if opponent.stamina < 90 else 0

            elif opponent_move == 'attack' and opponent_direction == 'high':
                self.health -= 10
                opponent.stamina -= 30
                opponent.health -= 10

            elif opponent_move == 'attack' and opponent_direction == 'low':
                self.health -= 15
                opponent.stamina -= 15
                opponent.health -= 30

            else:
                opponent.health -= 30

        elif direction == 'low':
            self.stamina -= 15
            if opponent_move == 'block' and opponent_direction == 'high':
                opponent.health -= 15

            elif opponent_move == 'attack' and opponent_direction == 'high':
                self.health -= 30
                opponent.stamina -= 30
                opponent.health -= 15

            elif opponent_move == 'attack' and opponent_direction == 'low':
                self.health -= 5
                opponent.stamina -= 15
                opponent.health -= 5

            else:
                opponent.stamina += 10 if opponent.stamina < 90 else 0

        return opponent

    def block(self, direction, opponent, opponent_move, opponent_direction):

        if opponent_move == 'block':
            return opponent
        
        if direction == 'high':

            if opponent_move == 'attack' and opponent_direction == 'high':
                opponent.stamina -= 50

            else:
                self.health -= 15
                opponent.stamina -= 15


        elif direction == 'low':
            
            if opponent_move == 'attack' and opponent_direction == 'high':
                self.health -= 30
                opponent.stamina -= 30

            else:
                self.stamina += 10 if self.stamina < 90 else 0
                opponent.stamina -= 15

        return opponent