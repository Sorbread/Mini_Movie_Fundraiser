import pandas
import random


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

# currency formatting (calling currency function)
add_dollars = ["Ticket Price", "Surcharge", "Total", "Profit"]
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

print("---- Ticket Data ----\n")

# set index at end (before printing)
mini_movie_frame = mini_movie_frame.set_index("Name")

# output table with ticket data
print(mini_movie_frame)

print("\n---- Raffle Winner ----")
print(
    f"\nCongratulations {winner_name}. You have won ${total_won :.2f} ie: your ticket is free!\n\n\n"
)
