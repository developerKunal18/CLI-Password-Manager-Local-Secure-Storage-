import base64

FILE = "data.txt"

def encode(text):
    return base64.b64encode(text.encode()).decode()

def decode(text):
    return base64.b64decode(text.encode()).decode()

def add_password():
    account = input("Enter account name: ")
    password = input("Enter password: ")

    with open(FILE, "a") as file:
        file.write(f"{account}:{encode(password)}\n")

    print("Password saved.")

def view_passwords():
    try:
        with open(FILE, "r") as file:
            print("\nStored Passwords:\n")
            for line in file:
                account, password = line.strip().split(":")
                print(f"{account} → {decode(password)}")
    except FileNotFoundError:
        print("No data found.")

while True:
    print("\n1. Add Password")
    print("2. View Passwords")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_password()
    elif choice == "2":
        view_passwords()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
