from os import system as sys_cmd
from platform import system


def clean():
    if system() == 'Windows':
        sys_cmd('cls')
    elif system() == 'Linux':
        sys_cmd('clear')
