import uuid


class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.id = str(uuid.uuid4())
        self.status = False


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def remove(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                return True
        return False

    def completed(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.status = True
                return True
        return False

    def show_tasks(self):
        for task in self.tasks:
            print(task.id, task.name, task.description)

