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
print("This program can be used to decrypt and encrypt phone codes whitch are a type of code number pad flipphones used to text people with.")

while True:
    print("")
    choice = input("Will you be decrypting or encrypting code today? [encrypt/decrypt] ").lower()
    
    if choice == "encrypt":
        print("")
        print("Please enter what you want to encrypt please note it must be in only letters")
        print("")
        choice = input(": ").lower()
        print("")
        for char in choice:
            if char in code_encrypt:
                new_code.append(code_encrypt[char])
            else:
                new_code.append(char)
        print("Encrypted code:", ' '.join(new_code))
        print("")
    
    elif choice == "decrypt":
        print("")
        print("Please enter the code to decrypt (use spaces between codes and only use numbers) (if you are un familiar with phone code try the encrypter first)")
        print("")
        choice = input(": ").split()
        print("")
        for code in choice:
            if code in code_decrypt:
                decrypted_text.append(code_decrypt[code])
            else:
                decrypted_text.append('')
        print(" the decrypted text say's:", ''.join(decrypted_text))
        print("")

    
    else:
        print("That's not an option. please enter either 'encrypt' or 'decrypt' to proceed.")
        pass

    choice = input("would you like to encrypt or decript something else? [yes/no] ")
    if choice == "yes":
        print("")
        print("ok lets continue")
        pass
    if choice == "no":
        print("")
        print("ok goodbye")
        break