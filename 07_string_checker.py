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


string_check("enter y/n", ["y", "n"])
