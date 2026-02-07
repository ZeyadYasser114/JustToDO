tasks = []
while True:
    print("=====================")
    print("Welcome To JustToDO")
    print("=====================")
    print("""
    1- Add Tasks
    2- View Tasks
    3- Exit
    """)
    choice = input("Choose: ")
    if choice == '1':
        task = input("Enter Task: ")
        tasks.append(task)
    elif choice == '2':
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("Your tasks: ")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}- {task}")
    elif choice == '3':
        print("Thank you for using JustToDO.")
        break
    else:
        print("Error, Invalid input, please try again")