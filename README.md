<<<<<<< HEAD
Slacker by
888888 888888    db    8b    d8     88""Yb  dP"Yb   dP"Yb  888888 
  88   88__     dPYb   88b  d88     88__dP dP   Yb dP   Yb   88   
  88   88""    dP__Yb  88YbdP88     88"Yb  Yb   dP Yb   dP   88   
  88   888888 dP""""Yb 88 YY 88     88  Yb  YbodP   YbodP    88 
  Korrupt

I am not responsible for any illegal activity you do with this tool.
This tool is for educational purposes only.



Run install.sh to install *MOST* of the tools used in this tool. 
then launch slacker.py.
'''
sudo chmod +x install.sh && ./install.sh
echo "alias slacker='python3 ~/Slacker/slacker.py'" >> ~/.bash_aliases
python3 slacker.py
'''


Notes About Python Version Issues:
The tools that Slacker utilizes are a combination of Perl, Python2.x, and Python3.x.
The tool itself is written in Python3.
Slacker assumes that your python 2.x is called using 'python', and python 3.x is called using 'python3'.
If you need to have errors, you may need to change this. I would recommend adjusting symlinks.



How To Use Slacker: 
         Arguments: 
 [!target] Set A Global Target [* Used By Default]
                       IE: !target yourdomain.com
 [#target] Set A Single-Tool Use Target
                       IE: #target yourdomain.com
 [#port] Set A Global Target (Where Applicable)
                       IE: #port 22
 [#args] Set Custom Arguments (Where Applicable)
                       IE: #args -Pn -Sv
 [#help] See What Custom Arguments Are Available For That Tool.
                       IE: #help
 [!help] Show This Menu.
                       IE: !help
------------------------------------------------------------------------
All Global Arguments Are Set Using ! - All Local Variables Are Set With #
Tools That Can't Use Local Variables, Such As SQLMap, Will Not Use Global Variables.
=======
# Slacker

For Lazy Penetration Testers
>>>>>>> 5356d3efce93e8efe3df12e46f3d0df2add0990a
