from tkinter import *
class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-do-list')
        self.root.geometry('650x410+300+150')

        self.label = Label(self.root, text='To-Do-List-App',
                           font='arial 25 bold', width=10, bd=5, bg='orange', fg='black')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add task',
                            font='arial 18 bold', width=10, bd=5, bg='orange', fg='black')
        self.label2.place(x=40, y=54)

        self.label3 = Label(self.root, text='Tasks',
                            font='arial 18 bold', width=10, bd=5, bg='orange', fg='black')
        self.label3.place(x=320, y=54)

        self.main_text = Listbox(self.root, height=9, bd=5, width=23, font="arial 20 italic bold")
        self.main_text.place(x=280, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30, font='arial 10 bold')
        self.text.place(x=20, y=120)

        self.button = Button(self.root, text="Add", font='arial 20 bold italic',
                             width=10, bd=5, fg='black', command=self.add_task)
        self.button.place(x=30, y=180)

        self.button2 = Button(self.root, text="Delete", font='arial 20 bold italic',
                              width=10, bd=5, fg='black', command=self.delete_task)
        self.button2.place(x=30, y=280)

        self.load_tasks()  # Load existing tasks from the file

    def add_task(self):
        content = self.text.get(1.0, END)
        self.main_text.insert(END, content)
        with open('data.txt', 'a') as file:
            file.write(content)
        self.text.delete(1.0, END)

    def delete_task(self):
        selected_indices = self.main_text.curselection()
        if selected_indices:
            for index in selected_indices:
                self.main_text.delete(index)
            self.save_tasks()

    def load_tasks(self):
        try:
            with open('data.txt', 'r') as file:
                tasks = file.readlines()
                for task in tasks:
                    self.main_text.insert(END, task)
        except FileNotFoundError:
            pass

    def save_tasks(self):
        tasks = self.main_text.get(0, END)
        with open('data.txt', 'w') as file:
            file.writelines(tasks)

def main():
    root = Tk()
    Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()