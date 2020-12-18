# Slacker By Team R00T
> A Tool To Make Your Lazy Ass Useful

Slacker is a combination of other hacking tools, utilizing global variables - providing quicker tool navigation. Slacker does a lot of the work for you - making hacking easier, quicker, and more efficient. This is Version .5 because the toolset is yet to be complete! Feel free to drop some constructive critisism/tool requests.

NOTE: 
I am not responsible for any illegal activity you do with this tool.
This tool is for educational purposes only.


## Installation

OS X & Linux:

Run install.sh to install *MOST* of the tools used in this tool. 
then launch slacker.py.
'''
sudo chmod +x install.sh && ./install.sh
echo "alias slacker='python3 ~/Slacker/slacker.py'" >> ~/.bash_aliases
python3 slacker.py
'''

Windows:

```
wget linux.distros kthx
```

## Usage example

How To Use Slacker: 
Arguments:
!target Set A Global Target
'''
        ie: !target yourdomain.com
'''
\#target Set A One-Time Local Target
'''
        ie: #target yourdomain.com
'''
\#port Set Local Ports
'''
        ie: #port 22
'''
\#args Set Custom Args (Where Applicable)
'''
        ie: #args -t -p
'''
\#help Get Help From A Tool For Custom Args
'''
        ie: #help
'''
!help Display This Menu
'''
        ie: !help
'''


#Slacker by Team R00T | Korrup
Notes About Python Version Issues:
The tools that Slacker utilizes are a combination of Perl, Python2.x, and Python3.x.
The tool itself is written in Python3.
Slacker assumes that your python 2.x is called using 'python', and python 3.x is called using 'python3'.
If you need to have errors, you may need to change this. I would recommend adjusting symlinks.

All Global Arguments Are Set Using ! - All Local Variables Are Set With #
Tools That Can't Use Local Variables, Such As SQLMap, Will Not Use Global Variables.
=======
Slacker
For Lazy Penetration Testers
