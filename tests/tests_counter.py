import unittest
from counter import count_words

class TestWordCounter(unittest.TestCase):

    def test_count_words(self):
        # Test with regular input
        self.assertEqual(count_words("This is a test sentence."), 5)
        
        # Test with empty input
        self.assertEqual(count_words(""), 0)
        
        # Test with multiple spaces
        self.assertEqual(count_words("   Hello    world   "), 2)
        
        # Test with one word
        self.assertEqual(count_words("Hello"), 1)

if __name__ == "__main__":
    unittest.main()
