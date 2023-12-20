class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print(f"{task} not found in the to-do list.")

    def display_tasks(self):
        print("To-Do List:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

# Example usage:
todo_list = ToDoList()
todo_list.add_task("Buy groceries")
todo_list.add_task("Read a book")
todo_list.display_tasks()
todo_list.remove_task("Buy groceries")
todo_list.display_tasks()
