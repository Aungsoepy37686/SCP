#!/bin/python

import os
import sys
import time
import pyfiglet

def bersih():
       os.system("clear")

def menu():
       bersih()
       a = pyfiglet.figlet_format('SCP - 097')
       print (a)
       print("----------------------------------------------")
       print(" ➤Author   : \033[1:93mAunSoePy")
       print(" ➤Github   : \033[1:93mhttps://github.com/Aungsoepy37686")
       print(" ➤Facebook : \033[1:93mAung SoePy")
       print(" ----------------------------------------------") 
       print("[ 1 ] Facebook Login")
       print("[ 2 ] File create")
       print("[ 0 ] Exit")
       print("----------------------------------------------")
       pil = input("Select an option: ")
       if pil =="1":
            os.system("python 777.py")
       elif pil =="2":
            os.system("python devil.py")
       elif pil =="3":
            sys.exit()

menu()