import os 
import sys
import re
import time
import linecache
from clear import clear
from logo import logo, BC

global menuz
menuz = ["Set Target", "Use A Proxy", "Clear Proxy", "Scan", "Main Menu"]
global count
count = 1
for i in menuz:
    print( BC.G + "[" + BC.F + str(count) + BC.G + "] " + i)
    count += 1