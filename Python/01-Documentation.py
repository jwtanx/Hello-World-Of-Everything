# Referece: https://www.youtube.com/watch?v=URBSvqib0xw
"""
$ python -m pydoc

$ python -m pydoc -k <keyword>
    Search for a keyword in the synopsis lines of all available modules.
    NOTE:   To view page by page - press SPACE
            To quit the documentation - press q

$ python -m pydoc -n <hostname>
    Start an HTTP server with the given hostname (default: localhost).

$ python -m pydoc -p <port>
    Start an HTTP server on the given port on the local machine.  Port
    number 0 can be used to get an arbitrary unused port.

$ python -m pydoc -b
    Start an HTTP server on an arbitrary unused port and open a Web browser
    to interactively browse documentation.  This option can be used in
    combination with -n and/or -p.

$ python -m pydoc -w <name> ...
    Write out the HTML documentation for a module to a file in the current
    directory.  If <name> contains a '\', it is treated as a filename; if
    it names a directory, documentation is written for all the contents.
"""

############################################################
# Reference: https://realpython.com/documenting-python-code/
# This is a basic comment
# PEP8: comments should have a maximum length of 72 characters

# Tagging: to label specific sections of code (improvement or issue)
# Example: BUG, FIXME, and TODO.
"""
# TODO: Add condition for when val is None
"""

# This line here is the brief function of the function below.
def say_hello(name):
    """Documentation Title
    This is the function of ...
    :param name: string
    """
    return(f"Hello {name}")

print(say_hello('World'))

# Another way of documenting it
say_hello.__doc__ = "This is a function of..."

# In python console, this is how you get the documentation
"""
>>> help(say_hello)
NOTE: Above code only available in python console
"""

############################################################
# Reference: https://www.journaldev.com/22892/python-help-function
# This is how you can go through the entire python file doc
"""
# Step 1:
>>> exec(open(r"C:/Users/<USERNAME>/Project/HelloWorld.py").read())

# Step 2:
>>>  globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__warningregistry__': {'version': 0}, 'say_hello': <function say_hello at 0x000001853B86E040>}

# Step 3:
>>> help('HelloWorld.say_hello')
"""

############################################################
# Last updated: 030221 15:30