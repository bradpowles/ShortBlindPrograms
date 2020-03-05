def encrypt2(message, keyword):
    return("".join([chr(((ord(message[i]) - 65) + (ord(keyword[i % len(keyword)]) - 64)) % 26 + 65) for i in range(len(message))]))
