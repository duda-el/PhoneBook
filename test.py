# sort by alphabet
# update,remove,add mobile numbers and names
# search mobile numbers and names


contact = {"Duda" : "592505750",
           "Duto" : "599595750"}


while True:
    choose = print("\n 1. Seacrh contact \n 2. Add contact \n 3. Delete contact \n 4. Update contact \n 5. Display contacts \n")
    choose_1 = int(input("What you would like to do? "))

    
    if choose_1 == 1:
        search_name = input("Please enter name or part of a name: ")
        found = False
        for name,number in contact.items():
            if search_name.lower() in name.lower():
                print(f"{name}'s contact number is {number}")
                found = True
        if found == False:
                print(f"No contact found for {search_name.capitalize()}")
    elif choose_1 == 2:
        add_name = input("Please enter name: ")
        while add_name.isdigit():
             print("ERROR: Name can't contain number")
             add_name = input("Please enter name: ")
        add_contact = input("Please enter contact:")
        dict_add = contact[add_name.capitalize()] = add_contact

        
