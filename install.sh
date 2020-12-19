#ColorMe
RED=`tput setaf 1`
ORANGE=`tput setaf 3`


#Welcome
clear
echo "${ORANGE}This installation will take several minutes depending on your connection speed."
echo "Please don't cancel or reboot during install or packages ${RED}may break${ORANGE}!"
echo "Otherwise, enjoy!"
echo ""
echo "-Korrupt"
echo ""
echo ""
echo ""
echo "Press ${RED}enter${ORANGE} to continue"
read init


#Package Type Checker
t=pacman
y=dpkg
z=emerge
declare -A osInfo;
osInfo[/etc/redhat-release]=yum
osInfo[/etc/arch-release]=pacman
osInfo[/etc/gentoo-release]=emerge
osInfo[/etc/SuSE-release]=zypp
osInfo[/etc/debian_version]=apt-get

for f in ${!osInfo[@]}
do
    if [[ -f $f ]];then
       echo Package manager: ${osInfo[$f]}
       u=${osInfo[$f]}
  
    fi
done
if [ "$u" == "$t" ]; then
clear
i=$u" -S"
up=$u" -Syu"
elif [ "$u" == "$y" ]; then
clear
i=$u" -i"
elif [ "$u" == "$z" ]; then
i=$u" install"
up=$u" --update --deep world"
else
i=$u" install"
up=$u" update"
fi
echo "${ORANGE}your package manager is: ${RED}$u"
echo "${ORANGE}utilizing ${RED}$u ${ORANGE}installation methods."
echo ""
echo ""
echo "Please wait...."
sleep 3
clear


#Installing Tor and SSH for the next step
sudo $i -y tor
sudo $i -y openssh-client 
sudo $i -y openssh-server 

#Readable options
#Tor Host Option
clear
echo "Would you like to install ${RED}tor host${ORANGE}? [Y/N]? ${RED}"
read tora
echo "${ORANGE}"
tor() {
echo "${ORANGE}What ${RED}port ${ORANGE}do you wish to open tor services on: ${RED}"
read tport
echo "${ORANGE}"
sudo sed -i "s|#HiddenServiceDir /var/lib/tor/hidden_service/|HiddenServiceDir /var/lib/tor/hidden_service/|g" /etc/tor/torrc
sudo sed -i "s|#HiddenServicePort 80 127.0.0.1:80|HiddenServicePort ${tport} 127.0.0.1:${tport}|g" /etc/tor/torrc 
sudo service tor restart
clear
}
if [[ "$tora" == "y" ]] || [[ "$tora" == "Y" ]] || [[ "$tora" == "Yes" ]] || [[ "$tora" == "yes" ]]; then
     tor
else
     clear
     echo "OK - Continuing..."
     sleep 2
fi


## UFW Options              
#UFW disable
ufwd() {
sudo ufw disable
}
    
#UFW open port 22
ufws1 () {
sudo ufw allow 22/udp
sudo ufw allow 22/tcp
sudo sed -i "s|#Port 22|Port 22|g" /etc/ssh/sshd_config
sudo systemctl restart ssh
}

#UFW open port 6400 and edit sshd_config
ufws2 () {
sudo ufw allow 6400/udp
sudo ufw allow 6400/tcp
sudo sed -i "s|#Port 22|Port 6400|g" /etc/ssh/sshd_config
sudo systemctl restart ssh
}
                
#UFW open port 80
ufwh () {
sudo ufw allow 80/udp
sudo ufw allow 80/tcp
}
                
#Port Options
echo "Would you like to add port 80 for HTTP [Y/N]:${RED}"
read ufwh
echo "${ORANGE}"
if [[ "$ufwh" == "y" ]] || [[ "$ufwh" == "Y" ]] || [[ "$ufwh" == "Yes" ]] || [[ "$ufwh" == "yes" ]]; then
     ufwh
else
     clear
     echo "OK - Continuing..."
     sleep 2
fi

clear
echo "Would you like to add port ${RED}22${ORANGE} for SSH (Option 2: port 6400 for SSH is the next prompt) [Y/N]:${RED}"
read ufws1
echo "${ORANGE}"
if [[ "$ufws1" == "y" ]] || [[ "$ufws1" == "Y" ]] || [[ "$ufws1" == "Yes" ]] || [[ "$ufws1" == "yes" ]]; then
     ufws1
else
     clear
     echo "OK - Continuing..."
     sleep 2
fi

clear
echo "Would you like to add port ${RED}6400${ORANGE} for SSH AND change /etc/ssh/sshd_config to operate on port 6400 [Y/N]:${RED}"
read ufws2
echo "${ORANGE}"
if [[ "$ufws2" == "y" ]] || [[ "$ufws2" == "Y" ]] || [[ "$ufws2" == "Yes" ]] || [[ "$ufws2" == "yes" ]]; then
     ufws2
