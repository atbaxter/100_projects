import random

try:
    while True:
        def dice_roll():
            rolls = int(input("How many times should I roll the dice? "))
            while rolls > 0:
                dice = random.randint(1,6)
                print(dice)
                rolls -= 1

        dice_roll()

except KeyboardInterrupt:
    pass

    
