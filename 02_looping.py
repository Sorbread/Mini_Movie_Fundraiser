# Looping Component

# Constant, for testing purposes set to low number (e.g. 3)
MAX_TICKETS = 3

# Amount of tickets we have sold.
tickets_sold = 0


# Main loop for every ticket
while tickets_sold < MAX_TICKETS:
    # Get Name
    name = get_input("Please enter your name or 'xxx to exit: ")

    # Program Kill Code
    if name == "xxx":
        break

    # Increment Tickets Sold
    tickets_sold += 1

    # Print amount of tickets sold.
    print(f"You have sold {tickets_sold} ticket/s so far.")
