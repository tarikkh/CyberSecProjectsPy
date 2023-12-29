import string
import sys

allchars = string.digits + string.ascii_letters + string.punctuation + " "
allchars_len = len(allchars)

def caesar_cipher_encrypt(word, shift=15):
    encrypted = ""
    for char in word:
        try:
            indexchar = allchars.index(char)
        except ValueError:
            print("Invalid characters entered. Please use only valid characters.")
            sys.exit(1)
        resultIndex = (indexchar + shift) % allchars_len
        encrypted += allchars[resultIndex]
    return encrypted

def caesar_cipher_decrypt(word, shift=15):
    decrypted = ""
    for char in word:
        try:
            indexchar = allchars.index(char)
        except ValueError:
            print("Invalid characters entered. Please use only valid characters.")
            sys.exit(1)
        resultIndex = (indexchar - shift) % allchars_len
        decrypted += allchars[resultIndex]
    return decrypted

print("""            
    ████████╗░█████╗░██████╗░██╗██╗░░██╗██╗░░██╗██╗░░██╗
    ╚══██╔══╝██╔══██╗██╔══██╗██║██║░██╔╝██║░██╔╝██║░░██║
    ░░░██║░░░███████║██████╔╝██║█████═╝░█████═╝░███████║
    ░░░██║░░░██╔══██║██╔══██╗██║██╔═██╗░██╔═██╗░██╔══██║
    ░░░██║░░░██║░░██║██║░░██║██║██║░╚██╗██║░╚██╗██║░░██║
    ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝
""")

def menu():
    print("*******************************************************")
    print("1 for encryption\n2 for decryption\n3 Quit")
    print("*******************************************************")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid input (1-3).")
        return None
    
    if choice == 3:
        print("Goodbye!")
    elif choice not in [1, 2]:
        print("Invalid choice. Please enter a valid option (1 or 2).")
    else:
        word = input("Enter your input (word): ")
        if choice == 1:
            print(f"Your input: {word} ----> Encryption: {caesar_cipher_encrypt(word)}")
        elif choice == 2:
            print(f"Your input: {word} ----> Decryption: {caesar_cipher_decrypt(word)}")

    return choice

choice = menu()
while choice != 3:
    choice = menu()
