contacts = {
    "Thomas": {
        "phone number": "0842669858"
    },
    "Spicy": {
        "phone number": "+84984923319"
    }
}

import pyinputplus


def view_all_contact():
    for contact in contacts:
        contact_name = contact
        contact_number = contacts[contact]['phone number']
        print(f"Name: {contact_name}\nContact Number: {contact_number}")


def add_contact():
    contact_name = input("Insert Name: ")
    contact_number = input("Insert Phone number: ")
    contacts[contact_name] = {
        "phone number": contact_number
    }
    print("\nViewing all contact\n")
    view_all_contact()


def search_contact():
    search_key = input("Please enter keyword to search: ")
    for contact_name, contact_info in contacts.items():
        if search_key.lower() in contact_name.lower():
            contact_name = contact_name
            contact_number = contacts[contact_name]['phone number']
            print(f"Name: {contact_name}\nContact Number: {contact_number}")
            break
        else:
            print("Contact Not Found!")
            break


functions = ["View All Contact", "Add New Contact", "Search For Contact", "Quit"]
usr_choice = pyinputplus.inputMenu(functions, prompt="Welcome to Contact Book Program, what do you want to do:\n", numbered=True)
print(usr_choice)

if usr_choice == functions[0]:
    view_all_contact()
elif usr_choice == functions[1]:
    add_contact()
elif usr_choice == functions[2]:
    search_contact()
elif usr_choice == functions[-1]:
    print("Goodbye!")