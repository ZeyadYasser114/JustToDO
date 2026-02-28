from _datetime import datetime
import customtkinter as ctk
from functions import load_tasks, save_tasks, delete_tasks, edit_tasks, check_tasks
class JustToDo(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.tasks = load_tasks()
        self.title("JustToDo")
        self.geometry("500x600")
        self.setup_ui()
        self.refresh_list()
    def setup_ui(self):
        self.add_btn = ctk.CTkButton(self, text="+ Add Task", command=self.open_add_popup)
        self.add_btn.pack(pady=10)
        self.task_frame = ctk.CTkScrollableFrame(self, label_text="Your Tasks")
        self.task_frame.pack(fill="both", expand=True, padx=10, pady=10)
        ctk.CTkButton(self, text="Exit", command=self.destroy).pack(pady=5)
    def refresh_list(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()
        for i, task in enumerate(self.tasks):
            self.create_task_row(i, task)
    def create_task_row(self, index, task):
        row = ctk.CTkFrame(self.task_frame)
        row.pack(fill="x", pady=3)
        status = "✅" if task['done'] else "⬜"
        label = ctk.CTkLabel(row, text=f"{status} {task['title']}", anchor="w")
        label.pack(side="left", padx=8, expand=True, fill="x")
        ctk.CTkButton(row, text="✏️", width=35,
                      command=lambda i=index: self.open_edit_popup(i)).pack(side="right", padx=2)
        ctk.CTkButton(row, text="🗑️", width=35,
                      command=lambda i=index: self.handle_delete(i)).pack(side="right", padx=2)
        ctk.CTkButton(row, text="✔️", width=35,
                      command=lambda i=index: self.handle_check(i)).pack(side="right", padx=2)
    def open_add_popup(self):
        popup = ctk.CTkToplevel(self)
        popup.title("Add Task")
        popup.geometry("350x200")
        ctk.CTkLabel(popup, text="Task Title:").pack(pady=5)
        title_entry = ctk.CTkEntry(popup, width=300)
        title_entry.pack()
        ctk.CTkLabel(popup, text="Note (optional):").pack(pady=5)
        note_entry = ctk.CTkEntry(popup, width=300)
        note_entry.pack()
        def confirm():
            title = title_entry.get().strip()
            if title:
                self.tasks.append({
                    'title': title,
                    'done': False,
                    'notes': note_entry.get(),
                    'created_at': datetime.now().strftime("%m / %d/ %Y  %H:%M:%S")
                })
                save_tasks(self.tasks)
                self.refresh_list()
                popup.destroy()
        ctk.CTkButton(popup, text="Add", command=confirm).pack(pady=10)
    def open_edit_popup(self, index):
        task = self.tasks[index]
        popup = ctk.CTkToplevel(self)
        popup.title("Edit Task")
        popup.geometry("350x200")
        ctk.CTkLabel(popup, text="Task Title:").pack(pady=5)
        title_entry = ctk.CTkEntry(popup, width=300)
        title_entry.insert(0, task['title'])
        title_entry.pack()
        ctk.CTkLabel(popup, text="Note:").pack(pady=5)
        note_entry = ctk.CTkEntry(popup, width=300)
        note_entry.insert(0, task['notes'])
        note_entry.pack()
        def confirm():
            self.tasks[index]['title'] = title_entry.get().strip()
            self.tasks[index]['notes'] = note_entry.get()
            save_tasks(self.tasks)
            self.refresh_list()
            popup.destroy()
        ctk.CTkButton(popup, text="Save", command=confirm).pack(pady=10)
    def handle_delete(self, index):
        self.tasks.pop(index)
        save_tasks(self.tasks)
        self.refresh_list()
    def handle_check(self, index):
        self.tasks[index]['done'] = not self.tasks[index]['done']
        save_tasks(self.tasks)
        self.refresh_list()
app = JustToDo()
app.mainloop()