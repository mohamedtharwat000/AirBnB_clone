#!/use/bin/python3
"""unittest for the User Class"""
import unittest
from models.user import User
from datetime import datetime
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models import storage


class TestUser(unittest.TestCase):
    """The start of unittest for User Class"""

    def test_attributes(self):
        """test the initial values for every attribute in the class"""

        user = User()
        self.assertEqual(user.email, '')
        self.assertEqual(user.password, '')
        self.assertEqual(user.first_name, '')
        self.assertEqual(user.last_name, '')

    def test_to_dict_method(self):
        """test to_dict method that is from the BaseModel class"""

        user = User()
        user_dict = user.to_dict()
        self.assertTrue("__class__" in user_dict)
        self.assertTrue("created_at" in user_dict)
        self.assertTrue("updated_at" in user_dict)
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["created_at"], user.created_at.isoformat())
        self.assertEqual(user_dict["updated_at"], user.updated_at.isoformat())

    def test_set_values(self):
        """assign values to the attributes of a User
            and check if they are set correctly
        """

        user = User()
        user.email = 'test@email.com'
        self.assertEqual(user.email, 'test@email.com')

        user.password = 'test_password'
        self.assertEqual(user.password, 'test_password')

        user.first_name = 'Ahmed'
        self.assertEqual(user.first_name, 'Ahmed')

        user.last_name = 'Ali'
        self.assertEqual(user.last_name, 'Ali')

    def test_reload_method(self):
        """test reload method which is from FileStorage Class"""

        user = User()

        user.first_name = 'Salah'
        user.last_name = 'Gamal'

        user.save()
        storage.reload()

        reloaded_user = storage.all()[f'{user.__class__.__name__}.{user.id}']

        self.assertEqual(reloaded_user.first_name, 'Salah')
        self.assertEqual(reloaded_user.last_name, 'Gamal')


class TestUserAndConsole(unittest.TestCase):
    """Test the user class with the console"""

    def setUp(self):
        """setting up the console to use it"""

        self.console = HBNBCommand()

    def test_update_user(self):
        """test user values before and after updating"""

        user = User()
        user.email = 'test@email.com'
        user.password = 'test_password'
        user.first_name = 'Ahmed'
        user.last_name = 'Ali'

        # we will change the first_name from Ahmed to Mohammed
        self.console.onecmd(f'update User {user.id} first_name "Mohammed"')
        self.assertEqual(user.first_name, 'Mohammed')

        # email from test@email.com to test2@mail.net
        self.console.onecmd(f'update User {user.id} email "test2@mail.net"')
        self.assertEqual(user.email, 'test2@mail.net')
