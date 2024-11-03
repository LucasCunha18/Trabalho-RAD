Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import tkinter as tk
... from tkinter import messagebox, Listbox, Scrollbar
... 
... class GerenciadorDeTarefas:
...     def __init__(self, root):
...         self.root = root
...         self.root.title("Gerenciador de Tarefas")
...         
...         self.tarefas = []
...         
...         self.label = tk.Label(root, text="Digite uma nova tarefa:")
...         self.label.pack(pady=10)
... 
...         self.entrada = tk.Entry(root, width=50)
...         self.entrada.pack(pady=5)
... 
...         self.botao_adicionar = tk.Button(root, text="Adicionar", command=self.adicionar_tarefa)
...         self.botao_adicionar.pack(pady=5)
... 
...         self.botao_remover = tk.Button(root, text="Remover", command=self.remover_tarefa)
...         self.botao_remover.pack(pady=5)
... 
...         self.lista_tarefas = Listbox(root, width=50, height=10)
...         self.lista_tarefas.pack(pady=10)
... 
...         self.scrollbar = Scrollbar(root)
...         self.scrollbar.pack(side='right', fill='y')
... 
...         self.lista_tarefas.config(yscrollcommand=self.scrollbar.set)
...         self.scrollbar.config(command=self.lista_tarefas.yview)
... 
...     def adicionar_tarefa(self):
...         tarefa = self.entrada.get()
...         if tarefa:
...             self.tarefas.append(tarefa)
            self.atualizar_lista()
            self.entrada.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada inválida", "Por favor, digite uma tarefa.")

    def remover_tarefa(self):
        try:
            index = self.lista_tarefas.curselection()[0]
            del self.tarefas[index]
            self.atualizar_lista()
        except IndexError:
            messagebox.showwarning("Seleção inválida", "Por favor, selecione uma tarefa para remover.")

    def atualizar_lista(self):
        self.lista_tarefas.delete(0, tk.END)
        for tarefa in self.tarefas:
            self.lista_tarefas.insert(tk.END, tarefa)

if __name__ == "__main__":
    root = tk.Tk()
    app = GerenciadorDeTarefas(root)
    root.mainloop()
