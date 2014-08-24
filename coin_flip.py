import random


try:
    while True:
        

        def coin_flip():
            flips = int(input("How many times should we flip a coin? "))
            while flips > 0:
                
                outcome = random.randint(0,1)
                if outcome == 0:
                    print ("Heads")
                else:
                    print ("Tails")
                flips -= 1

        coin_flip()

except KeyboardInterrupt:
    pass
