class Task:
    def __init__(self, id, name, description, ):
        self.__id = id
        self.__name = name
        self.__description = description

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name


class Subtask(Task):
    # have comlex task id
    def __init__(self, id, name, description, status, parent_id):
        super().__init__(id, name, description, status)
        self.parent_id = parent_id


class ComplexTask(Task):
    # contains list of subtasks
    def __init__(self):
        self.subtasks = []


class TaskManager:
    id_series = 0

    def __init__(self):
        self.tasks = {}
        self.subtasks = {}
        self.complex_tasks = {}

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
            parent_task = self.tasks.get(parent_id)
            self.complex_tasks[parent_id] = ComplexTask(parent_id, par_task.get_name(), par_task.get_description(),
                                                          [current_id], parent_task.get_status())
            del self.tasks[parent_id]
        elif parent_id in self.complex_tasks:
            parent_task = self.complex_tasks.get(parent_id)
            complex_subtasks = parent_task.get_subtasks()
            compl_subtasks.append(current_id)


    def create_complex_task(self, complex_task):
        current_id = self.__get_and_increment_id()
        new_task = ComplexTask(current_id, name, description, subtasks)
        self.complex_tasks[current_id] = new_task
        return new_task

    def get_tasks(self):
        return list(self.tasks)

    def get_subtasks(self):
        return list(self.subtasks)

    def get_complex_tasks(self):
        return list(self.complex_tasks)

    def get_tasks_by_id(self, id):
        return self.tasks.get(id)

    def get_subtasks_by_id(self, id):
        return self.subtasks.get(id)

    def get_complex_tasks_by_id(self, id):
        return self.complex_tasks.get(id)

    def remove_tasks(self):
        self.tasks.clear()

    def remove_subtasks(self):
        for id in list(self.subtasks):
            self.remove_subtask_by_id(id)

    def remove_complex_tasks(self):
        for id in list(self.complex_tasks):
            self.remove_complex_task_by_id(id)

    def remove_task_by_id(self, id):
        del self.tasks[id]

    def remove_subtask_by_id(self, id):
        subtask = self.get_subtasks_by_id(id)
        parent_task = self.get_complex_tasks_by_id(par_id)
        del self.subtasks[id]
        parent_subtasks = parent_task.get_subtasks()
        parent_subtasks.remove(id)
        if not parent_task_subtasks:
            del self.complex_tasks[par_id]

    def remove_complex_task_by_id(self, id):
        complex_task = self.get_complex_tasks_by_id(id)
        for id in complex_task.get_subtasks():
            del self.subtasks[sub_tasks_id]
        del self.complex_tasks[id]

    def update_status(self,id,st):
        if id in self.tasks:
            task = self.get_tasks_by_id(id)
            task.update_status(st)
        elif id in self.__complex_tasks:
            complex_task = self.get_complex_tasks_by_id(id)
            complex_task.update_status(st)
            for id in complex_task.get_subtasks():
                subtask = self.get_subtasks_by_id(subtask_id)
                subtask.update_status(st)
        else:
            subtask = self.get_subtasks_by_id(id)
            subtask.update_status(st)

def main():
    task1 = Task(1,'buy','fruit')
    task2 = Task(2, 'sell', 'car')
    task3 = Task(3, 'learn', 'Python')
    manager = TaskManager()
    manager.create_task(task1,'04.05.2022')
    manager.create_task(task2,'04.05.2022 ')
    manager.create_task(task3,'04.05.2022 ')
    print(manager.get_tasks())
    print(manager.get_tasks_by_id(1))
    manager.remove_tasks()





if __name__ == "__main__":
    main()

