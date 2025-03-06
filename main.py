decript_phone = []
encripted_code = []
decripted_code = []

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

print("hello wellcome to the encript and decripting program.")
print("This program can be used to decript and encript phone code")
while True:
    choice = input("will you be decripting or encripting code this time? [encript/decript] ")
    if choice == "encript":
        choice = input("please enter what you want to encript: ")
        
        break

    elif choice == "decript":
        choice = input("please enter what you would like to decript: ")
        break

    else:
        print("thats not an option, please enter ether encript or dycript for this program to work")
        pass
