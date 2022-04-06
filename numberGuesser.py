import random

numbers = [1, 2, 3, 4, 5]

while True:
    randomNumber = random.choice(numbers)
    userInput = input("Guess a number 1-5: ")
    userNumber = int(userInput)
    if userNumber >= 6:
        print("Number is too large!\n")
    if userNumber <=0:
        print("Number is too small!\n")
    if 1 <= userNumber <= 5:
        print(f"You chose number {userNumber}.")
        print(f"Computer chose number {randomNumber}")

        if userNumber == randomNumber:
            print("Congrats, you guessed the correct number!\n")
        else:
            print("You guessed wrong!\n")