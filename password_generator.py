import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    
    # Get user input for password length
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    # Generate and display the password
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
