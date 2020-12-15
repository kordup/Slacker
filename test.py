def delMe(*args):
    with open('metasploit/meta.py') as f:
        global _lines
        _lines = f.read().splitlines()
        print(_lines)
    for i in args:
        g = [x for x in _lines if not i in x]        
        _lines = g
        print(_lines)
    
    
delMe('RHOST', 'RPORT', 'LHOST', 'LPORT', 'SRVHOST', 'SRVPORT', 'exploit -t 0 -j', 'sleep', 'exit' )