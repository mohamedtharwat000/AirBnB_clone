#!/use/bin/python3
"""unittest for the Review Class"""
import unittest
from models.review import Review
from datetime import datetime
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models import storage


class TestReview(unittest.TestCase):
    """The start of unittest for Review Class"""

    def test_attributes(self):
        """test the initial values for every attribute in the class"""

        review = Review()
        self.assertEqual(review.place_id, '')
        self.assertEqual(review.user_id, '')
        self.assertEqual(review.text, '')

    def test_to_dict_method(self):
        """test to_dict method that is from the BaseModel class"""

        review = Review()
        review_dict = review.to_dict()
        self.assertTrue("__class__" in review_dict)
        self.assertTrue("created_at" in review_dict)
        self.assertTrue("updated_at" in review_dict)
        self.assertEqual(review_dict["__class__"], "Review")
        tmp_1 = review.created_at.isoformat()
        tmp_2 = review.updated_at.isoformat()
        self.assertEqual(review_dict["created_at"], tmp_1)
        self.assertEqual(review_dict["updated_at"], tmp_2)

    def test_set_values(self):
        """assign values to the attributes of a Review
            and check if they are set correctly
        """

        review = Review()
        review.place_id = 'ABC-123'
        review.user_id = 'XYZ-123'
        review.text = 'It\'s a wonderful palce, the kids loved it.'
        self.assertEqual(review.place_id, 'ABC-123')
        self.assertEqual(review.user_id, 'XYZ-123')
        tmp_txt = 'It\'s a wonderful palce, the kids loved it.'
        self.assertEqual(review.text, tmp_txt)


class TestUserAndConsole(unittest.TestCase):
    """Test the Review class with the console"""

    def setUp(self):
        """setting up the console to use it"""

        self.console = HBNBCommand()

    def test_update_review(self):
        """test review values before and after updating"""

        review = Review()
        review.place_id = 'ABC-456'
        review.user_id = 'XYZ-456'
        review.text = 'Good place, but the kitchen wasn\'t good.'

        # we will change the place_id from ABC-456 to DEF-789
        self.console.onecmd(f'update Review {review.id} place_id "DEF-789"')
        self.assertEqual(review.place_id, 'DEF-789')

        # user_id from XYZ-456 to GHI-789
        self.console.onecmd(f'update Review {review.id} user_id "GHI-789"')
        self.assertEqual(review.user_id, 'GHI-789')

        # text from Good place..... to Great!!!
        temp_text = 'Great!!!'
        self.console.onecmd(f'update Review {review.id} text "{temp_text}"')
        self.assertEqual(review.text, temp_text)
