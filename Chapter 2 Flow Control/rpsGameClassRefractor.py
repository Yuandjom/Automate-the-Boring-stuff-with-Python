import random , sys
print("ROCK , PAPER , SCISSORS")
#These variables keep track of the number of wins ,losses and ties.
class RPSGame:
    def __init__(self,wins = 0 , losses =0 , ties=0):
        #initialize the settings
        self.wins = wins
        self.losses = losses
        self.ties = ties
        
    
    def run_game(self):
        #start the main loop for game
        while True:
            print("%s Wins, %s Losses, %s Ties" % (self.wins , self.losses , self.ties))
            print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit ")
            self.player_Movement()
            self.display_player_Movement()
            self.computer_Movement()
            self.Display_Records()
    
    def player_Movement(self):
        while True:
            print('Type one of r , p , s or q ')
            self.playerMove = input()
            if self.playerMove == 'q':
                sys.exit() #quit the program
            elif self.playerMove == 'r' or self.playerMove == 'p' or self.playerMove == 's':
                break #break out of the player input loop.
    
    def display_player_Movement(self):
        #Display what the player chose:
        if self.playerMove == 'r':
            print("Rock versus...")
        elif self.playerMove == 'p':
            print('PAPER versus...')
        elif self.playerMove == 's':
            print('SCISSORS versus...')        
    
    def computer_Movement(self):
        #Display what the computer chose:
        self.randomNumber = random.randint(1,3)
        if self.randomNumber == 1 :
            self.computerMove = 'r'
            print("ROCK")
        elif self.randomNumber == 2:
            self.computerMove = 'p'
            print("PAPER")
        elif self.randomNumber == 3:
            self.computerMove = 's'
            print("SCISSORS")
    def Display_Records(self):

        #Display and record the win/loss/tie:
        if self.playerMove == self.computerMove:
            print('It is a tie!')
            self.ties = self.ties + 1 
        elif self.playerMove == 'r' and self.computerMove =='s':
            print("You win!")
            self.wins  = self.wins + 1
        elif self.playerMove == 'p' and self.computerMove =='r':
            print("You win!")
            self.wins = self.wins + 1        
        elif self.playerMove == 's' and self.computerMove =='p':
            print("You win!")
            self.wins = self.wins + 1
        elif self.playerMove == 'r' and self.computerMove =='p':
            print("You lose!")
            self.losses = self.losses + 1
        elif self.playerMove == 'p' and self.computerMove =='s':
            print("You lose!")
            self.losses = self.losses + 1           
        elif self.playerMove == 's' and self.computerMove =='r':
            print("You lose!")
            self.losses = self.losses + 1        

if __name__ == "__main__":
    RPSgame = RPSGame()
    RPSgame.run_game()


     