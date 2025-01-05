"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class TestCalc(SimpleTestCase):
    """Function to test calc"""

    def test_add_numbers(self):
        """Test adding two number"""

        x = 2
        y = 3

        res = calc.add(x,y)

        self.assertEquals(res, 5)

    def test_subtract_numbers(self):
        """Test subtracting two number"""

        x = 3
        y = 2

        res = calc.subtract(x,y)

        self.assertEquals(res, 1)