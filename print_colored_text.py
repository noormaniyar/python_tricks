"""
    Did you know that you can add color to your code using Python
    and ANSI escape codes? Below, I created a class of codes and
    applied it to the code that I printed out.
"""

class Colors():
    Black = '\033[30m'
    Green = '\033[32m'
    Blue = '\033[34m'
    Magenta = '\033[35m'
    Red = '\033[31m'
    Cyan = '\033[36m'
    White = '\033[37m'
    Yellow = '\033[33m'

print(f'{Colors.Red} Warning Message: {Colors.Green} Love Don\'t live here anymore')