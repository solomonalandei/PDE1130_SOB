import random

def compare_numbers(number, user_guess):
    ## make a list of digits for both arguments
    number = [digit for digit in number]
    user_guess = [digit for digit in user_guess]

    cowbull = [0,0]
    for digit in user_guess:
        if digit in number:
            index_in_userguess = user_guess.index(digit)
            index_in_number = number.index(digit)
            #mask out the number
            number[index_in_number] = 'x'
            if index_in_number == index_in_userguess:
                cowbull[1] += 1
            else:
                cowbull[0] += 1
        
        else:
            # using x to replace the digits we covered
            index = user_guess.index(digit)
            user_guess[index] = 'x'
    return cowbull

playing = True #gotta play the game
number = str(random.randint(0,9999)) #random 4 digit number
guesses = 0
print(number)

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!")
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + "! The number was "+str(number))
    else:
        print("Your guess isn't quite right, try again.")
