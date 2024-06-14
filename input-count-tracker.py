#log attempt limiter condition
import os
import time

username = ["push", "pull", "bench", "squat", "press", "cardio"]
attempt = 0
max_attempt = 4
#name = input("enter your username: ")
while attempt < max_attempt:
    name = input("enter your username: ")
    attempt += 1
    # check first if the name entered  is in username list
    if name in username:
        os.system('cls')
        print(f"Welcome {name}!")
        break
    # repeated loop condition within elif to clear terminal
    elif attempt < max_attempt:
        time.sleep(0.5)
        os.system('cls')
        print(f"{name} is not register! \nTry again!")
        continue
if attempt == max_attempt:
    os.system('cls')
    print("You have exausted the number trials! \nreset account or create a new account!")
