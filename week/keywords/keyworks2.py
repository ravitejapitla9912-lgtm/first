"""Write	a	program	that	checks	whether	a	user-input	word	is	a	Python	keyword	or	not,	using"""	

import keyword

word = input("Enter a word: ")

if keyword.iskeyword(word):
    print(word, "is a Python keyword")
else:
    print(word, "is not a Python keyword")
"""Enter a word: def
def is a Python keyword"""