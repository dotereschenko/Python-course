import unittest
from task_manager import TaskManager

class Test(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_create_task(self):
        name="food"
        description = "icecream"
        task = self.manager.create_task(name,description)
        self.assertEqual(task.get_name(), name)
        self.assertEqual(task.get_description(), description)

    def test_create_subtask(self):
        name="food"
        description = "icecream"
        name1 = "mall"
        description1 = "shoe repair"
        task = self.manager.create_task(name, description)
        subtask = self.manager.create_subtask(name1, description1, task.get_id())
        self.assertIsNotNone(self.manager.get_subtasks)
        self.assertEqual(len(self.manager.get_tasks()), 0)
        self.assertIsNotNone(self.manager.get_complex_tasks)

    def test_create_complex_task(self):
        name="food"
        description = "icecream"
        subtask = self.manager.create_subtask(name, description, 0)
        complex = self.manager.create_complex_task(name, description,subtask.get_id())
        subtask = self.manager.create_subtask('s1', 's1d', subtask.get_id())
        self.assertIsNotNone(complex)

    def test_remove_by_id(self):
        name="food"
        description = "icecream"
        name1 = "mall"
        description1 = "shoe repair"
        task = self.manager.create_task(name, description)
        task1 = self.manager.create_task(name, description)
        subtask = self.manager.create_subtask(name1, description1, task1.get_id())
        self.manager.remove_task_by_id(task.get_id())
        self.assertEqual(self.manager.get_tasks_by_id(task.get_id()), None)
        self.manager.remove_subtask_by_id(subtask.get_id())
        self.assertEqual(self.manager.get_subtasks_by_id(subtask.get_id()), None)
        self.assertEqual(self.manager.get_complex_tasks_by_id(task1.get_id()), None)



if __name__ == "__main__":
    unittest.main()