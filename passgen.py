import random
import string

def generate_password(length):
    if length < 4:
        print("Password should be at least 4 characters.")
        return ""

    # Create character pools
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # Randomly choose characters
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("🔐 Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        if password:
            print(f"Generated password: {password}")
    except ValueError:
        print("Please enter a valid number!")

if __name__ == "__main__":
    main()
