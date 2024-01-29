# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:05:00 2024

@author: joali
"""

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

def main():
    todo_list = TodoList()

    while True:
        print("\n===== Todo List Menu =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("Task added.")
        elif choice == "2":
            task = input("Enter the task to remove: ")
            try:
                todo_list.remove_task(task)
                print("Task removed.")
            except ValueError:
                print("Task not found.")
        elif choice == "3":
            print("\n===== Tasks =====")
            todo_list.display_tasks()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()



#The application is functionnal but i want to add more features 
# I want that the users can evaluate the progress of the task like 'in progress' 'started' 
# I want that the users can classify the importance of the task like 'can be done later or after' 'should be done immediately' 