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
