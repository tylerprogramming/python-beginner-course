# Contact Book Application

# Defining a class for contacts
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"


# Contact book class to manage contacts
class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(contact)

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]


# Creating a contact book instance
contact_book = ContactBook()

# Adding contacts
contact1 = Contact("Alice", "123-456-7890", "alice@example.com")
contact2 = Contact("Bob", "987-654-3210", "bob@example.com")

contact_book.add_contact(contact1)
contact_book.add_contact(contact2)

# Viewing contacts
print("All Contacts:")
contact_book.view_contacts()

# Deleting a contact
contact_book.delete_contact("Alice")

# Viewing contacts after deletion
print("\nContacts after deletion:")
contact_book.view_contacts()
