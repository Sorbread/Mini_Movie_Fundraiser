# Export Data to File

import pandas
import random
from datetime import date


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# dictionaries to hold ticket details
all_names = ["a", "b", "c", "d", "e"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
all_surcharge = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharge,
}

# main routine
mini_movie_frame = pandas.DataFrame(mini_movie_dict)
# mini_movie_frame = mini_movie_frame.set_index('Name')

# calculate the total ticket cost (ticket + surcharge)
mini_movie_frame["Total"] = (
    mini_movie_frame["Ticket Price"] + mini_movie_frame["Surcharge"]
)

# calculate the profit for each ticket
mini_movie_frame["Profit"] = mini_movie_frame["Ticket Price"] - 5

# calculate ticket and profit totals
total = mini_movie_frame["Total"].sum()
profit = mini_movie_frame["Profit"].sum()


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
if total != MAX_TICKETS:
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
