import tkinter as tk
from tkinter import messagebox, simpledialog
import shelve
from datetime import datetime

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Tarefas")
        self.root.configure(bg='#FFFFFF')
        self.root.geometry("400x400")
        self.tasks = []
        self.load_tasks()

        # Listbox com borda colorida
        self.task_listbox = tk.Listbox(root, width=50, height=15, bd=2, relief='solid', bg='#ffffff', fg='#000000', highlightthickness=1, highlightcolor='#007acc')
        self.task_listbox.pack(pady=10)

        self.load_task_listbox()

        # Frame para alinhar os botões à esquerda
        button_frame = tk.Frame(root, bg='#FFFFFF')
        button_frame.pack(fill=tk.X, padx=10, pady=5)

        button_font = ('Verdana', 10, 'bold')

        self.add_button = tk.Button(button_frame, text="Adicionar Tarefa", command=self.add_task, bg='#8A2BE2', fg='#ffffff', font=button_font)
        self.add_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.add_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.update_button = tk.Button(button_frame, text="Atualizar Tarefa", command=self.update_task, bg='#FF1493', fg='#ffffff', font=button_font)
        self.update_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.delete_button = tk.Button(button_frame, text="Excluir Tarefa", command=self.delete_task, bg='#2E8B57', fg='#ffffff', font=button_font)
        self.delete_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.view_button = tk.Button(button_frame, text="Visualizar Tarefa", command=self.view_task, bg='#4169E1', fg='#ffffff', font=button_font)
        self.view_button.pack(side=tk.LEFT, padx=5, pady=5)

    def load_tasks(self):
        with shelve.open('tasks_db') as db:
            self.tasks = db.get('tasks', [])

    def save_tasks(self):
        with shelve.open('tasks_db') as db:
            db['tasks'] = self.tasks

    def load_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task['title'])

    def add_task(self):
        title = simpledialog.askstring("Adicionar Tarefa", "Título da Tarefa:")
        if title:
            category = simpledialog.askstring("Adicionar Tarefa", "Categoria:")
            priority = simpledialog.askstring("Adicionar Tarefa", "Prioridade (Alta, Média, Baixa):")
            due_date = simpledialog.askstring("Adicionar Tarefa", "Data de Vencimento (DD-MM-YYYY):")
            if due_date:
                try:
                    datetime.strptime(due_date, '%d-%m-%Y')
                except ValueError:
                    messagebox.showerror("Erro na execução.", "Data de vencimento inválida!")
                    return
            reminder = simpledialog.askstring("Adicionar nova Tarefa", "Lembrete (DD-MM-YYYY HH:MM):")
            if reminder:
                try:
                    datetime.strptime(reminder, '%d-%m-%Y %H:%M')
                except ValueError:
                    messagebox.showerror("Erro ao salvar.", "Formato de lembrete inválido!")
                    return
            self.tasks.append({
                'title': title,
                'category': category,
                'priority': priority,
                'due_date': due_date,
                'reminder': reminder
            })
            self.save_tasks()
            self.load_task_listbox()

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Erro ao salvar.", "Nenhuma tarefa selecionada!")
            return
        task = self.tasks[selected_index[0]]
        new_title = simpledialog.askstring("Atualizar Tarefa", "Título da Tarefa:", initialvalue=task['title'])
        if new_title:
            task['title'] = new_title
        new_category = simpledialog.askstring("Atualizar Tarefa", "Categoria:", initialvalue=task['category'])
        if new_category:
            task['category'] = new_category
        new_priority = simpledialog.askstring("Atualizar Tarefa", "Prioridade (Alta, Média, Baixa):", initialvalue=task['priority'])
        if new_priority:
            task['priority'] = new_priority
        new_due_date = simpledialog.askstring("Atualizar Tarefa", "Data de Vencimento (DD-MM-YYYY):", initialvalue=task['due_date'])
        if new_due_date:
            try:
                datetime.strptime(new_due_date, '%d-%m-%Y')
                task['due_date'] = new_due_date
            except ValueError:
                messagebox.showerror("Erro", "Data de vencimento inválida!")
                return
        new_reminder = simpledialog.askstring("Atualizar Tarefa", "Lembrete (DD-MM-YYYY HH:MM):", initialvalue=task['reminder'])
        if new_reminder:
            try:
                datetime.strptime(new_reminder, '%d-%m-%Y %H:%M')
                task['reminder'] = new_reminder
            except ValueError:
                messagebox.showerror("Erro", "Formato de lembrete inválido!")
                return
        self.save_tasks()
        self.load_task_listbox()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Erro", "Nenhuma tarefa selecionada!")
            return
        del self.tasks[selected_index[0]]
        self.save_tasks()
        self.load_task_listbox()

    def view_task(self):
        selected_index = self.task_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Erro", "Nenhuma tarefa selecionada!")
            return
        task = self.tasks[selected_index[0]]
        task_details = (f"Título: {task['title']}\n"
                        f"Categoria: {task['category']}\n"
                        f"Prioridade: {task['priority']}\n"
                        f"Data de Vencimento: {task['due_date']}\n"
                        f"Lembrete: {task['reminder']}")
        messagebox.showinfo("Detalhes da Tarefa", task_details)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
