import unittest
#from src.palindrome import is_palindrome 
class testpalindrome (unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("hola"))
        self.assertFalse(is_palindrome("Mundo")) 
    

if __name__ == '__main__':
    unittest.main() 