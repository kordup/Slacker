import globalt

class BC:
    G = '\033[92m'
    A = '\033[0;37m'
    F = '\033[91m'


def logo():
            print(BC.G + "Slacker by")
            print(BC.F + "888888 888888    db    8b    d8     88\"\"Yb  dP\"Yb   dP\"Yb  888888 ")
            print("  88   88__     dPYb   88b  d88     88__dP dP   Yb dP   Yb   88   ")
            print("  88   88\"\"    dP__Yb  88YbdP88     88\"Yb  Yb   dP Yb   dP   88   ")
            print("  88   888888 dP\"\"\"\"Yb 88 YY 88     88  Yb  YbodP   YbodP    88 ")
            print(BC.G + "  Korrupt")
            print("Global Target: [" + BC.F + globalt.target + BC.G + "]")
            print("")
            
            
def logo2():
            print(BC.G + "Slacker by")
            print(BC.F + "888888 888888    db    8b    d8     88\"\"Yb  dP\"Yb   dP\"Yb  888888 ")
            print("  88   88__     dPYb   88b  d88     88__dP dP   Yb dP   Yb   88   ")
            print("  88   88\"\"    dP__Yb  88YbdP88     88\"Yb  Yb   dP Yb   dP   88   ")
            print("  88   888888 dP\"\"\"\"Yb 88 YY 88     88  Yb  YbodP   YbodP    88 ")
            print(BC.G + "  Korrupt")
            print("")
            
    
def mitems2(*a):
    global menuz
    mitems = a 
    for idx, i in enumerate(mitems, start=1):
        print( BC.G + " [" + BC.F + str(idx) + BC.G + "] " + i)
    else:
        print("------------------------------------------")
        print(" [" + BC.F + "**" + BC.G + "] Help Menu")
        print("  [" + BC.F + "*" + BC.G + "] Main Menu")
        print("  [" + BC.F + "0" + BC.G + "] Exit")    
    
        
def mitems(*a):
    global menuz
    mitems = a 
    for idx, i in enumerate(mitems, start=1):
        print( BC.G + " [" + BC.F + str(idx) + BC.G + "] " + i)
    else:
        print("------------------------------------------")
        print(" [" + BC.F + "!" + BC.G + "] Back")
        print(" [" + BC.F + "**" + BC.G + "] Help Menu")
        print(" [" + BC.F + "*" + BC.G + "] Main Menu")
        print(" [" + BC.F + "0" + BC.G + "] Exit")
        
        
def helpm():
    print(BC.G + "How To Use Slacker: ")
    print(BC.F + "         Arguments: " + BC.G)
    print(" [" + BC.F + "!target" + BC.G + "] Set A Global Target [* Used By Default]")
    print("                       IE: !target yourdomain.com")
    print(" [" + BC.F + "#target" + BC.G + "] Set A Single-Tool Use Target")
    print("                       IE: #target yourdomain.com")
    print(" [" + BC.F + "#port" + BC.G + "] Set A Global Target")
    print("                       IE: #port 22")
    print(" [" + BC.F + "#args" + BC.G + "] Set Custom Arguments")
    print("                       IE: #args -Pn -Sv")
    print(" [" + BC.F + "#help" + BC.G + "] See What Custom Arguments Are Available For That Tool.")
    print("                       IE: #help")
    print(" [" + BC.F + "!help" + BC.G + "] Show This Menu.")
    print("                       IE: !help")
    print("NOTES:")
    print("All Global Arguments Are Set Using ! - All Local Variables Are Set With #")
    print("Tools That Can't Use Local Variables, Such As SQLMap, Will Not Use Global Variables.")
    print("")
