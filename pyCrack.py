## Written by Korrupt             ##
## Just for fun :)                ##
## Scripting is still in progress ##
from subprocess import call
import itertools
import string
import os
import time
import hashlib
import getopt
import sys
from typing import List, Tuple


num = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}'
y = ""
counted = 1
## Test Hashes With The Below ##
sha256 = "cd0047a42d8f9^C222ba25dbd7d9b90401dc536c5d2414bd4c71c9ede4732e7c" #64
sha1 =  "657f971538ff4d6316f6ef2935e7d3ea611d7851" #40
md11 = "9f9de00ac5f1513cfa23e5823a0b46b6" # 32


class BC:
    G = '\033[92m'

    F = '\033[91m'

##Set up clear terminal/screen
def clear():  
    _ = call('clear' if os.name =='posix' else 'cls') 

	
##Main hash check function
def md52(a, b):
	counted = 1
	for c in itertools.product(num, repeat=a):
		hsh = b
		pw = y+''.join(c)
		if hsh == 1:		
			hassh = hashlib.md5(pw.encode()).hexdigest()
		elif hsh == 2:
			hassh = hashlib.sha1(pw.encode()).hexdigest()
		elif hsh == 3:
			hassh = hashlib.sha256(pw.encode()).hexdigest()
		else:
			clear()
			print(BC.F + "You're using me wrong!!!")
			print("")
		sys.stdout.write("\033[F")
		sys.stdout.write("\033[F")
		sys.stdout.write("\033[F")
		sys.stdout.write("\033[F")
		sys.stdout.write("\033[F")
		sys.stdout.write("\033[F")
		sys.stdout.write("\033[F")
		sys.stdout.write("\033[F")
		sys.stdout.write("\033[F")
		sys.stdout.write("\033[F")
		sys.stdout.write("\033[F")
		logo()
		print(BC.G + "[" + BC.F + "*" + BC.G + "]  Hash String: %s " %(md5))
		print(BC.G + "[" + BC.F + "*" + BC.G + "]  Attempts: %s" % (counted))
		print(BC.G + "[" + BC.F + "*" + BC.G + "]  Text: %s " %(pw))
		print(BC.G + "[" + BC.F + "*" + BC.G + "]  Hashed: %s " %(hassh))
		counted += 1
		if hassh == md5:
			clear()
			logo()
			print(BC.G + "[" + BC.F + "*" + BC.G + "]  Hash String: %s " %(md5))
			print(BC.G + "[" + BC.F + "*" + BC.G + "]  Attempts: %s" % (counted))
			print(BC.G + "[" + BC.F + "*" + BC.G + "]  Text: %s " %(pw))
			print(BC.G + "[" + BC.F + "*" + BC.G + "]  Hashed: %s " %(hassh))
			print("")
			print(BC.G + "[" + BC.F + "*" + BC.G + "] Hash [ %s ] was found as: %s " % (md5, pw))
			print("")
			return False
	md52(7)
	md52(8)
	md52(9)
	md52(10)
	md52(11)
	md52(12)
	md52(13)
	md52(14)
	md52(15)
	md52(16)



##Help menu
thisStr = sys.argv[0]
USAGE = BC.G + "Usage: python " + str(thisStr) + " -h             		: Displays this Menu"
USAGE1 = "       python " + str(thisStr) + " -m <hash> 				: Pretty self explanitory"
USAGE2 = ""
USAGE3 = "MD5:" + BC.F + "		   -m <hash>"
USAGE4 = BC.G + "SHA1:" + BC.F + "		   -s <hash>"
USAGE5 = BC.G + "SHA256:" + BC.F + "		   -S <hash>"
USAGE6 = BC.G + "		    Be sure to use Python3"
#VERSION = f"{sys.argv[0]} version 1.0.0"




def usages():       
            	clear() 
            	logo()
            	print(USAGE)
            	print(USAGE1)
            	print(USAGE2)
            	print(USAGE3)
            	print(USAGE4)
            	print(USAGE5)
            	print(USAGE6)


##Start Screen
def logo():
            print(BC.G + "pyCrack by")
            print(BC.F + "888888 888888    db    8b    d8     88\"\"Yb  dP\"Yb   dP\"Yb  888888 ")
            print("  88   88__     dPYb   88b  d88     88__dP dP   Yb dP   Yb   88   ")
            print("  88   88\"\"    dP__Yb  88YbdP88     88\"Yb  Yb   dP Yb   dP   88   ")
            print("  88   888888 dP\"\"\"\"Yb 88 YY 88     88  Yb  YbodP   YbodP    88 ")
            print(BC.G + "  Korrupt")
            print("")
