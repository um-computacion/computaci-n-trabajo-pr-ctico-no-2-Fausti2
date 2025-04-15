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
    def test_frases_no_palindrome(self):
        self.assertFalse(is_palindrome("La ruta no es natural"))
        self.assertFalse(is_palindrome("escribir un texto "))
        self.assertFalse(is_palindrome(" me gusta la computadora "))
    def test_casos_edge(self):
        self.assertTrue(is_palindrome("A Santa at NASA"))
        self.assertTrue(is_palindrome("¿Cómo es tu nombre?"))
        self.assertTrue(is_palindrome("No lemon, no melon"))
        self.assertTrue(is_palindrome("5458989"))
    
if __name__ == '__main__':
    unittest.main() 