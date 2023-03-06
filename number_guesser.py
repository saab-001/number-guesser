import random

logo = """
                                                          $$\     $$\                                                         $$\                           
                                                          $$ |    $$ |                                                        $$ |                          
 $$$$$$\  $$\   $$\  $$$$$$\   $$$$$$$\  $$$$$$$\       $$$$$$\   $$$$$$$\   $$$$$$\        $$$$$$$\  $$\   $$\ $$$$$$\$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  
$$  __$$\ $$ |  $$ |$$  __$$\ $$  _____|$$  _____|      \_$$  _|  $$  __$$\ $$  __$$\       $$  __$$\ $$ |  $$ |$$  _$$  _$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$ /  $$ |$$ |  $$ |$$$$$$$$ |\$$$$$$\  \$$$$$$\          $$ |    $$ |  $$ |$$$$$$$$ |      $$ |  $$ |$$ |  $$ |$$ / $$ / $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |  $$ |$$ |  $$ |$$   ____| \____$$\  \____$$\         $$ |$$\ $$ |  $$ |$$   ____|      $$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$   ____|$$ |      
\$$$$$$$ |\$$$$$$  |\$$$$$$$\ $$$$$$$  |$$$$$$$  |        \$$$$  |$$ |  $$ |\$$$$$$$\       $$ |  $$ |\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |\$$$$$$$\ $$ |      
 \____$$ | \______/  \_______|\_______/ \_______/          \____/ \__|  \__| \_______|      \__|  \__| \______/ \__| \__| \__|\_______/  \_______|\__|      
$$\   $$ |                                                                                                                                                  
\$$$$$$  |                                                                                                                                                  
 \______/                                                                                                                                                   

"""
print(logo)
print("\nWelcome to the Number Guessing Game\nYou have to guess a number from '1' to '100'")


def num_generator():
    numbers = list(range(1,101))
    num_select = random.choice(numbers)
    return num_select


def guess_check(num,guess):

    if num == guess:
        print("\nyou win!")
        return True
    
    elif num < guess:
        print("too high\n")
        return False
    
    elif num > guess:
        print("too low\n")
        return False


def diff_level():

    diff = input("Choose the difficulty. Type 'easy' or 'hard': ").lower()
    
    if diff == "easy":
        return 10
    
    elif diff == "hard":
        return 5
    
    else:
        print("\nInvalid input!\n")
        return diff_level()


def guess_asker():
    
    print("You have "+ str(chances) +" remaining to guess the number.")
    guess = input("Make a guess: ")
    input_check = guess.isnumeric()
    
    if input_check:
        return int(guess)
    
    else:
        print("\nInvalid input!\n")
        return guess_asker()

chances = diff_level()
num = num_generator()
gameover = False

while not gameover :

    guess = guess_asker()
    gameover = guess_check(num,guess)
    chances -= 1

    if chances == 0:
        gameover = True
        print("\nYou Lose!")