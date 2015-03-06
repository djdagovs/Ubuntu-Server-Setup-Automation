__author__ = 'Elliot'
from subprocess import call
from platform import system

def clear_screen():
    if system() == "Windows":
        call("cls")
    elif system() == "Darwin" or system() == "Linux":
        call("clear")

# Sets up a multi platform clear screen function for Windows, OS X and Linux

def installsamba():
    call(["sudo", "apt-get", "update"])
    call(["sudo", "apt-get", "-y", "dist-upgrade"])
    call(["sudo", "apt-get", "-y", "install", "python-dnspython", "dnsutils", "attr", "krb5-user", "docbook-xsl", "acl", "samba"])
    clear_screen()
    print("SAMBA is now installed!")
    print("")
    print("Press Enter/Return to continue...")
    mainmenu()

# This installs all of the necessary components for building samba then downloads samba from git.
# After that it then compiles and installs samba and returns to the main menu.

def installvsftpd():
    call(["sudo", "apt-get", "update"])
    call(["sudo", "apt-get", "-y", "dist-upgrade"])
    call(["sudo", "apt-get", "-y", "install", "vsftpd"])
    clear_screen()
    print("VSFTPd is now installed!")
    print("")
    print("Press Enter/Return to continue...")
    mainmenu()
# This installs VSFTPd and return to the main menu.


def installwebmin():
    call(["wget", "http://www.webmin.com/download/deb/webmin-current.deb"])
    call(["sudo", "apt-get", "update"])
    call(["sudo", "apt-get", "-y", "dist-upgrade"])
    call(["sudo", "dpkg", "-i", "webmin-current.deb"])
    call(["sudo", "apt-get", "-y", "install", "-f"])
    call(["rm", "webmin-current.deb"])
    clear_screen()
    print("Webmin is now installed!")
    print("")
    print("Press Enter/Return to continue...")
    mainmenu()

# This installs the current version of WebMin and then returns to the main menu.

def updatesystem():
    call(["sudo", "apt-get", "update"])
    call(["sudo", "apt-get", "-y", "dist-upgrade"])
    clear_screen()
    print("Update Complete!")
    print("It may be wise to restart your computer.")
    print("")
    print("Press Enter/Return to continue...")
    input()
 #   call(["read", "-n", "1"])
    mainmenu()

# This install the latest updates for the system and then returns to the main menu.


def configuresambaforactivedirectory():
    call(["sudo", "sed", "-i.original", "-r", "'/[ \t]\/[ \t]/{s/(ext4[\t ]*)([^\t ]*)/\1\2,user_xattr,acl,barrier=1/}'", "/etc/fstab"])
    call(["mount", "-a"])
    call(["sudo", "rm", "/etc/samba/smb.conf"])
    call(["sudo", "samba-tool", "domain", "provision", "--use-rfc2307", "--interactive"])
    call(["sudo", "mv", "/etc/krb5.conf", "/etc/krb5.conf.bak"])
    call(["sudo", "cp", "/var/lib/samba/private/krb5.conf", "/etc/krb5.conf"])
    domaincontrolleryorn()
    clear_screen()
    print("SAMBA is now configured for Active Directory!")
    print("")
    print("Press Enter/Return to continue...")
    mainmenu()

# This function runs all of the necessary actions to make samba a domain controller.


def domaincontrolleryorn():
    clear_screen()
    print("Did you set this installation as a primary domain controller?")
    print("")
    print("If you select yes then it will upgrade the forrest and domain to")
    print("Server 2008 R2 levels. This may break compatibility with earlier")
    print("versions of Windows Server. You can always manually change the levels")
    print("if you wish... Press wisely!")
    print("")
    print("Y or N:")
    domaincontrolleryesorno = str(input("Y or N:"))
    if domaincontrolleryesorno == "Y" or domaincontrolleryesorno == "y":
        upgradeforrestanddomain()
    elif domaincontrolleryesorno == "N" or domaincontrolleryesorno == "n":
        clear_screen()
        print("Samba configuration complete!")
        print("Press Enter/Return to continue...")
        input()
#        print("read -n 1")
    else:
        clear_screen()
        print("Please press either Y or N!!!")
        print("")
        print("Press Enter/Return to continue...")
        input()
#        call(["read", "-n", "1"])
        domaincontrolleryorn()

# This asks the user if he or she would like to upgrade the domain and forrest level.
# If yes then it roputs the user to the code below. If not then the user is taken to the main menu.

def upgradeforrestanddomain():
    clear_screen()
    call(["sudo", "samba-tool", "domain level", "raise", "--domain-level=2008_R2"])
    call(["sudo", "samba-tool", "domain", "level", "raise", "--forest-level=2008_R2"])
    call(["sudo", "samba-tool", "domain", "passwordsettings", "set", "--complexity=off"])
    print("Domain Controller setup has completed!")
    print("")
    print("Press Enter/Return to return to the main menu...")
    input()
#    call(["read", "-n", "1"])


# This function upgrade the Domain and Forrest level to (Server) 2008_R2.
# Acceptable levels are 2008 and 2008 R2. The default is 2003.


def quitprogram():
    clear_screen()
    print("Sorry to see you go... :(")
    exit()
# This is a simple good by program closer.
# Oh, did I mention that it stops the program?


def mainmenu():
    clear_screen()
    print("Press 1 to update your system")
    print("Press 2 to install samba")
    print("Press 3 to install vsFTPd")
    print("Press 4 to install the current version of Webmin")
    print("Press 5 to configure samba for Active Directory")
    print("Press x to exit the script")
    print("")
    mainmenuinput = str(input("Input Selection:"))
    if mainmenuinput == "1":
        updatesystem()
    elif mainmenuinput == "2":
        installsamba()
    elif mainmenuinput == "3":
        installvsftpd()
    elif mainmenuinput == "4":
        installwebmin()
    elif mainmenuinput == "5":
        configuresambaforactivedirectory()
    elif mainmenuinput == "x" or mainmenuinput == "X":
        quitprogram()
    else:
        clear_screen()
        print("You have entered an invallid selection!")
        print("Please try again!")
        print("")
        print("Press Return/Enter to continue...")
        input()
#        call(["read", "-n", "1"])
        mainmenu()

# This builds the main menu and routs the user to the function selected.

mainmenu()

# This executes the main menu function.
# Let the fun begin!!!! WOOT WOOT!!!!
