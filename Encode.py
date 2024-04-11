# by seamus
def encode(rawPass):
    encoded = ""
    for char in rawPass:
        char = str(int(char) + 3)
        encoded += char
    return encoded