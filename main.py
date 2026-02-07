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
            checkbox = "[✓]" if task["done"] else "[ ]"
            print(f"{i}- {checkbox} {task['title']}")
        try:
            num = int(input("Enter task number to delete: "))
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
        for i, task in enumerate(tasks, start=1):
            checkbox = "[✓]" if task["done"] else "[ ]"
            print(f"{i}- {checkbox} {task['title']}")
        try:
            num = int(input("Enter the number to check/uncheck: "))
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
===============
1- Add Tasks
2- View Tasks
3- Delete Tasks
4- Check Tasks
5- Exit
===============
    """)
    choice = input("Choose: ")
    if choice == '1':
        task = input("Enter Task: ")
        tasks.append({'title': task, 'done': False})
        save_tasks(tasks)
    elif choice == '2':
        if not tasks:
            print("No tasks yet.")
        else:
            print("Your tasks: ")
            for i, task in enumerate(tasks, start=1):
                checkbox = "[✓]" if task["done"] else "[ ]"
                print(f"{i}- {checkbox} {task['title']}")
    elif choice == '3':
        delete_tasks(tasks)
    elif choice == '4':
        check_tasks(tasks)
    elif choice == '5':
        print("Thank you for using JustToDO.")
        break
    else:
        print("Error, Invalid input, please try again.")