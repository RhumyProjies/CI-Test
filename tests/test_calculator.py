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

    def test_add_negative_numbers(self):
        """Test adding negative numbers"""
        result = self.calc.add(-1, -1)
        self.assertEqual(result, -2)
    
    def test_add_zero(self):
        """Test adding zero"""
        result = self.calc.add(5, 0)
        self.assertEqual(result, 5)

    def test_subtract_numbers(self):
        """Test subtracting two positive numbers"""
        result = self.calc.add(5, 3)
        self.assertEqual(result, 2)
        
    def test_multiply_numbers(self):
        """Test multiplying two positive numbers"""
        result = self.calc.add(2, 3)
        self.assertEqual(result, 6)
        
    def test_divide_numbers(self):
        """Test dividing two positive numbers"""
        result = self.calc.add(10, 2)
        self.assertEqual(result, 5)        