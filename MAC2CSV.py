#!/usr/bin/env python

#####################################
#                                   #
#      Created by Stew Alexander    #
#                2022.              #
#                                   #
#####################################

import os
from re import I
import sys
import time
import subprocess
import csv

word_list = []

#Show the contents of the current directory
print("\nPlease select the ARP or MAC Data text file from the current directory\n")
print(os.listdir(), "\n")

#while the file name is not valid, ask the user to input the file name again
while True:
	ip_arp_file = input("Please enter the file name: ")
	if os.path.isfile(ip_arp_file):
		break
	else:
		print("\nThe file name is not valid, please try again\n")

#Open the file
with open(ip_arp_file, 'r') as f:
	#split each line into a list called "words"
	for line in f:
		word = line.split()
		#append each word to the word_list
		word_list.append(word)
#close the file
f.close()

#Create a new csv file
csv_file = ip_arp_file.replace(".txt", ".csv")

with open(csv_file, 'w') as csvfile:
	#create a csv writer
	writer = csv.writer(csvfile)
	#write the word_list to the csv file
	writer.writerows(word_list)

#Close the csv file
csvfile.close()

#Convert the newline characters to a PC format
with open(csv_file, 'r') as f:
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

print("The new CSV File", csv_file,"has been created successfully in the current directory")
#press return to quit
input("\nPress [return] to quit")
