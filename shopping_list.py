# Part B: Shopping List Manager

shopping_list = []

while True:
    choice = input("Enter command (add / remove / show / done): ").strip().lower()
    
    if choice == "add":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"'{item}' added to your list.")
        
    elif choice == "remove":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' removed from your list.")
        else:
            print("That item is not on your list.")
            
    elif choice == "show":
        print("--- Current Shopping List ---")
        if not shopping_list:
            print("Your list is empty.")
        else:
            for item in shopping_list:
                print(item)
        print("-----------------------------")
        
    elif choice == "done":
        print("Goodbye! Exiting shopping list manager.")
        break
        
    else:
        print("Invalid command. Please use add, remove, show, or done.")