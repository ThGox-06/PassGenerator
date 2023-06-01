import pyperclip
from pass_gen import *


def copy_to_clipboard(a):
    pyperclip.copy(str(a))


def ask_copy():
    asking = input("Do you want to copy the password? Y/N: ")
    print("-" * 40)
    if asking in ("s", "si", "y", "yes"):
        copy_to_clipboard(''.join(password))
