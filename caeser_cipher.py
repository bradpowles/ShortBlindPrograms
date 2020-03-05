def caeser_cipher(input_text, offset):
    return("".join([chr((ord(char) - 65 + int(offset)) % 26 + 65) if 65 <= ord(char) <= 90 else char for char in input_text]))
