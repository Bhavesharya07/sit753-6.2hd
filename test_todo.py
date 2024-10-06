import unittest
from io import StringIO
import sys

# Assuming the functions are in a file named todo.py, import them
from todo import add_task, view_tasks, delete_task, tasks

class TestTodoList(unittest.TestCase):

    def setUp(self):
        """Reset tasks before each test."""
        global tasks
        tasks = []

    def test_add_task(self):
        """Test adding a task."""
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            add_task("Test task")
            self.assertIn("Test task", tasks)
            self.assertEqual(fake_stdout.getvalue().strip(), "Task 'Test task' added.")

    def test_view_tasks_empty(self):
        """Test viewing tasks when empty."""
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            view_tasks()
            self.assertEqual(fake_stdout.getvalue().strip(), "No tasks available.")

    def test_delete_task(self):
        """Test deleting a task."""
        add_task("Test task")
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            delete_task(1)  # Assuming we want to delete the first task
            self.assertNotIn("Test task", tasks)
            self.assertEqual(fake_stdout.getvalue().strip(), "Task 'Test task' deleted.")

    def test_delete_invalid_task(self):
        """Test deleting an invalid task."""
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            delete_task(1)  # Try to delete from empty tasks
            self.assertEqual(fake_stdout.getvalue().strip(), "No tasks available.")

if __name__ == "__main__":
    unittest.main()
