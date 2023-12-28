import random
import string

def Password_Generator(min_length,add_numbers,add_special_chars):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    characters = ""
    characters += letters

    if add_numbers:
        characters += digits
    if add_special_chars:
        characters += special
    
    password = ""

    has_number = False
    has_special = False
    meets_conditions = False

    while not meets_conditions or len(password) < min_length:
        character = random.choice(characters)
        password += character

        if character in digits:
            has_number = True
        elif character in special:
            has_special = True
        
        meets_conditions = True

        if add_numbers:
            meets_conditions = has_number
        if add_special_chars:
            meets_conditions = meets_conditions and has_special
    
    return password


print("""            
            ████████╗░█████╗░██████╗░██╗██╗░░██╗██╗░░██╗██╗░░██╗
            ╚══██╔══╝██╔══██╗██╔══██╗██║██║░██╔╝██║░██╔╝██║░░██║
            ░░░██║░░░███████║██████╔╝██║█████═╝░█████═╝░███████║
            ░░░██║░░░██╔══██║██╔══██╗██║██╔═██╗░██╔═██╗░██╔══██║
            ░░░██║░░░██║░░██║██║░░██║██║██║░╚██╗██║░╚██╗██║░░██║
            ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝
        """)

min_length = int(input("Enter the min lenght of your password: "))
add_numbers = input("Do you want to add digits to your password (y/n): ").lower() == "y"
add_special_chars = input("Do you want to add special characters to your password (y/n): ").lower() == "y"


password = Password_Generator(min_length,add_numbers,add_special_chars)
print(f"That's your password: {password}")

            

