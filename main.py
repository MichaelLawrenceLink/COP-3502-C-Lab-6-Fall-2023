# Michael Link
# COP 3502 C
# Fall 2023
# Partner: Logan Chenicek

def print_menu():
    print("""
    Menu
-------------
1. Encode
2. Decode
3. Quit
""")

def encode(inputted_password):
    assert int(inputted_password),"Entered password is not all numbers."
    assert len(inputted_password) == 8, "Password is not eight characters long"
    password = ""
    for digit in inputted_password:
        pass_digit = int(digit)+3
        password += str(pass_digit)[-1]
    return password

def decode(password):
    pass

def print_menu():
    print("""Menu
-------------
1. Encode
2. Decode
3. Quit""")


def main():
    while True:
        print_menu()
        option = int(input("Please enter an option:"))
        if option == 1:
            encoded_password = encode(input("Please enter your password to encode:"))
            print("Your password has been encoded and stored.")
        if option == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}")
        if option == 3:
            break



if __name__ == "__main__":
    main()
