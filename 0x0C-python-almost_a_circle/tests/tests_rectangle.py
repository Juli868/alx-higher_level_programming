import unittest
from models.rectangle import Rectangle
from models.base import Base
class TextBAse(unittest.TestCase):
    def test_width_setter(self):
        """Test if it sets the value correcty defined"""
        new_rectangle = Rectangle(2, 4)
        """
        result = {'_Rectangle__id': 1, 
                '_Rectangle__width': 2, 
                '_Rectangle__height': 4, 
                '_Rectangle__x': 0, 
                '_Rectangle__y': 0}
        compare = vars(new_rectangle)
        self.assertDictEqual(result, compare)
        """
        self.assertIsInstance(new_rectangle, Rectangle)
