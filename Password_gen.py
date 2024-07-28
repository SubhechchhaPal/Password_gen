import random
import string

def user_choice():
    length = int(input("Enter the desired length of the password: "))
    uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    digits = input("Include digits? (y/n): ").lower() == 'y'
    special = input("Include special characters? (y/n): ").lower() == 'y'
    return length,uppercase,lowercase,digits,special

def character(uppercase,lowercase,digits,special):
    character = ''
    if uppercase:
        character += string.ascii_uppercase
    if lowercase:
        character += string.ascii_lowercase
    if digits:
        character += string.digits
    if special:
        character+= string.punctuation
    return character

def password(length,char):
    return ''.join(random.choice(char) for _ in range(length))

def main():
    length,uppercase,lowercase,digits,special =user_choice()
    char = character(uppercase,lowercase,digits,special)
    
    if not char:
        print("No character types selected. Please include at least one type of character.")
        return

    gen_password =password(length,char)
    print(f"Generated password: {gen_password}")

if __name__ == "__main__":
    main()
