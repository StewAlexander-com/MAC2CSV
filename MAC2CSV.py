#!/usr/bin/env python

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
import csv
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

#check if the tqdm module exists, if not install it
try :
    from tqdm import tqdm
except ImportError:
    subprocess.call([sys.executable, "-m", "pip", "install", "tqdm"])
    time.sleep(10)
    from tqdm import tqdm

#check if the plotly module exists, if not install it
try :
    import plotly
    import plotly.graph_objs as go
except ImportError:
    print("[!] Plotly library not installed, Installing...")
    os.system("pip3 install plotly")
    time.sleep(30)
    import plotly
    import plotly.graph_objs as go

#if the library requests is not installed, install it via pip
try:
    import requests
except ImportError:
    print("[!] The requests library is not installed. Installing...")
    os.system("pip install requests")
    print("[+] The requests library has been installed.")
    time.sleep(30)
    import requests

#Try to import the csv library, if it doesn't exist, install it
try:
    import csv
except ImportError:
    print("[!] The csv library is not installed. Installing...")
    os.system("pip install csv")
    print("[+] The csv library has been installed.")
    time.sleep(30)
    import csv

OUI_list = [] 
OUI_list_final = []
company_list =[]
company_list_final = []
vlan_list = []
vlan_list_final = []
word_list = []  

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

print("The new CSV File", csv_file, "has been created successfully in the current directory")
#press return to quit
input("\nPress [return] to quit")


            

            
                 