else
     clear
     echo "OK - Continuing..."
     sleep 2
fi

clear




#Basic Packages
sudo $up -y
clear
sudo $i -y git 
sudo $i -y ruby 
sudo $i -y python2 
sudo $i -y php 
sudo $i -y gedit 
sudo $i -y ruby rubygems 
sudo $i -y php-curl 
sudo $i -y snapd
sudo $i -y libevent-dev 
sudo $i -y libssl-dev
sudo $i -y ruby-dev
sudo $i -y nmap
sudo snap install noip-client
sudo $i -y tor
sudo $i -y postgresql
sudo $i -y Nikto
sudo $i -y Masscan
sudo $i -y Hashcat
sudo $i -y sqlmap
sudo pip install droopescan
sudo gem install wpscan
git clone https://github.com/drego85/JoomlaScan.git
git clone https://github.com/maldevel/IPGeoLocation.git
cd ipGeoLocation
sudo pip install -r requirements.txt
cd ..



#MSFConsole and Armitage
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall
sudo chmod +x msfinstall
sudo ./msfinstall
sudo service postgresql start
msfdb init

#:::NOTE: The following is not my script:::




##Ruby and git
echo "Installing dependencies"
sudo apt-get install git ruby nmap -y > /dev/null
#


##Man install armitage
echo "Installing Armitage..."
curl -# -o /tmp/armitage.tgz http://www.fastandeasyhacking.com/download/armitage150813.tgz > /dev/null
sudo tar -xvzf /tmp/armitage.tgz -C /opt > /dev/null
sudo ln -s /opt/armitage/armitage /usr/local/bin/armitage > /dev/null
sudo ln -s /opt/armitage/teamserver /usr/local/bin/teamserver > /dev/null
sudo sh -c "echo java -jar /opt/armitage/armitage.jar \$\* > /opt/armitage/armitage" > /dev/null
sudo perl -pi -e 's/armitage.jar/\/opt\/armitage\/armitage.jar/g' /opt/armitage/teamserver > /dev/null
##Create database.yml file
sudo sh -c "echo export MSF_DATABASE_CONFIG=~/.msf4/database.yml >> /etc/profile"
source /etc/profile > /dev/null
sudo chown -R `whoami` ~/.msf4



#:::Continue my script:::

#BadMod installation                                                                                
cd ~
git clone https://github.com/MrSqar-Ye/BadMod.git
mv BadMod ./BM

#Add command-creation shortcut shell
echo 'echo "Name of Command: "'>>commands.sh
echo 'read name'>>commands.sh
echo 'echo $name"s command: "'>>commands.sh
echo 'read command'>>commands.sh
echo 'echo "alias "$name"="\"$command\">>~/.bash_aliases'>>commands.sh
echo 'source ~/.bash_aliases'>>commands.sh
sudo chmod +x commands.sh



#Writing Port Adding Shell
echo 'echo "Port To Add: "'>>./ports.sh
echo 'read port'>>./ports.sh
echo 'ufw allow $port/tcp'>>./ports.sh
echo 'ufw allow $port/udp'>>./ports.sh
sudo chmod +x ports.sh


#Creating WPScan extension for easy use
echo 'echo "enter URL: "'>>./wpscan.sh
echo 'read url'>>./wpscan.sh
echo '~/wpscan/wpscan --url $url --enumerate p --api-token Aj1aAaBpKVFagdawc6uSGjpBks2ahjjn55NvBM1cs2k'>>./wpscan.sh
echo 'wpscan --url $url --enumerate vp --api-token Aj1aAaBpKVFagdawc6uSGjpBks2ahjjn55NvBM1cs2k'>>./wpscan.sh
echo 'wpscan --url $url --enumerate t --api-token Aj1aAaBpKVFagdawc6uSGjpBks2ahjjn55NvBM1cs2k'>>./wpscan.sh
echo 'wpscan --url $url --enumerate vt --api-token Aj1aAaBpKVFagdawc6uSGjpBks2ahjjn55NvBM1cs2k'>>./wpscan.sh
echo 'wpscan --url $url --enumerate u --api-token Aj1aAaBpKVFagdawc6uSGjpBks2ahjjn55NvBM1cs2k'>>./wpscan.sh
echo 'wpscan --url $url --enumerate tt --api-token Aj1aAaBpKVFagdawc6uSGjpBks2ahjjn55NvBM1cs2k'>>./wpscan.sh
sudo chmod +x ./wpscan.sh


