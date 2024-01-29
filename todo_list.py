# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:05:00 2024

@author: joali
"""
class Task:
    def __init__(self, description, status="Open", importance="Normal"):
        self.description = description
        self.status = status
        self.importance = importance

    def __str__(self):
        return f"{self.description} [Status: {self.status}, Importance: {self.importance}]"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def get_tasks(self):
        return self.tasks

    def display_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def change_task_status(self, task_number, new_status):
        if 1 <= task_number <= len(self.tasks):
            task = self.tasks[task_number - 1]
            task.status = new_status
            print("Task status updated.")
        else:
            print("Invalid task number.")

    def change_task_importance(self, task_number, new_importance):
        if 1 <= task_number <= len(self.tasks):
            task = self.tasks[task_number - 1]
            task.importance = new_importance
            print("Task importance updated.")
        else:
            print("Invalid task number.")


def main():
    todo_list = TodoList()

    while True:
        print("\n===== Todo List Menu =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Change Task Status")
        print("5. Change Task Importance")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_description = input("Enter the task description: ")
            task = Task(task_description)
            todo_list.add_task(task)
            print("Task added.")
        elif choice == "2":
            task_number = int(input("Enter the task number to remove: "))
            try:
                todo_list.remove_task(todo_list.get_tasks()[task_number - 1])
                print("Task removed.")
            except IndexError:
                print("Invalid task number.")
        elif choice == "3":
            print("\n===== Tasks =====")
            todo_list.display_tasks()
        elif choice == "4":
            task_number = int(input("Enter the task number to change status: "))
            new_status = input("Enter the new status for the task: ")
            todo_list.change_task_status(task_number, new_status)
        elif choice == "5":
            task_number = int(input("Enter the task number to change importance: "))
            new_importance = input("Enter the new importance for the task: ")
            todo_list.change_task_importance(task_number, new_importance)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


#The application is functionnal but i want to add more features 
# I want that the users can evaluate the progress of the task like 'in progress' 'started' 
# I want that the users can classify the importance of the task like 'can be done later or after' 'should be done immediately' 