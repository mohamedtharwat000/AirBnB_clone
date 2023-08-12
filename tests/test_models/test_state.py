#!/use/bin/python3
"""unittest for the State Class"""
import unittest
from models.state import State
from datetime import datetime
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models import storage


class TestState(unittest.TestCase):
    """The start of unittest for State Class"""

    def test_attributes(self):
        """test the initial values for every attribute in the class"""

        state = State()
        self.assertEqual(state.name, '')

    def test_to_dict_method(self):
        """test to_dict method that is from the BaseModel class"""

        state = State()
        state_dict = state.to_dict()
        self.assertTrue("__class__" in state_dict)
        self.assertTrue("created_at" in state_dict)
        self.assertTrue("updated_at" in state_dict)
        self.assertEqual(state_dict["__class__"], "State")
        tmp_1 = state.created_at.isoformat()
        tmp_2 = state.updated_at.isoformat()
        self.assertEqual(state_dict["created_at"], tmp_1)
        self.assertEqual(state_dict["updated_at"], tmp_2)

    def test_set_values(self):
        """assign values to the attributes of a State
            and check if they are set correctly
        """

        state = State()
        state.name = 'New York'
        self.assertEqual(state.name, 'New York')


class TestUserAndConsole(unittest.TestCase):
    """Test the State class with the console"""

    def setUp(self):
        """setting up the console to use it"""

        self.console = HBNBCommand()

    def test_update_state(self):
        """test state values before and after updating"""

        state = State()
        state.name = 'Las Vegas'

        # we will change the state from Las Vegas to Chicago
        self.console.onecmd(f'update State {state.id} name "Chicago"')
        self.assertEqual(state.name, 'Chicago')
