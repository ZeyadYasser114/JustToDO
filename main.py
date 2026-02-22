from functions import datetime
from functions import load_tasks
from functions import save_tasks
from functions import delete_tasks
from functions import edit_tasks
from functions import check_tasks
from functions import show_tasks
# ===============================================================
print("*********************")
print("Welcome To JustToDO")
print("*********************")
tasks = load_tasks()
while True:
    print("""
|===============|
|1- Add Tasks   |
|2- View Tasks  |
|3- Edit Tasks  |
|4- Delete Tasks|
|5- Check Tasks |
|6- Exit        |
|===============|
    """)
    choice = input("Choose: ")
    if choice == '1':
        task = input("Enter Task (0 to cancel): ")
        if task == '0':
            continue
        note = input("Enter Note (Optional, press enter to skip): ")
        tasks.append({'title': task,
                      'done': False,
                      'notes': note,
                      'created_at': datetime.now().strftime("%m / %d/ %Y  %H:%M:%S")})
        save_tasks(tasks)
    elif choice == '2':
        if not tasks:
            print("No tasks yet.")
        else:
            print("Your tasks: ")
            show_tasks(tasks)
    elif choice == '3':
        edit_tasks(tasks)
    elif choice == '4':
        delete_tasks(tasks)
    elif choice == '5':
        check_tasks(tasks)
    elif choice == '6':
        print("Thank you for using JustToDO.")
        break
    else:
        print("Error, Invalid input, please try again.")