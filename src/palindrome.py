import string 

def is_palindrome(word):
    word = word.lower()
    word = word.translate(str.maketrans('', '', string.punctuation))
    word = word.replace(" ", "")
    return word==word[::-1]

