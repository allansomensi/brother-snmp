import os
from sys import exit
import platform


def close():
    os.system("exit")
    exit(0)


def clear():
    if platform.system() == "Windows":
        os.system("cls")

    else:
        os.system("clear")
