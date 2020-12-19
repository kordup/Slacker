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

The following lines assume that you have Slacker installed in the ~ (Home) directory. 

```
sudo chmod +x install.sh && ./install.sh
source ~/.bash_aliases
slacker
```

Windows:

```
wget linux.distros kthx
```

## How to use Slacker 

!target - Set a global target.
```
!target yourdomain.com
```
\#target - Set a one-time local target.
```
#target yourdomain.com
```
\#port - Set local port(s).
```
#port 22
```
\#args - Set custom arguments. (Where applicable)
```
#args -t -p
```
\#help - Get the arguments a tool uses (that specific tools help menu) for the #args command.
```
#help
```
!help - Display This Menu
```
!help
```

> All global arguments are set using ! - whereas all local arguments are set using # .
>
> Tools that can not use global variables, such as SQLMap, will only utilize local variables. The !target, #target, etc. commands will only assign locally in these conditions.
>
> If a tool does not list a local variable (ports, custom arguments, etc), that local variable does not exist for that tool.



 To Do: - [ ] Add More Tools
              - [ ] HashCat
              - [ ] Dir Tools
              - [ ] Admin Finder
              - [ ] FPing
              - [ ] IPGeolocation
              - [ ] Crawlers
              - [ ] Admin Page Finder(s)
              - [ ] Vuln Scanners
              - [ ] Bluetooth Tools
              - [ ] Wifi Tools
              - [ ] More DoS Tools
        - [ ] Make Source More Windows Friendly
              - [ ] Add A PS Script For Installation
              - [ ] Find Alternate Methods of os.system Calls.
        - [ ] Create Custom Tool Area
              - [ ] Make Menu Creator
              - [ ] Make Tool Functionality/Call Creator






Slacker
For Lazy Penetration Testers
