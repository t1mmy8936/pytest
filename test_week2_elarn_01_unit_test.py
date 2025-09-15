import unittest
import sys
import os

# Add the parent directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from week2_elarn_01_unit_test import calculate_discount

class TestCalculateDiscount(unittest.TestCase):
    """
    Unit tests for the calculate_discount function, which determines discount percentage based on loyalty points.
    The tests cover the following cases:
    - High loyalty points (1000+) providing 20% discount
    - Medium loyalty points (500-999) providing 10% discount
    - Low loyalty points (0-499) providing 0% discount
    - Boundary values between discount tiers (499/500 and 999/1000)
    - Negative loyalty points (edge case)
    Each test method validates that the calculate_discount function returns the expected
    discount percentage for various inputs within each range.
    """
    
    def test_high_loyalty_points(self):
        """Test that 1000 or more loyalty points gives 20% discount"""
        self.assertEqual(calculate_discount(1000), 20)
        self.assertEqual(calculate_discount(1500), 20)
    
    def test_medium_loyalty_points(self):
        """Test that 500-999 loyalty points gives 10% discount"""
        self.assertEqual(calculate_discount(500), 10)
        self.assertEqual(calculate_discount(750), 10)
        self.assertEqual(calculate_discount(999), 10)
    
    def test_low_loyalty_points(self):
        """Test that 0-499 loyalty points gives 0% discount"""
        self.assertEqual(calculate_discount(0), 0)
        self.assertEqual(calculate_discount(250), 0)
        self.assertEqual(calculate_discount(499), 0)
    
    def test_boundary_values(self):
        """Test boundary values between discount tiers"""
        self.assertEqual(calculate_discount(499), 0)
        self.assertEqual(calculate_discount(500), 10)
        self.assertEqual(calculate_discount(999), 10)
        self.assertEqual(calculate_discount(1000), 20)
    
    def test_negative_points(self):
        """Test with negative loyalty points (edge case)"""
        self.assertEqual(calculate_discount(-100), 0)

if __name__ == '__main__':
    unittest.main()