def starting():
            clear()
            logo()
            print("Cracking: %s       |" % (md5))
            sys.stdout.write("\033[F")
            time.sleep(.5)
            print(BC.G + "Cracking: %s >     |" % (md5))
            sys.stdout.write("\033[F")
            time.sleep(.25)
            print(BC.G + "Cracking: %s >>    |" % (md5))
            sys.stdout.write("\033[F")
            time.sleep(.25)
            
            print(BC.G + "Cracking: %s >>>   |" % (md5))
            sys.stdout.write("\033[F")
            time.sleep(.25)
            print(BC.G + "Cracking: %s >>>>  |" % (md5))
            sys.stdout.write("\033[F")
            time.sleep(.25)
            print(BC.G + "Cracking: %s >>>>> |" % (md5))
            sys.stdout.write("\033[F")
            time.sleep(.25)
            print(BC.G + "Cracking: %s >>>>>>|" % (md5))
            sys.stdout.write("\033[F")
            time.sleep(.25)


    
def agr():  
    global opt
    global opts
    opts = ""
    global help
    help = ""

    global md
    md = ""
    
    global md2
    md2 = ""
    
    global sh1
    sh1 = ""

    global sh2
    sh2 = ""
    
    global b
    b = ""

    global e
    e = ""
    
    argv = sys.argv[1:]  
    
    try:  
        opts, args = getopt.getopt(argv, "ha:m:s:S:b:e:")  
        
    except:
        clear()  
        print("Error")  
        print(usages())
        print("")
        

    for opt, arg in opts:
        if opt in ['-h']:  
            #help = 1
            print(usages())


        if opt in ['-m']:  
            md = arg
            if len(md) != 32:
            	sha = len(md)
            	print(BC.G + "The string provided is " + BC.F + str(sha) + BC.G + " characters long, MD5 hashes are 32 characters. Are you sure this is a MD5?")
            	if sha == 64:
            		print(BC.F + "SHA256" + BC.G + " is 64 characters, maybe try that.")
            	elif sha == 40:
            		print(BC.F + "SHA1" + BC.G + " is 40 characters, maybe try that.")
            	print("")
            	usages()
            	sys.exit()

            global md5
            md5 = md
            starting()
            clear()
            md52(6, 1)

        if opt in ['--md5']:  
            md2 = arg
            if len(md2) != 32:
            	sha = len(md2)
            	print(BC.G + "The string provided is " + BC.F + str(sha) + BC.G + " characters long, MD5 hashes are 32 characters. Are you sure this is a MD5?")
            	if sha == 64:
            		print(BC.F + "SHA256" + BC.G + " is 64 characters, maybe try that.")
            	elif sha == 40:
            		print(BC.F + "SHA1" + BC.G + " is 40 characters, maybe try that.")
            	print("")
            	usages()
            	sys.exit()
            md5 = md2
            starting()
            clear()
            md52(6, 1)




        if opt in ['-s']:
            sh1 = arg
            if len(sh1) != 40:
            	sha = len(sh1)
            	print(BC.G + "The string provided is " + BC.F + str(sha) + BC.G + " characters long, SHA1 hashes are 40 characters. Are you sure this is a SHA1?")
            	if sha == 64:
            		print(BC.F + "SHA256" + BC.G + " is 64 characters, maybe try that.")
            	elif sha == 32:
            		print(BC.F + "MD5" + BC.G + " is 32 characters, maybe try that.")
            	print("")
            	usages()
            	sys.exit()
            md5 = sh1
            starting()
            clear()
            md52(6, 2)




        if opt in ['-S']:
            sh2 = arg
            if len(sh2) != 64:
            	sha = len(sh2)
            	print(BC.G + "The string provided is " + BC.F + str(sha) + BC.G + " characters long, SHA256 hashes are 64 characters. Are you sure this is a SHA256?")
            	if sha == 40:
            		print(BC.F + "SHA1" + BC.G + " is 40 characters, maybe try that.")
            	elif sha == 32:
            		print(BC.F + "MD5" + BC.G + " is 32 characters, maybe try that.")
            	print("")
            	usages()
            	sys.exit()
            md5 = sh2
            starting()
            clear()
            md52(6, 3)   



        if opt in ['-b']:  
            b = arg
            print(b)     



        if opt in ['-e']:
            e = arg
            print(e)  
        
    
agr()
