import first

def farst():
    if first.first == 0:
        fst = input("Would you like to run a bash shell to install most required tools?")
        if str(fst) == "y" or str(fst) == "Y":
            os.system ( './required.sh' )
            items = []
            meta = open('metasploit/meta.py')
            _lines = meta.readlines()
            for i in _lines:
                items.append(i)
            out = []
            for i in items:
                if str('0') not in i:
                    out.append(i)
            





first = 0


def onkeypress(fun, key=None)():
    items = []
    meta = open('metasploit/meta.py')
    _lines = meta.readlines()
    for i in _lines:
        items.append(i)
    out = []
    for i in items:
        if str(a) not in i:
            out.append(i)