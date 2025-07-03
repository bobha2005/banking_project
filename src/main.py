# This is the entry point for CLI application.
# manages user interface and routing logic.

from auth import login, register
from banking import banking_menu

def main():
    while True:
        print("\n=== Secure CLI Banking System ===")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Select options: ")
        if choice == "1":
            user = login()
            if user:
                banking_menu(user)
        elif choice == "2":
            register()
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("\nInvalid options! Please try again.")

if __name__ == "__main__":
    main()