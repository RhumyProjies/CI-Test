"""
Test suite for the Calculator class
"""

import unittest
import sys
import os

# Add the src directory to the path so we can import our calculator
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for Calculator class"""
    
    def setUp(self):
        """Set up test fixtures before each test method"""
        self.calc = Calculator()
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers"""
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)
        