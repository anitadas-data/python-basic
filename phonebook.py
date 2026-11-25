def phonebook():
    phonebook = {}

    n = int(input("How many contacts do you want to add?: "))

    for i in range(n):
        name = input("Enter Name: ")
        number = input("Enter Number: ")
        phonebook[name] = number

    search = input("Search Name: ")
    print(phonebook.get(search, "Not Found"))

    delete = input("Delete Name: ")
    phonebook.pop(delete, None)

    update_name = input("Update Name: ")
    update_number = input("New Number: ")
    phonebook.update({update_name: update_number})

    print("\nAll Contacts")
    for name, number in phonebook.items():
        print(name, ":", number)

    print("Total Contacts:", len(phonebook))

phonebook()