# sort by alphabet
# update,remove,add mobile numbers and names
# search mobile numbers and names


phonebook = {"Duda" : "592505750",
           "Gela" : "597603450",
           "Mariami" : "577402490",
           "Alexi" : "595115427"}


while True:
    choose = print("\n 1. Seacrh contact \n 2. Add contact \n 3. Delete contact \n 4. Update contact \n 5. Display phonebook \n")
    choose_1 = int(input("What you would like to do? "))

    
    if choose_1 == 1:
        search_name = input("Please enter name or part of a name: ")
        found = False
        for name,number in phonebook.items():
            if search_name.lower() in name.lower():
                print(f"{name}'s contact number is {number}")
                found = True
        if found == False:
                print(f"No contact found for {search_name.capitalize()}")
                
    elif choose_1 == 2:
        add_name = input("Please enter name: ")
        add_phonebook = input("Please enter contact: ")
        dict_add = phonebook[add_name.capitalize()] = add_phonebook

    elif choose_1 == 3:
        delete_name = input("Please enter name or part of a name: ")
        if delete_name.capitalize() in phonebook:
            phonebook.pop(delete_name.capitalize())
        elif delete_name.lower() not in phonebook.lower():
             print(f"No contact found for {delete_name.capitalize()}")

    elif choose_1 == 5:
         for name,number in sorted(phonebook.items()):
              print(f"{name} - {number}")
        
        
