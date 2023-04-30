# functions go here

# yn(inp_text) - Ask a yn question
# Returns only 'y' or 'n' depending on user answer.
# Handles incorrect inputs by asking question again.
def yn(inp_text):
    while True:
        answer = input(inp_text).lower()

        if answer == "y" or answer == "yes":
            return "y"
        elif answer == "n" or answer == "no":
            return "n"
        else:
            print("Please enter Y/N")


# main routine goes here
want_instructions = yn("Do you want to read the instructions? (Y/N): ")
if want_instructions == "y":
    print("instructions")
