class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f'Name: {self.name}\nPhone Number: {self.phone_number}\nEmail: {self.email}'


class Contact_Book:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("Contact found:")
                print(contact)
                return
        print(" Contact not found.")

    def view_contacts(self):
        if not self.contacts:
            print(" Contact book is empty.")
            return
        print("\n All Contacts:")
        for contact in self.contacts:
            print(contact)

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"🗑️ Contact '{name}' deleted.")
                return
        print("No such contact found to delete.")


def get_contact_input():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    return Contact(name, phone, email)


def main():
    book = Contact_Book()

    while True:
        print("\n==== Contact Book Menu ====")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact by Name")
        print("4. Delete Contact by Name")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            contact = get_contact_input()
            book.add_contact(contact)

        elif choice == '2':
            book.view_contacts()

        elif choice == '3':
            search = input("Enter name to search: ")
            book.search_contact(search)

        elif choice == '4':
            delete_name = input("Enter name to delete: ")
            book.delete_contact(delete_name)

        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please select from 1 to 5.")


if __name__ == "__main__":
    main()
