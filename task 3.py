import random
import string

def generate_password(length):
    # Define the character sets to use in generating the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password using random.choices (Python 3.6+)
    password = ''.join(random.choices(characters, k=length))
    
    return password
if __name__ == "__main__":
    try:
        # Get desired password length from user input
        length = int(input("Enter the desired length of the password: "))
        
        # Generate the password
        password = generate_password(length)
        
        # Print the generated password
        print("Generated password:", password)
        
    except ValueError:
        print("Error: Please enter a valid integer for password length.")
