#!/usr/bin/env python

#####################################
#                                   #
#      Created by Stew Alexander    #
#      last updated 11/2023.        #
#                                   #
#####################################

import os
import csv
import subprocess
import sys

def install_package(package_name):
    """Installs a package using pip."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

try:
    from simple_term_menu import TerminalMenu
except ImportError:
    user_choice = input("simple-term-menu is not installed. Would you like to install it? [y/N]: ").lower()
    if user_choice == 'y':
        print("Attempting to install simple-term-menu...")
        install_package("simple-term-menu")
        print("Please restart the script to use the newly installed package.")
        sys.exit()
    else:
        print("Please install simple-term-menu manually to proceed. Exiting.")
        sys.exit()

def pick_file():
    """Let the user pick a file using a TUI menu."""
    files = [f for f in os.listdir() if os.path.isfile(f) and f.endswith('.txt')]
    if not files:
        print("No .txt files found in the directory. Please add some and rerun the script.")
        sys.exit()
    terminal_menu = TerminalMenu(files, title="Select a file:")
    menu_entry_index = terminal_menu.show()
    if menu_entry_index is None:
        print("No file selected. Exiting.")
        sys.exit()
    return files[menu_entry_index]

# Use the pick_file function to let the user select a text file
ip_arp_file = pick_file()

def convert_to_csv(txt_file, csv_file):
    """Convert a text file to a CSV file."""
    try:
        with open(txt_file, 'r') as f, open(csv_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for line in f:
                writer.writerow(line.strip().split())
    except Exception as e:
        print(f"An error occurred: {e}")

# Convert to CSV
csv_file = ip_arp_file.replace(".txt", ".csv")
convert_to_csv(ip_arp_file, csv_file)
print(f"The new CSV File {csv_file} has been created successfully.")

# Press return to quit
input("\nPress [return] to quit")
