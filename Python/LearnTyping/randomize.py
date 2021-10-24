# List of website for learning to type code
# https://www.how-to-type.com/typing-practice/programming/
# https://typing.io/lessons

# General typing
# https://typing.works/
# https://typings.gg/

# Paste the below output into keybr: https://www.keybr.com/

from json import load
from random import shuffle
import pyperclip

with open('keywords.json', 'r') as kws:
    kw_ls = load(kws)

shuffle(kw_ls)

print(f'Your clipboard:\n==============\n{pyperclip.paste()}')

print(f'Copied shuffled kw to your clipboard:\n==============\n{" ".join(kw_ls)}')
