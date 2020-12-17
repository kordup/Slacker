import os 
import sys
import re
import time
import linecache
from clear import clear
from logo import *

def start():
    global msfconsole
    global msfdb
    global msfupdate
    global _lines
    with open('metasploit/msfconsole.py') as f:
        msfconsole = f.read()
    with open('metasploit/msfdb.py') as f:
        msfdb = f.read()
    with open('metasploit/meta.py') as f:
        _lines = f.readlines()
    with open('metasploit/msfupdate.py') as f:
        msfupdate = f.read()
    menu()



def delMe(*args):
    global g
    global lines
    with open('metasploit/meta.py') as f:
        global _lines
        _lines = f.read().splitlines()
    for i in args:
        g = [x for x in _lines if not i in x]        
        _lines = g
seconds = 0


def oute():
    with open('metasploit/meta.py') as f:
        global _lines
        _lines = f.read().splitlines()
        print(_lines)
    clear()
    logo2()
    print("")
    print("Old metasploit host data: \n" + '\n'.join(_lines))
    print("")
    print(BC.F + "WARNING:" + BC.G + " LazyBoi stores current metasploit host data in your local directory.")
    print("           any existing metasploit host data (above) is going to be replaced.")
    print("Press 0 to cancel")
    delMe('RHOST', 'RPORT', 'LHOST', 'LPORT', 'SRVHOST', 'SRVPORT', 'exploit -t 0 -j', 'sleep', 'exit', '\n' )
    global listed
    listed = []
    

def exploit(a):
    with open('metasploit/meta.py') as f:
        global _lines
        _lines = f.read().splitlines()
        print(_lines)
    delMe('use' )
    _lines.insert(0, 'use ' + a) 
    with open('metasploit/meta.py','w') as f:
        for element in _lines:
            f.write(element)
            f.write('\n')
    print(_lines)
    clear()
    menu()


def payload(a):
    with open('metasploit/meta.py') as f:
        global _lines
        _lines = f.read().splitlines()
        print(_lines)
    delMe('PAYLOAD' )
    _lines.insert(0, 'set PAYLOAD ' + a) 
    with open('metasploit/meta.py','w') as f:
        for element in _lines:
            f.write(element)
            f.write('\n')
    print(_lines)
    clear()
    menu()


