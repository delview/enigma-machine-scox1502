new_code = []
decrypted_text = []

code_encrypt = {
    "a": "2", "b": "22", "c": "222", "d": "3", "e": "33", "f": "333", "g": "4", "h": "44", "i": "444", 
    "j": "5", "k": "55", "l": "555", "m": "6", "n": "66", "o": "666", "p": "7", "q": "77", "r": "777", 
    "s": "7777", "t": "8", "u": "88", "v": "888", "w": "9", "x": "99", "y": "999", "z": "9999",
}

code_decrypt = {
    "2": "a", "22": "b", "222": "c", "3": "d", "33": "e", "333": "f", "4": "g", "44": "h", "444": "i",
    "5": "j", "55": "k", "555": "l", "6": "m", "66": "n", "666": "o", "7": "p", "77": "q", "777": "r", 
    "7777": "s", "8": "t", "88": "u", "888": "v", "9": "w", "99": "x", "999": "y", "9999": "z",
}

print("Hello! Welcome to the encrypting and decrypting program.")
print("This program can be used to decrypt and encrypt phone codes.")

while True:
    choice = input("Will you be decrypting or encrypting code this time? [encrypt/decrypt] ").lower()
    
    if choice == "encrypt":
        text_to_encrypt = input("Please enter what you want to encrypt: ").lower()
        for char in text_to_encrypt:
            if char in code_encrypt:
                new_code.append(code_encrypt[char])
            else:
                new_code.append(char)
        print("Encrypted code:", ' '.join(new_code))
        break
    
    elif choice == "decrypt":
        text_to_decrypt = input("Please enter the code to decrypt (use spaces between codes): ").split()
        for code in text_to_decrypt:
            if code in code_decrypt:
                decrypted_text.append(code_decrypt[code])
            else:
                decrypted_text.append('?')
        print("Decrypted text:", ''.join(decrypted_text))
        break
    
    else:
        print("That's not an option! Please enter either 'encrypt' or 'decrypt' to proceed.")
        pass