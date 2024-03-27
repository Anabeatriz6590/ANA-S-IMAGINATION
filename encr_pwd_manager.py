import hashlib

class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def add_password(self, website, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.passwords[website] = {"username": username, "password": hashed_password}
        print(f"Password for {website} added successfully.")

    def get_password(self, website):
        if website in self.passwords:
            return self.passwords[website]
        else:
            return None

    def list_websites(self):
        print("Websites with their saved passwords:")
        for website in self.passwords:
            print(website)

if __name__ == "__main__":
    manager = PasswordManager()

    while True:
        print("\n1. Add a Password")
        print("2. Get Password")
        print("3. List Websites")
        print("4. Exit")

        choice = input("Choose an option to proceed: ")

        if choice == "1":
            website = input("Enter the website name: ").upper()
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            manager.add_password(website, username, password)
        elif choice == "2":
            website = input("Enter the website name to get the password: ").upper()
            stored_password = manager.get_password(website)
            if stored_password:
                print(f"Username: {stored_password['username']}")
                print("Password: *****")
            else:
                print("Password not found for this website.")
        elif choice == "3":
            manager.list_websites()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")