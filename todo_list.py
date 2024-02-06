class Task:
    def __init__(self, description, status="Open", importance="Normal", progress="Not started"):
        self.description = description
        self.status = status
        self.importance = importance
        self.progress = progress

    def __str__(self):
        return f"{self.description} [Status: {self.status}, Importance: {self.importance}, Progress: {self.progress}]"


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

    def change_task_progress(self, task_number, new_progress):
        if 1 <= task_number <= len(self.tasks):
            task = self.tasks[task_number - 1]
            task.progress = new_progress
            print("Task progress updated.")
        else:
            print("Invalid task number.")
