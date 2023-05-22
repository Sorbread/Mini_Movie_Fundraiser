# 00_base_v01.py
# The base program for 'Mini Movie Fundraiser'
# Made to buy tickets for movie
import pandas
import random
from datetime import date


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


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
            print(
                f"Please enter valid response, such as '{valid_responses[0]}' or '{valid_responses[1]}' "
            )


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

    return category, category_to_price


# dictionaries to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharge = []

# Constant, for testing purposes set to low number (e.g. 3)
MAX_TICKETS = 3

# Minimum and maximum ages for tickets as specified by client.
MIN_AGE = 12
MAX_AGE = 120


# Amount of tickets we have sold.
tickets_sold = 0


# Main loop
while tickets_sold < MAX_TICKETS:
    # Makes easier to see next input
    print("\n\n")

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
    # Calculate string version of age (e.g. 'child') and  ticket price (e.g. 7.50)
    age_stringified, ticket_price = calc_ticket_price(age)
    print(f"A ticket for a {age} year old person will cost you ${ticket_price:.2f}.")

    # Ask if this is the correct information, or exit out
    if yn("Would you like to continue? (Y/N): ") == "n":
        print("Thank you for your time.")
        continue

    payment_method = string_check(
        "Please enter your payment method (credit/cash): ",
        ["cr", "credit", "ca", "cash"],
    )

    # Calculate surcharge
    surcharge = 0
    if payment_method == "cr" or payment_method == "credit":
        surcharge = ticket_price * 0.05
        print(f"Credit will cost you ${surcharge:.2f} more.")

    total_cost = ticket_price + surcharge
    # Final confirmation of purchase
    if (
        yn(
            f"Would you like to confirm your payment of ${total_cost:.2f} for one {age_stringified} ticket? (Y/N): "
        )
        == "n"
    ):
        continue

    # Add data to final
    all_names.append(name)
    all_ticket_costs.append(ticket_price)
    all_surcharge.append(surcharge)

    # Increment Tickets Sold
    tickets_sold += 1

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharge,
}
# Set frame for our data
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# calculate the total ticket cost (ticket + surcharge)
mini_movie_frame["Total"] = (
    mini_movie_frame["Ticket Price"] + mini_movie_frame["Surcharge"]
)

# calculate the profit for each ticket
mini_movie_frame["Profit"] = mini_movie_frame["Ticket Price"] - 5

# choose a winner from our name list
winner_name = random.choice(all_names)

# get position of winner name in list
winner_index = all_names.index(winner_name)

# look up total amount won (ticket price + surcharge)
total_won = mini_movie_frame.at[winner_index, "Total"]

# Get Date
today = date.today()

day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")

# Main Heading
heading = "---- Mini Movie Fundraiser Ticket Date ({}/{}/{}) ----\n".format(
    day, month, year
)
filename = "MMF_{}_{}_{}".format(day, month, year)

mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)
MAX_TICKETS = 10

sales_status = "\nAll tickets have been sold."
if tickets_sold != MAX_TICKETS:
    sales_status = f"\nYou have sold {sales_status}."

# Ticket heading & text
ticket_cost_heading = "\n---- Ticket Cost / Profit ----"
total_ticket_sales = "Total Ticket Sales: ${:.2f}".format(total)
total_profit = "Total Profit: ${:.2f}".format(profit)

# Raffle heading & text
winner_heading = "\n---- Raffle Winner ----"
winner_text = f"\nCongratulations to {winner_name}. They have won ${total_won :.2f} ie: their ticket is free!"

to_write = [
    heading,
    mini_movie_string,
    ticket_cost_heading,
    total_ticket_sales,
    total_profit,
    sales_status,
    winner_heading,
    winner_text,
]

for item in to_write:
    print(item)

write_to = f"{filename}.txt"
text_file = open(write_to, "w+")
for item in to_write:
    text_file.write(item)
    text_file.write("\n")
text_file.close()
