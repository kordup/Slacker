import os
from subprocess import call


def clear():  
    _ = call('clear' if os.name =='posix' else 'cls') 