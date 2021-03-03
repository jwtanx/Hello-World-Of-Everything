# Last updated: Wed, March 03, 2021 - 09:38

"""
Just in case you wanna rename all of your image creation data file from alphabetical format in to numeric format
"""

import os

print(os.listdir())
text = 'ABC'

for f in os.listdir():
	if f == 'rename.py':
		continue
	new = f.replace(text, '')
	os.rename(f, new)
