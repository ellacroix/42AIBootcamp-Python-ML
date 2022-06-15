from random import randint

def print_menu():
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!")

def game():
    answer = randint(1, 99)
    tries = 0
    while True:
        print_menu()
        print("")
        while True:
            try:
                number = input("What's your guess between 1 and 99?\n")
                if number == "exit":
                    exit()
                number = int(number)
            except ValueError:
                print("Not a valid answer!\n")
                continue
            if int(number) > answer:
                print("Too high!\n")
                tries += 1
            elif int(number) < answer:
                print("Too low!\n")
                tries += 1
            else:
                print("Congratulations, you've got it!")
                print("You won in", tries, "attempts")
                exit()

game()