def menu():
    global msfconsole
    global msfdb
    global msfupdate
    logo2()
    mitems = (" Exploits", " Payloads", " Set Values", " Print Current Metasploit Host Data", " Run/Exploit", " Msfdb Init", " Msfdb Delete and Init *May Help If Errors*", " Delete Host File and Renew", " Update Exploit/Payload List", "Custom File Paths")
    for idx, i in enumerate(mitems, start=1):
        print( BC.G + " [" + BC.F + str(idx) + BC.G + "] " + i)
    else:
        print("------------------------------------------")
        print(" [" + BC.F + "*" + BC.G + "] Main Menu")
        print(" [" + BC.F + "0" + BC.G + "] Exit")
        m7 = input("")
    if m7 == "1":
        clear()
        logo2()
        e7 = print(" [" + BC.F + "1" + BC.G + "] Search For An Exploit")
        e7 = print(" [" + BC.F + "2" + BC.G + "] Set Exploit")
        e7 = input("")
        e7 = int(e7)
        if e7 == 1:
            global search
            print(BC.F + "NOTE:" + BC.G +" Separate multiple items with a |")
            print("IE: blue|samba")
            search = input("What Service Are We Exploiting: ")
            with open("metasploit/exploits.txt", "r") as f:
                for line in f:
                    if re.match("(.*)(" + search + ")(.*)", line):
                        print(line)
            expl = input("Enter an Exploit To Use: ")
            print("")
            if expl == "":
                print('1')
            else:   
                exploit(expl)           
        elif e7 == 2:
            expl = input("Enter an Exploit To Use: ")
            print("")
            if expl == "":
                None
            else:   
                exploit(expl1)
        clear()
        menu()
    elif m7 == "2":
        clear()
        logo2()
        p7 = print(" [" + BC.F + "1" + BC.G + "] Search For A Payload")
        p7 = print(" [" + BC.F + "2" + BC.G + "] Set Payload")
        p7 = input("")
        p7 = int(p7)
        if p7 == 1:
            print(BC.F + "NOTE:" + BC.G +" Separate multiple items with a |")
            print("IE: tcp|multi")
            search = input("What Type of Payload?: ")
            with open("metasploit/payloads.txt", "r") as f:
                for line in f:
                    if re.match("(.*)(" + search + ")(.*)", line):
                        print(line)
            payl = input("Enter a Payload To Use: ")
            if payl == "":
                None
            else:
                payload(payl)           
        elif p7 == 2:
            payl = input("Enter a Payload To Use: ")
            if payl == "":
                None
            else:   
                payload(payl)
        clear()
        menu()
    elif m7 == "3":
        clear()
        logo2()
        global _lines
        oute()
        rhost = input("RHOST: ")
        if rhost == '0':
            menu()
        rport = input("RPORT: ")
        lhost = input("LHOST: ")
        lport = input("LPORT: ")
        srvhost = input("SRVHOST: ")
        srvport = input("SRVPORT: ")
        print("NOTE: Enter 0 For No Time Limit.")
        sleep = input("Time To Run : ")
        bin = ['set RHOST ' + rhost, 'set RPORT ' + rport, 'set LHOST ' + lhost, 'set LPORT ' + lport, 'set SRVHOST ' + srvhost, 'set SRVPORT ' + srvport, 'exploit -t 0 -j']
        for i in bin:
         _lines.append(i)
        if int(sleep) > 0:
            _lines.append('sleep ' + sleep)
            _lines.append('exit -y')
        else:
            None
        with open('metasploit/meta.py','w') as f:
            for element in _lines:
                f.write(element)
                f.write('\n')
        clear()
        start()
    elif m7 == "4":
        clear()
        print(BC.F + "Current Metasploit Host Data: \n" + BC.G + ''.join(_lines))
        print("")
        menu()
    elif m7 == "5":
        os.system ( msfconsole + ' -r ./metasploit/meta.py' )
        menu()
    elif m7 == "6":
        clear()
        os.system ( msfdb + ' init' )
        menu()
    elif m7 == "7":
        clear()
        os.system ( msfdb + ' delete' )
        os.system ( msfdb + ' init' )
        menu()
    elif m7 == "8":
        with open('metasploit/meta.py', 'w') as f:
            f.write("")
        clear()
        menu()
    elif m7 == "9":
        clear()
        logo2()
        print("")
        print("Updating Metasploit Exploits and Payloads...")
        print("This Will Take Several Minutes.")
        print("")
        time.sleep(2)
        os.system(msfupdate)
        print("")
        print("Fetching New Exploits And Payloads...")
        print("")
        os.system(msfconsole + " -r metasploit/update_pay.py > metasploit/payloads.txt")
        os.system(msfconsole + " -r metasploit/update_exp.py > metasploit/exploits.txt")
        clear()
        print("")
        print("Complete!")
        menu()
    elif m7 == "10":
        msfconsole = input("Enter The Path To msfconsole: ")
        with open('metasploit/msfconsole.py', 'w') as f:
            msfconsole = f.write(msfconsole)
        msfdb = input("Enter The Path To msfdb: ")
        with open('metasploit/msfdb.py', 'w') as f:
            msfdb = f.write(msfdb)
        msfupdate = input("Enter The Path To msfupdate: ")
        with open('metasploit/msfupdate.py', 'w') as f:
            msfupdate = f.write(msfupdate)
        clear()
        start()
    elif m7 == "*":
        quit
    elif m7 == "0":
        sys.exit()
    else:
        clear()
        print("WHELP! That didn't quite work...")
        time.sleep(1)
        menu()