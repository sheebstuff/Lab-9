from Encode import encode

if __name__ == "__main__":
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode\n"
              "2. Decode\n"
              "3. Quit")

        selection = int(input("Please enter an option: "))
        if selection == 1:
            decodedPassword = (input("Please enter your password to encode: "))
            encodedPassword = encode(decodedPassword)
            print("Your password has been encoded and stored!",encodedPassword)
        elif selection == 2:
            print(f"The encoded password is f{encodedPassword}, and the original is ")
