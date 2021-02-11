# I am going to first list out all my variables and assign them values

hidden_number = 5

users_guess = int(input("Pls Enter A Value: "))

number_of_guesses = 1

times_guessed = 4

no_more_guess = False

# I am using a while loop so that im able to give my code more detailed instructions

while users_guess != hidden_number and not(no_more_guess):
    
    if number_of_guesses < times_guessed:
        users_guess = input("Pls Try Again: ")
        number_of_guesses += 1 
    
    else:
        no_more_guess = True

#I created an if loop outside of my wile loop so that when all the conditions inside my loop has been met it can print the results

if no_more_guess:
    print("No More Guesses , You Lose!")

else:
    print("Weldone You Guessed Correct In ", number_of_guesses, " Tries")   

