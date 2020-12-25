import sys
import os
import requests
from colorama import *
import pefile
import re


# Title print

logo = (Fore.RED + '''
░██████╗███████╗░█████╗░███╗░░░███╗██╗░░░██╗████████╗███████╗██╗░░██╗
██╔════╝██╔════╝██╔══██╗████╗░████║██║░░░██║╚══██╔══╝██╔════╝╚██╗██╔╝
╚█████╗░█████╗░░██║░░╚═╝██╔████╔██║██║░░░██║░░░██║░░░█████╗░░░╚███╔╝░
░╚═══██╗██╔══╝░░██║░░██╗██║╚██╔╝██║██║░░░██║░░░██║░░░██╔══╝░░░██╔██╗░
██████╔╝███████╗╚█████╔╝██║░╚═╝░██║╚██████╔╝░░░██║░░░███████╗██╔╝╚██╗
╚═════╝░╚══════╝░╚════╝░╚═╝░░░░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            SecMutex : Automated Malware Analysis Framwork

[!] This Tool Must Run As ROOT [!]         Created By : SecFirm Team
----------------------------------------------------------------------------\n\n''')
print(logo)
print(Style.RESET_ALL)

user_input = input(Fore.GREEN + "Enter the path of your file: ")
print(Style.RESET_ALL)
if os.path.exists(user_input):
    print("Hooray, found your file! : " + str(user_input))
else:
    print(Fore.RED + "Failed to Fetch File, Pleae Try Again")
    print(Style.RESET_ALL)
    print("")

# Main Menu for Users


def mainmenu():
    print("""
   {1}--PE Viewer
   {2}--HEX Viewer
   {3}--Threat Intelligence Analysis
   {4}--Sandbox
   {5}--Automated Analysis
   {6}--Custom and Rule Based Analysis
   {7}--Reverse Engineering ( Ollydbg Integrated V1)
   {8}--Memory Analysis
   {9}--Behavior analysis
   {10}--Sysinternals
   {0}--Exit
 """)
    choice = input("SecFirm~# ")
    if choice == "1":
        pemenu()
    elif choice == "2":
        hexmenu()
    elif choice == "3":
        timenu()
    elif choice == "4":
        sanboxemenu()
    elif choice == "5":
        automenu()
    elif choice == "6":
        custommenu()
    elif choice == "7":
        reversemenu()
    elif choice == "8":
        memorymenu()
    elif choice == "9":
        behaviouremenu()
    elif choice == "10":
        sysinternalsmenu()
    elif choice == "0":
        print("Thanks for Using SecMutex")
        os.system('clear'), sys.exit()
    elif choice == "":
        print(logo)
        print("\033[1m [+] Kindly Choose One Option \033[0m")
    else:
        print(logo)


# PEViewer
def pemenu():
    peview = pefile.PE(user_input)
    print(peview)


# Call main Menu
mainmenu()
