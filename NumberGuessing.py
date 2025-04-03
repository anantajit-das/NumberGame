import random
print("Welcome to number guessing game.\n You will have 8 chances.")

number_to_be_guessed = random.randrange(100)

chances=8

guess_counter=0

while guess_counter < chances:
    guess_counter+=1
    my_guess=int(input("Enter your guess: "))
    
    if my_guess==number_to_be_guessed:
        print("This number is {number_to_be_guessed} and you found it right !! in the {guess_counter} attempt")

        break
    elif guess_counter>=chances and my_guess != number_to_be_guessed:
        print("Oops sorry, The number is {number_to_be_guessed} better lick next time ")

    elif my_guess > number_to_be_guessed:
        print('Your guess is higher ')

    elif my_guess < number_to_be_guessed:
        print('Your guess is lesser')

