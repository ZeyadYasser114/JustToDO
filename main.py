import json
from datetime import datetime

def show_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        checkbox = "[✓]" if task["done"] else "[ ]"
        created = task.get("created_at", 'N/A')
        print(f"{i}- {checkbox} {task['title']}  [{created}]")
        if task.get('notes'):
            print(f"    Notes: {task['notes']}")
def edit_tasks(tasks):
    if not tasks:
        print("No tasks to edit.")
    else:
        print("Your tasks:")
        show_tasks(tasks)
        try:
            num = int(input("Enter task number to edit (0 to cancel): "))
            if num == 0:
                return
            index = num - 1
            if 0 <= index < len(tasks):
                print(f"\nEditing: {tasks[index]['title']}")
                print("What would you like to edit?")
                print("1- Title")
                print("2- Notes")
                print("3- Both")
                edit_choice = input("Choose: ")
                if edit_choice == '1':
                    new_title = input("Enter a new title: ")
                    tasks[index]['title'] = new_title
                    print(f"Title updated to {new_title}.")
                elif edit_choice == '2':
                    new_notes = input("Enter new notes: ")
                    tasks[index]['notes'] = new_notes
                    print(f"Notes updated to {new_notes}")
                elif edit_choice == '3':
                    new_title = input("Enter a new title: ")
                    new_notes = input("Enter new notes: ")
                    tasks[index]['title'] = new_title
                    tasks[index]['notes'] = new_notes
                    print("Task updated.")
                else:
                    print("Invalid Choice")
                    return
                save_tasks(tasks)
        except ValueError:
            print('Please enter a valid number.')
def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def delete_tasks(tasks):
    if not tasks:
        print("No tasks to delete.")
    else:
        print("Your tasks:")
        show_tasks(tasks)
        try:
            num = int(input("Enter task number to delete (0 to cancel): "))
            if num == 0:
                return
            index = num - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                save_tasks(tasks)
                print(f"Deleted: {removed['title']}")
            else: 
                print("Invalid task number.")
        except ValueError:
            print('Please enter a valid number.')

def check_tasks(tasks):
    if not tasks:
        print("No tasks to check.")
    else:
        print("Your tasks:")
        show_tasks(tasks)
        try:
            num = int(input("Enter the number to check/uncheck (0 to cancel): "))
            if num == 0:
                return
            index = num - 1
            if 0 <= index < len(tasks):
                tasks[index]["done"] = not tasks[index]["done"]
                save_tasks(tasks)
                status = "checked" if tasks[index]["done"] else "Unchecked"
                print(f"{tasks[index]['title']} {status}!")
            else:
                print("Invalid task number.")
        except ValueError:
            print('Please enter a valid number.')

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