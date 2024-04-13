def decode(coded_password):
    decoded = ""
    for i in coded_password:
        i = str(int(i) - 3)
        decoded += i
    return decoded