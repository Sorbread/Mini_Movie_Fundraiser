# Get ticket price

# Ticket prices for age categories
TICKET_PRICE = {"child": 7.50, "adult": 10.50, "senior": 6.50}
LOSS_PER_TICKET = 5


# Calculate Ticket Prace based on age input
def calc_ticket_price(age):
    # Convert age to a category, e.g. 7 to 'child'
    if age < 16:
        category = "child"
    elif age < 64:
        category = "adult"
    else:
        category = "senior"
    category_to_price = TICKET_PRICE[category]

    print(
        f"For an age of {age}, you are counted as a {category} and your ticket will cost ${category_to_price:.2f}"
    )


calc_ticket_price(12)
