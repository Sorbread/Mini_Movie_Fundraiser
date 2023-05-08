# get_age.py
# get user age

MIN_AGE = 12
MAX_AGE = 120


# Get the user age.
def get_age(text):
    while True:
        # Get age without erroring
        try:
            age = int(input(text))
        except:
            print("Please enter a whole number (e.g. 12,13,14)")

        # Check age against constraints
        if age < MIN_AGE:
            print(f"You must be over {MIN_AGE}")
            continue
        elif age > MAX_AGE:
            print(f"You must be younger than {MAX_AGE}.")
            continue
        return age


while True:
    # Check user age is above 12
    age = get_age("Please enter your age: ")

    # Continue with program