#Aliases
#Add Source shortcut (src), Command-creation shortcut (com), WPScan shortcut (wp),
#And BadMod scan shortcut (bscan).
echo 'alias src="source ~/.bash_aliases"'>>./.bash_aliases
echo 'alias com="~/commands.sh"'>>./.bash_aliases
echo 'alias wp="~/wpscan.sh"'>>./.bash_aliases
echo 'alias zap="snap run zaproxy"'>>.bash_aliases
echo 'alias bscan="sudo php ~/BM/BadMod.php"'>>.bash_aliases
echo 'alias afi="sudo apt-fast install -y"'>>.bash_aliases
echo 'alias afr="sudo apt-fast -y remove --purge"'>>.bash_aliases
echo 'alias afu="sudo apt-fast -y update && sudo apt-fast -y upgrade && sudo apt-fast -y dist-upgrade"'>>.bash_aliases
echo 'alias aff="sudo $i -f install"'>>.bash_aliases
echo 'alias up="sudo ~/ports.sh"'>>.bash_aliases
echo 'alias upd="sudo ufw disable"'>>.bash_aliases
echo 'alias upe="sudo ufw enable"'>>.bash_aliases
echo 'alias hostname="sudo cat /var/lib/tor/hidden_service/hostname"'>>.bash_aliases
echo 'alias ts="sudo -E teamserver $(wget -qO- http://ipecho.net/plain | xargs echo) _hacked"'>>.bash_aliases
echo "alias slacker='cd ~/Slacker && ./slacker.py'" >> ~/.bash_aliases
clear


#WPScan install
cd ~
git clone https://github.com/wpscanteam/wpscan
cd wpscan
sudo gem install wpscan


clear
echo "Installing ${RED}ZAProxy${ORANGE} and Dependencies.. this may take a while."
sleep 2
sudo rm /etc/apt/preferences.d/nosnap.pref
sudo $up
sudo $i snapd
sudo snap install zaproxy --classic



#NOTE
#echo "This next portion is going to take several minutes depending on your PC."
#echo "Please let it complete so you get all the necessary packages installed."
#echo "Thanks!"
#echo "-Korrupt"
#echo "Please press Enter to continue, or CTRL+Z to quit."
#echo ""
#echo "-Korrupt"
#read korrupt
#clear
#
#
#NOTE: Use the following AT YOUR OWN RISK!
#People have had issues with adding Kali Repositories, which is why this is commented out. Uncomment at your own risk.
#Installing Kali repos
#sudo sh -c "echo 'deb https://http.kali.org/kali kali-rolling main non-free contrib' > /etc/apt/sources.list.d/kali.list"
#sudo apt -y gnupg
#wget 'https://archive.kali.org/archive-key.asc'
#sudo apt-key add archive-key.asc
#sudo apt update -y && sudo $i -y -y upgrade && sudo $i -y -y dist-upgrade
#sudo sh -c "echo 'Package: *'>/etc/apt/preferences.d/kali.pref; echo 'Pin: release a=kali-rolling'>>/etc/apt/preferences.d/kali.pref; echo 'Pin-Priority: 50'>>/etc/apt/preferences.d/kali.pref"
#sudo $up -y
#sudo $i -y -f install
#sudo apt update -y && sudo $i -y -y upgrade && sudo $i -y -y dist-upgrade
#sudo $i -y wpscan owasp-mantra-ff
#
clear


#Completed with Note
echo "You may want to type: ${RED}source ~/.bash_aliases${ORANGE}, then you can start creating commands with \'${RED}com${ORANGE}\'"
echo "Here are the other aliases I have already created for you:"
echo "${RED}wp${ORANGE} - launches WPScan tool with all possible options. 5 total scans for one target."
echo "${RED}src${ORANGE} - resync's the latest updated .bash_aliases file."
echo "${RED}com${ORANGE} - quickly create a shortcut to a command. Must follow up with src to sync new commands."
echo "${RED}bscan${ORANGE} - quickly launch BadMod scan tool."
echo "${RED}afi${ORANGE} - runs apt-fast install (enter file name last)"
echo "${RED}afr${ORANGE} - runs apt-fast remove --purge (enter file name last)"
echo "${RED}afu${ORANGE} - runs apt-fast update, upgrade, dist-upgrade"
echo "${RED}aff${ORANGE} - runs apt-fast -f install to fix broken packages."
echo "${RED}up${ORANGE} - runs a shell to add ports to UFW."
echo "${RED}upd${ORANGE} - disables UFW"
echo "${RED}upe${ORANGE} - enables UFW"
echo "${RED}hostname${ORANGE} - displays your tor hostname (if installed)"
echo "${RED}ts${ORANGE} - Launch teamserver with public IP and password _hacked"
echo "If you installed tor host your .onion URL is:${RED}"
sudo cat /var/lib/tor/hidden_service/hostname
echo "${ORANGE}Enjoy!"
echo "${RED}-Korrupt${ORANGE}"


