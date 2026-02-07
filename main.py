import json
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
        for i, task in enumerate(tasks, start=1):
            print(f"{i}- {task}")
        try:
            num = int(input("Enter task number to delete: "))
            index = num - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                save_tasks(tasks)
                print(f"Deleted: {removed}")
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
===============
1- Add Tasks
2- View Tasks
3- Delete Tasks
4- Exit
===============
    """)
    choice = input("Choose: ")
    if choice == '1':
        task = input("Enter Task: ")
        tasks.append(task)
        save_tasks(tasks)
    elif choice == '2':
        if not tasks:
            print("No tasks yet.")
        else:
            print("Your tasks: ")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}- {task}")
    elif choice == '3':
        delete_tasks(tasks)
    elif choice == '4':
        print("Thank you for using JustToDO.")
        break
    else:
        print("Error, Invalid input, please try again.")