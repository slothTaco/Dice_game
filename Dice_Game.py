import random
import time

def dice():
    player = random.randint(1,6)
    print("You rolled " + str(player) )

    ai = random.randint(1,6)
    print("The computer rolls...." )
    time.sleep(2)
    print("The computer has rolled a " + str(ai) )

    if player > ai :
        print("You win")  # notice indentation
    else:
        print("You lose")

    print("Quit? Y/N")
    _continue = input() #variable

    if _continue == "Y" or _continue == "y":
        exit()
    elif _continue == "N" or _continue == "n":
        pass
    else:
        print("I did not understand that. Playing again.")

# main loop
while True:
    print("Press return to roll your die.")
    roll = input()
    dice()
