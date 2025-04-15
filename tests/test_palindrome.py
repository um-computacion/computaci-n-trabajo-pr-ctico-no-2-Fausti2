import unittest
#from src.palindrome import is_palindrome 
class testpalindrome (unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("hola"))
        self.assertFalse(is_palindrome("Mundo")) 
    def test_frases_palindrome(self):
        self.assertTrue(is_palindrome("La ruta natural"))
        self.assertTrue(is_palindrome("Amo la pacífica paloma"))
        self.assertTrue(is_palindrome("La ruta natural"))



if __name__ == '__main__':
    unittest.main() 