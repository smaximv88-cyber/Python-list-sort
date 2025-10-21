from collections import Counter
text = 'Hello World'
text = text.lower().replace(' ','')
char_count = Counter(text)
print(dict(char_count))
