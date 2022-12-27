class Task:
    def __init__(self, id, name, description, status="doing"):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__status = status

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_status(self):
        return self.__status

    def update_status(self, new):
        self.__status = new


class Subtask(Task):
    # have comlex task id
    def __init__(self, id, name, description, parent_id, status="doing"):
        super().__init__(id, name, description, status)
        self.__parent_id = parent_id

    def parent(self):
        return self.__parent_id


class ComplexTask(Task):
    # contains list of subtasks
    def __init__(self, id, name, description, subtasks, status="doing"):
        super().__init__(id, name, description, status)
        self.__subtasks = subtasks

    def get_subtasks(self):
        return self.__subtasks


class TaskManager:
    id_series = 0

    def __init__(self):
        self.tasks = {}
        self.subtasks = {}
        self.complex = {}

    def __get_and_increment_id(self):
        next_id_value = TaskManager.id_series
        TaskManager.id_series += 1
        return next_id_value

    def create_task(self, name, description):
        current_id = self.__get_and_increment_id()
        new_task = Task(current_id, name, description)
        self.tasks[current_id] = new_task
        return new_task

    def create_subtask(self, name, description, parent_id):
        current_id = self.__get_and_increment_id()
        new_subtask = Subtask(current_id, name, description, parent_id)
        self.subtasks[current_id] = new_subtask
        if parent_id in self.tasks:
            parent = self.tasks.get(parent_id)
            self.complex[parent_id] = ComplexTask(parent_id, parent.get_name(), parent.get_description(),
                                                  [current_id], parent.get_status())
            del self.tasks[parent_id]
        elif parent_id in self.complex:
            parent = self.complex.get(parent_id)
            complex_subtasks = parent.get_subtasks()
            complex_subtasks.append(current_id)

        return new_subtask

    def create_complex_task(self, name, description, subtask):
        current_id = self.__get_and_increment_id()
        new_complex = ComplexTask(current_id, name, description, subtask)
        self.complex[current_id] = new_complex
        return new_complex

    def get_tasks(self):
        return list(self.tasks)

    def get_subtasks(self):
        return list(self.subtasks.values())

    def get_complex_tasks(self):
        return list(self.complex.values())

    def get_tasks_by_id(self, id):
        return self.tasks.get(id)

    def get_subtasks_by_id(self, id):
        return self.subtasks.get(id)

    def get_complex_tasks_by_id(self, id):
        return self.complex.get(id)

    def remove_tasks(self):
        return self.tasks.clear()

    def remove_subtasks(self):
        return self.subtasks.clear()

    def remove_complex_tasks(self):
        for id in list(self.complex):
            self.remove_complex_task_by_id(id)

    def remove_task_by_id(self, id):
        if id not in self.tasks:
            print("No task with this ID")
        else:
            del self.tasks[id]

    def remove_subtask_by_id(self, id):
        if id not in self.subtasks:
            print("No subtask with  this id")
        else:
            subtask = self.get_subtasks_by_id(id)
            par_id = subtask.parent()
            par_task = self.get_complex_tasks_by_id(par_id)
            del self.subtasks[id]
            par_task_subtasks = par_task.get_subtasks()
            par_task_subtasks.remove(id)
            if len(par_task_subtasks) == 0:
                del self.complex[par_id]

    def remove_complex_task_by_id(self, id):
        if id not in self.complex:
            print("No complex task with with this id")
        else:
            complex = self.get_complex_tasks_by_id(id)
            for sub in complex.get_subtasks():
                del self.subtasks[sub]
            del self.complex[id]

    def print_task(self, task):
        # print(task.__class__.__name__)
        print("===================================")
        print("ID:", task.get_id(), end="\n")
        print("task:", task.get_name(), end="\n")
        print("description:", task.get_description(), end="\n")
        print("status:", task.get_status(), end="\n")
        print("===================================")

    def print_all(self):
        print("tasks:", self.tasks, end="\n")
        print("subtasks:", self.subtasks, end="\n")
        print("complex:", self.complex, end="\n")


def main():
    task = Task(0, "groceries", "banana,apple,wine", 'doing')
    task2 = Subtask(0, "change tyres", "Winter protection", task.get_id())
    manager = TaskManager()
    task = manager.create_task(task.get_name(), task.get_description())
    task2 = manager.create_subtask(task2.get_name(), task2.get_description(), task2.parent())
    task.update_status("completed")
    manager.remove_task_by_id(3)
    manager.remove_complex_task_by_id(4)
    manager.remove_subtask_by_id(4)
    manager.print_task(task)
    manager.print_task(task2)
    manager.print_all()



if __name__ == "__main__":
    main()
