from Encode import encode


def decode(coded_password):
    decoded = ""
    for i in coded_password:
        i = str(int(char) - 3)
        decoded += char
    return decoded


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
            print(f"The encoded password is {encodedPassword}, and the original is ", end="")
            decodedPassword = decode(encodedPassword)
            print(decodedPassword)

        elif selection == 3:
            break

