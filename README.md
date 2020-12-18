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
```
sudo chmod +x install.sh && ./install.sh
echo "alias slacker='python3 ~/Slacker/slacker.py'" >> ~/.bash_aliases
source ~/.bash_aliases
slacker
```

Windows:

```
wget linux.distros kthx
```

## Usage example

How To Use Slacker: 

!target Set A Global Target
```
!target yourdomain.com
```
\#target Set A One-Time Local Target
```
#target yourdomain.com
```
\#port Set Local Ports
```
#port 22
```
\#args Set Custom Args (Where Applicable)
```
#args -t -p
```
\#help Get Help From A Tool For Custom Args
```
#help
```
!help Display This Menu
```
!help
```
~~~
All Global Arguments Are Set Using ! - All Local Variables Are Set With #
Tools That Can Not Use Global Variables, Such As SQLMap, Will Not Use Global Variables.
~~~
=======
Slacker
For Lazy Penetration Testers
