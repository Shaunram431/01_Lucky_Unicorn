import random


# Functions go here
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("please answer")
    print()

def instruction():
    print()
    print("****How to Play****")
    print()
    print("The rules of the game go here")
    print()
    print("Choose a starting amount  (minimum $1, maximum $10)")
    print("Then press <enter> to play. You will get either a house, a zebra, a donkey or a unicorn")
    print()
    print("ti costs a $1 per round. Depending on your prize you might win some of the money back. Here's the payout"
          "a ")
    print()
    return ""


# Functions go here
def num_check(question, low, high):
    error = "Please enter an whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is too low / too high give
            if low < response <= high:
                return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)


# for decorating statements
def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main Routine goes here...
print("*** Welcome To The Lucky Unicorn Game ***")
played_before = yes_no("Have you played the game before?")

if played_before == "no":
    instruction()

print()
# Ask user how much they want to play with...
how_much = num_check("How much would you like to play with? ", 0, 10)

print("You will be spending ${}".format(how_much))

balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()

while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # Print round number
    print()
    print("*** Rounds #{} ***".format(rounds_played))

    chosen_num = random.randint(1, 100)

    # Adjust balance
    # If the random # is between 1 and 5,
    # user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        decoration = "*"
        balance += 4

    # if the random # is between 6 and 36
    # user gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        decoration = "D"
        balance -= 1
    # if the number is even, set the chosen
    # item to a horse
    else:
        if chosen_num % 2 == 0:
            chosen = "horse"
            decoration = "H"

        # otherwise set it to a zebra
        else:
            chosen = "zebra"
            decoration = "Z"
        balance -= 0.5

    feedback = "You got a {}. Your balance is ${:.2f}".format(chosen, balance)
    statement_generator(feedback, decoration)

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:

        play_again = input("Press Enter to play again or 'xxx' to quit")

print()
final_balance = "Final balance ${:.2f}".format(balance)
statement_generator(final_balance, "-")
