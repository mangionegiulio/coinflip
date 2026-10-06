from random import randint
from time import time

while True:
    counter = 0
    tries = 0
    prec = None
    Interrupt = False
    percent = False

    target = int(input("Insert a number (times you want the same face consecutively): "))
    statistical_probability = (1 / (2 ** (target - 1))) * 100

    start = time()

    while counter != target:
        if tries > 10000000 or (time() - start) > 60:
            print("You passed 10.000.000 tries, or 1 minute has passed")
            Interrupt = True
            break

        lancio = randint(1, 2)

        if lancio == prec:
            counter += 1
        elif prec is None:
            prec = lancio
            counter += 1
        else:
            prec = lancio
            counter = 1
            
        tries += 1

    stop = time()
    total_time = stop - start

    if not Interrupt:
        percent = (target / tries) * 100
        print(f"Tries: {tries} in {total_time} seconds.")
        print(f"Actual percentage: {percent}%, Statistical probability: {statistical_probability}%")
    else:
        print(f"Search interrupted after {total_time} seconds.")

    play_again = input("Want to play again? (y/n): ").lower()
    if play_again != 'y':
        break