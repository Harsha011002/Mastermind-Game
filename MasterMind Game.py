#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random

# the .randrange() function generates
# a random number within the specified range.
k=int(input("--Select the Difficulty Level--\n1 -> One digits   [BEGINNER]\n2 -> Two digits   [EASY]\n3 -> Three digits [INTERMEDIATE]\n4 -> Four digits  [CHALLENGING]\n54321 -> To Exit [Don't try this.Crack it !!] \n"))
if k==1:
    num = random.randrange(0, 10)
    n = int(input("Guess the 1 digit number:"))
elif k==2:
    num = random.randrange(10, 100)
    n = int(input("Guess the 2 digit number:"))
elif k==3:
    num = random.randrange(100, 1000)
    n = int(input("Guess the 3 digit number:"))
elif k==4:
    num = random.randrange(1000, 10000)
    n = int(input("Guess the 4 digit number:"))
else:
    print("\n\nx-x-INVALID SELECTED-x-x\n\n-x-x-x-GAME OVER-x-x-x-")

# condition to test equality of the
# guess made. Program terminates if true.
if(n == num):
	print("Great! You guessed the number in just 1 try! You're a Mastermind!")
else:
	# ctr variable initialized. It will keep count of
	# the number of tries the Player takes to guess the number.
    ctr = 0

	# while loop repeats as long as the Player
	# fails to guess the number correctly.
    while n != num and n!=54321:
		# variable increments every time the loop
		# is executed, giving an idea of how many
		# guesses were made.
        ctr += 1

        count = 0

		# explicit type conversion of an integer to
		# a string in order to ease extraction of digits
        n = str(n)

		# explicit type conversion of a string to an integer
        num = str(num)

		# correct[] list stores digits which are correct
        correct = []

		# for loop runs 4 times since the number has 4 digits.
        for i in range(0, 4):
			# checking for equality of digits
            if(n[i] == num[i]):
				# number of digits guessed correctly increments
                count += 1
				# hence, the digit is stored in correct[].
                correct.append(n[i])
            else:
                continue

		# when not all the digits are guessed correctly.
        if (count < 4) and (count != 0):
            print("Not quite the number. But you did get ",
                count, " digit(s) correct!")
            print("Also these numbers in your input were correct.")

            for k in correct:
                print(k, end=' ')

            print('\n')
            print('\n')
            n = int(input("Enter your next choice of numbers: "))

		# when none of the digits are guessed correctly.
        elif(count == 0):
            print("None of the numbers in your input match.")
            n = int(input("Enter your next choice of numbers: "))

    if n == num:
        print("You've become a Mastermind!")
        print("It took you only", ctr, "tries.")
    elif n==54321:
        print("You were close buddy! Try lower levels.")


# In[ ]:


###### import random

def get_secret_number(num_digits):
    """Generate a random secret number with the given number of digits."""
    return random.sample(range(10), num_digits)

def get_user_guess(num_digits):
    """Get the user's guess for the secret number."""
    while True:
        try:
            guess = int(input(f"Enter your {num_digits}-digit guess: "))
            if len(str(guess)) == num_digits:
                return [int(digit) for digit in str(guess)]
            print(f"Please enter a {num_digits}-digit number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_matching_digits(secret_number, guess):
    """Find the matching digits between the secret number and the guess."""
    return [digit for digit in guess if digit in secret_number]

def play_game():
    print("Welcome to the Mastermind game!")
    difficulty = int(input("Enter the difficulty level (1, 2, 3, or 4): "))

    # Generate the secret number for Player 1
    secret_number_p1 = get_secret_number(difficulty)
    print("Player 1 has set the secret number.")

    # Player 2's turn to guess the secret number
    attempts_p2 = 0
    while True:
        attempts_p2 += 1
        guess_p2 = get_user_guess(difficulty)

        if guess_p2 == secret_number_p1:
            print(f"Congratulations! Player 2 is the Mastermind! You guessed the number in {attempts_p2} attempts.")
            break

        matching_digits = get_matching_digits(secret_number_p1, guess_p2)
        print(f"Hints: {len(matching_digits)} digit(s) are correct: {matching_digits}")

    # Player 2 failed to guess, now Player 2 sets the secret number for Player 1
    secret_number_p2 = get_secret_number(difficulty)
    print("Player 2's turn. Set the secret number for Player 1.")

    # Player 1's turn to guess the secret number
    attempts_p1 = 0
    while True:
        attempts_p1 += 1
        guess_p1 = get_user_guess(difficulty)

        if guess_p1 == secret_number_p2:
            print(f"Congratulations! Player 1 is the Mastermind! You guessed the number in {attempts_p1} attempts.")
            break

        matching_digits = get_matching_digits(secret_number_p2, guess_p1)
        print(f"Hints: {len(matching_digits)} digit(s) are correct: {matching_digits}")

    # Determine the winner
    if attempts_p1 < attempts_p2:
        print("Player 1 wins!")
    elif attempts_p1 > attempts_p2:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()


# In[ ]:




