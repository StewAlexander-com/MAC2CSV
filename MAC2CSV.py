#!/usr/bin/env python3

#####################################
#                                   #
#      Created by Stew Alexander    #
#                2021               #
#                                   #
#####################################

import os
from re import I
import sys
import time
import subprocess
import json

#check if the rich module exists, if not, install it
try:
    from rich import print
    from rich import pretty
except ImportError:
    subprocess.call([sys.executable, "-m", "pip", "install", "rich"])
    import rich
    time.sleep (10)
    from rich import print as rprint

#Try to import the csv library, if it doesn't exist, install it
try:
    import csv
except ImportError:
    print("[!] The csv library is not installed. Installing...")
    os.system("pip install csv")
    print("[+] The csv library has been installed.")
    time.sleep(30)
    import csv

word_list = []  

print('''[yellow]
  __  __               _____   ___     _____    _____  __      __
 |  \/  |     /\      / ____| |__ \   / ____|  / ____| \ \    / /
 | \  / |    /  \    | |         ) | | |      | (___    \ \  / / 
 | |\/| |   / /\ \   | |        / /  | |       \___ \    \ \/ /  
 | |  | |  / ____ \  | |____   / /_  | |____   ____) |    \  /   
 |_|  |_| /_/    \_\  \_____| |____|  \_____| |_____/      \/                                                                                                                                    
''')


print('''[bright_cyan]
 ┌───────────────────────────────────────────┐
 │    [white]Turns a MAC Address Hardware Table[/white]     │
 │    [white]or IP ARP into a csv file for easy[/white]     │
 │    [white]import and review by your favorite[/white]     │
 │    [white]spreadsheet application[/white]                │
 │                                           │
 └───────────────────────────────────────────┘
[/bright_cyan]''')


#Show the contents of the current directory
print("\nPlease select the [italic green]ARP[/italic green] or [italic green]MAC[/italic green] Data text file from the current directory\n")
print(os.listdir(), "\n")

#while the file name is not valid, ask the user to input the file name again
while True:
    ip_arp_file = input("Please enter the file name: ")
    if os.path.isfile(ip_arp_file):
        break
    else:
        print("\n[italic yellow]The file name is not valid, please try again[/italic yellow]\n")

#Open the file
with open(ip_arp_file, 'r') as f:
#split each line into a list called "words"
    for line in f:
        word= line.split()
       #append each word to the word_list
        word_list.append(word)
#close the file
f.close()

#Create a new csv file
csv_file =ip_arp_file.replace(".txt", ".csv")

with open(csv_file, 'w') as csvfile:
    #create a csv writer
    writer = csv.writer(csvfile)
    #write the word_list to the csv file
    writer.writerows(word_list) 

#Close the csv file
csvfile.close()

#Convert the newline characters to a PC format
with open(csv_file , 'r') as f:
    data = f.read().replace('\r', '')
    
#overwrite the file with the new data
with open(csv_file, 'w') as f:
    f.write(data)

#Remove duplicate \n characters from the file
with open(csv_file, 'r') as f:
    data = f.read().replace('\n\n', '\n')
#close the file
f.close()

#overwrite the file with the new data
with open(csv_file, 'w') as f:
    f.write(data)
#close the file

print("The new CSV File [green]" + csv_file + " [/green]has been created successfully in the current directory")
#press return to quit
print("\n[yellow]Press [bright_blue underline]enter[/bright_blue underline] or [bright_blue underline]return[/bright_blue underline] to quit[/yellow] ".rstrip())
input("> ")   
