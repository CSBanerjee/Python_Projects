import random

class Dice:
    def __init__(self, min_value=1, max_value=6):
        self.min_value = min_value
        self.max_value = max_value

    def roll(self):
        return random.randint(self.min_value, self.max_value)

class Player:
    def __init__(self,player_id):
        self.player_id = player_id
        self.total_score = 0
    
    def take_turn(self,dice):
        print(f"\nPlayer {self.player_id}'s turn has just started!")
        print(f"Your total score is: {self.total_score}\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll !="y":
                break
            
            value = dice.roll()
            print("you rolled {value}")
            
            if value ==1:
                print("Oops! You rolled a 1. Turn over, no points added.")
                current_score = 0
                break
            else:
                current_score +=value
                print(f"Your score this turn is: {current_score}")
        self.total_score += current_score
        print(f"Your total score is now: {self.total_score}")

class Game:
    def __init__(self,max_score = 50):
        self.max_score = max_score 
        self.players = []
        self.dice = Dice()
    
    def setup_players(self):
        while True:
            players = input("Enter the number of players (2 - 5): ")
            if players.isdigit():
                players = int(players)
                if 2 <= players <= 5:
                    self.players = [Player(i + 1) for i in range(players)]
                    break
                else:
                    print("Must be between 2 - 5 players.")
            else:
                print("Invalid, try again.")

    def play(self):
        while True:
            for player in self.players:
                player.take_turn(self.dice)
                if player.total_score >= self.max_score:
                    print(
                        f"\n🏆 Player {player.player_id} is the winner "
                        f"with a score of: {player.total_score}"
                    )
                    return


if __name__ == "__main__":
    game = Game(max_score=50)
    game.setup_players()
    game.play()

    



