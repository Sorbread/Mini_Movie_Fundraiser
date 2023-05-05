# yn(inp_text) - Ask a yes/no question
# Returns only 'y' or 'n' depending on user answer.
# Handles incorrect inputs by asking question again.
def yn(inp_text):
    while True:
        try:
            answer = input(inp_text).lower()

            if answer == "y" or answer == "yes":
                return "y"
            elif answer == "n" or answer == "no":
                return "n"
            else:
                raise ValueError
        except:
            print("\nPlease enter Y/N.")


# Get Input. Prevents blank inputs.
def get_input(text):
    while True:
        try:
            # Get input
            inp = input(text)
            # Strip of spaces to prevent a blank name or names such as '    '
            stripped = inp.strip()
            # Checks if input is blank after being stripped
            if stripped == "":
                raise ValueError
            return inp
        except:
            print("Please enter a non-blank value.")


# Constant, for testing purposes set to low number (e.g. 3)
MAX_TICKETS = 3


# Amount of tickets we have sold.
tickets_sold = 0


# Main loop
while tickets_sold < MAX_TICKETS:
    # Get Name
    name = get_input("Please enter your name or \'xxx\' to exit: ")

    # Program Kill Code
    if name == "xxx":
        tickets_left = MAX_TICKETS-tickets_sold
        print(
            f"You have sold {tickets_sold} ticket/s There are {tickets_left} ticket/s remaining.")
        break

    # Ask user if they need instructions
    want_instructions = yn("Do you want to read the instructions? (Y/N): ")
    if want_instructions == "y":
        print("instructions")

    # Increment Tickets Sold
    tickets_sold += 1

if tickets_sold == MAX_TICKETS:
    print("Congratulations, you have sold all the available tickets.")
