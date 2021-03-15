# Ask the user if they have played before
show_instructions = input("Have you played this game before? ").lower()

# If they say yes, output 'display instructions'
if show_instructions == "yes":
    print ("program continues")

elif show_instructions == "y":
    print("program continues")

elif show_instructions == "no":
    print("display instructions")

elif show_instructions == "n":
    print("display instructions")

# If they say no,output 'display instructions'
else:
    print("PLease answer yes / no")

