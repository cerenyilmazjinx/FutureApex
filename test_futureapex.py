# test_futureapex.py
"""
Tests for FutureApex module.
"""

import unittest
from futureapex import FutureApex

class TestFutureApex(unittest.TestCase):
    """Test cases for FutureApex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FutureApex()
        self.assertIsInstance(instance, FutureApex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FutureApex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
