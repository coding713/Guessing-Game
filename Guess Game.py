import random

def guessing_game():
    while True:
        confirm = input("Do you want to play the guessing game? Type Start \n")
        if confirm.upper() == 'START':
            while True:
                scope = list(range(1,101))
                guess_num = random.choice(scope)
                user_guess = 0
                print("Rules: Guess a number between 1 and 100")
                print(" Within 2 you are on lava\n Within 5 you'll be very hot\n Within 10 you'll be hot\n Within 20 you'll be warm\n Within 30 you are cold\n Within 50 you are very cold")
                print(" After that you are freezing")
                while(guess_num!=user_guess):
                    user_guess = input("Guess a number between 1 to 100? ")
                    if user_guess.isdigit() and 1<=int(user_guess)<101:   
                        user_guess = int(user_guess)
                        if guess_num == user_guess: 
                            break 
                        elif (-2<=(guess_num - user_guess)<=2):
                            print("You are on lava")        
                        elif (-5<=(guess_num - user_guess)<=5):
                            print("You are very hot")
                        elif (-10<=(guess_num - user_guess)<=10):
                            print("You are hot")
                        elif (-20<=(guess_num - user_guess)<=20):
                            print("You are warm")
                        elif (-30<=(guess_num - user_guess)<=30):
                            print("You are cold")
                        elif (-50<=(guess_num - user_guess)<=50):
                            print("You are very cold")
                        else:
                            print("You are freezing")
                    else: 
                        print("Please enter a number between 1 and 100")
                print('You guessed correctly!')
                break
        else:
            break
guessing_game()