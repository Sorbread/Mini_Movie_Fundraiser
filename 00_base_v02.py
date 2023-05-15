# 00_base_v01.py
# The base program for 'Mini Movie Fundraiser'
# Made to buy tickets for movie


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


# Get the user age.
def get_number(text, min, max):
    while True:
        # Get age without erroring
        try:
            age = int(input(text))
        except:
            print("Please enter a whole number (e.g. 12,13,14)")

        # Check age against constraints
        if age < min:
            print(f"You must be over {MIN_AGE}")
            continue
        elif age > max:
            print(f"You must be younger than {MAX_AGE}.")
            continue
        return age


# Check string against valid responses (case-insensitive)
def string_check(inp_text, valid_responses):
    while True:
        while True:
            try:
                answer = input(inp_text)
                break
            except:
                print("Please enter a string")
        if answer in valid_responses:
            return answer
        else:
            print("Please enter valid response. ")


# Ticket prices for age categories
TICKET_PRICE = {"child": 7.50, "adult": 10.50, "senior": 6.50}
LOSS_PER_TICKET = 5


# Calculate the ticket price based on integer age
def calc_ticket_price(age):
    # Convert age to a category, e.g. 7 to 'child'
    if age < 16:
        category = "child"
    elif age < 64:
        category = "adult"
    else:
        category = "senior"
    category_to_price = TICKET_PRICE[category]

    return age, category, category_to_price


# Constant, for testing purposes set to low number (e.g. 3)
MAX_TICKETS = 3

# Minimum and maximum ages for tickets as specified by client.
MIN_AGE = 12
MAX_AGE = 120


# Amount of tickets we have sold.
tickets_sold = 0


# Main loop
while tickets_sold < MAX_TICKETS:
    # Get Name
    name = get_input("Please enter your name or 'xxx' to exit: ")

    # Program Kill Code
    if name == "xxx":
        tickets_left = MAX_TICKETS - tickets_sold
        print(
            f"You have sold {tickets_sold} ticket/s There are {tickets_left} ticket/s remaining."
        )
        break

    # Ask user if they need instructions
    want_instructions = yn("Do you want to read the instructions? (Y/N): ")
    if want_instructions == "y":
        print("instructions")

    # Get Age
    age = get_number("Please enter your age: ", MIN_AGE, MAX_AGE)

    payment_method = string_check(
        "Please enter your payment method (credit/cash): ",
        ["cr", "credit", "ca", "cash"],
    )

    # Increment Tickets Sold
    tickets_sold += 1

if tickets_sold == MAX_TICKETS:
    print("Congratulations, you have sold all the available tickets.")
