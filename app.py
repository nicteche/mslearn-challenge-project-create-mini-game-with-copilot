# write 'hello world' to the console
print('hello world')
#Make a py game of Rock, Sicssors, Paper
#Rock beats Scissors
#Scissors beats Paper
#Paper beats Rock
#If both players choose the same, it's a tie
#The computer should randomly select a move
#The user should be able to input their move
#the game dont admit wrong inputs
#In the final, the game should show the winner and ask if the user wants to play again
#show the score of the user
#Any answer is lower case
import random
def game():
    print('Welcome to Rock, Paper, Scissors')
    score = 0
    while True:
        user = input('Choose Rock, Paper or Scissors: ').lower()
        if user not in ['rock', 'paper', 'scissors']:
            print('Invalid input')
            continue
        computer = random.choice(['rock', 'paper', 'scissors'])
        print(f'Computer chose {computer}')
        if user == computer:
            print('It\'s a tie')
        elif user == 'rock' and computer == 'scissors':
            print('You win')
            score += 1
        elif user == 'scissors' and computer == 'paper':
            print('You win')
            score += 1
        elif user == 'paper' and computer == 'rock':
            print('You win')
            score += 1
        else:
            print('You lose')
        print(f'Score: {score}')
        play_again = input('Do you want to play again? (yes/no): ')
        if play_again != 'yes':
            break
game()  # Call the function to start the game