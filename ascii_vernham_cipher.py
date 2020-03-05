def ascii_vernham_cipher(input_text, keyword):
    return("".join([chr(((ord(input_text[i]) - 65) + (ord(keyword[i % len(keyword)]) - 64)) % 26 + 65) for i in range(len(input_text))]))
