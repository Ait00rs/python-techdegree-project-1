import random

high_score = []


# greeting message to the player
print("""
-------------------------
The Number Guessing Game!
-------------------------
    """)

# creating the personalized gaming experience
user_name = input("Enter Your Name: ")
print(("\nWelcome, {}!".format(user_name)))


def start_game():
    # generate random number from 1-10
    # random.randrange() from https://docs.python.org/2/library/random.html
    random_number = random.randrange(1, 11)
    # start counter to track player guesses
    attempts = 0
    while True:
        # prompt a player to guess the number and handle errors in user-friendly manner
        try:
            user_guess = int(input("Pick a number between 1 and 10: "))
        except ValueError:
            print("Oh no! That's not a valid value. Pick should be a number (example: 3, 6 or similar). Try again...")
        else:
            attempts += 1
            if user_guess == random_number:
                break
            elif user_guess > random_number and 11 > user_guess > 0:
                # If the guess greater than generated random number, display to the player "It's lower"
                print("It's lower!")
                continue
            elif user_guess < random_number and 11 > user_guess > 0:
                # If the guess is less than the solution, display to the player "It's higher".
                print("It's higher!")
                continue
            else:
                # Let the player know if guess is not in range (1-10)".
                print("Oh no! Your guess is not in range between 1 and 10. Try again...")
    # Adding players attempts to high_score list to track highscore
    high_score.append(attempts)
    # Once the guess is correct, stop looping, inform the user they "Got it" and show how many attempts it took them to get the correct number.
    print("\nYou got it! It took you {} tries.".format(attempts))
    # Ask player if they would like to play again.
    play_again = input("Would you like to play again? [y]es/[n]o: ")
    # Show the highscore for last game

    if play_again.lower() == "y":
        # print high score using min() method. https://www.geeksforgeeks.org/python-program-to-find-smallest-number-in-a-list/
        print("\nTHE HIGHSCORE: {}!".format(min(high_score)))
        start_game()
    else:
        print("""
----------------------------
Ending Number Guessing Game!
See you next time, {}!
----------------------------
            """.format(user_name))


start_game()
