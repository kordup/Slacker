import os 
import sys
import re
import linecache
from clear import clear
from logo import logo, BC


def menu():
    clear()
    logo()
    m4 = print("Denial of Service")
    mitems = ("TorsHammer", "KingKor", "SYN Flooder", "The Hulk")
    for idx, i in enumerate(mitems, start=1):
        print( BC.G + " [" + BC.F + str(idx) + BC.G + "] " + i)
    else:
        print("------------------------------------------")
        print(" [" + BC.F + "*" + BC.G + "] Main Menu")
        print(" [" + BC.F + "0" + BC.G + "] Exit")
        m4 = input("")
    if m4 == "1":
        clear()
        print("I am one")
        menu()
    elif m4 == "2":
        clear()
        print("I am Two")
        menu()
    elif m4 == "3":
        clear()
        print("I am Three")
        menu()
    elif m4 == "*":
        quit
    elif m4 == "0":
        sys.exit()