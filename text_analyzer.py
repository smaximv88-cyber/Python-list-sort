import string
from collections import Counter

def func_text (text):
    text = text.lower()
    text_ignor = ['the', 'and', 'a', 'in', 'on', 'at', 'to', 'for', 'of', 'is', 'are']
    new_text = ''.join(char for char in text if char not in string.punctuation)
    new_text = new_text.split(" ")
    filter_words = [word for word in new_text if word not in text_ignor]
    word_count = Counter(filter_words)
    return {word: count for word, count in word_count.items() if count > 1}

text =  "This this book book is designed specifically with programming beginners beginners beginners in mind. Basic programming concepts — such as expressions, variables, loops, decisions, lists, dictionaries, sets, functions, files."

print(func_text(text))
