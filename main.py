decript_phone = []
encripted_code = []
decripted_code = []

code = {
    "a": "2", "b": "22", "c": "222", "d": "3", "e": "33", "f": "333", "g": "4", "h": "44", "i": "444", 
    "j": "5", "k": "55", "l": "555", "m": "6", "n": "66", "o": "666", "p": "7", "q": "77", "r": "777", 
    "s": "7777", "t": "8", "u": "88", "v": "888", "w": "9", "x": "99", "y": "999", "z": "9999"
}

print("hello wellcome to the encript and decripting program.")
print("This program can be used to decript and encript phone code")
while True:
    choice = input("will you be decripting or encripting code this time? [encript/decript] ")
    if choice == "encript":
        choice = input("please enter what you want to encript ")
        break

    elif choice == "decript":
        choice = input("please enter what you would like to decript ")
        break

    else:
        print("thats not an option, please enter ether encript or dycript for this program to work")
        pass
