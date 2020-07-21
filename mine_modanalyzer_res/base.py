import random
import os
# import time #uncomment for launcher feature
verfile=open('ver.txt', 'r')
ver=verfile.read()
verfile.close

def header():
    print("Minecraft Mod Analyzer "+ver+". To get help, enter here 'help'.")
    print("Settings and locations you can set in 'settings.ini' file")
    print("----------------------------------------------")
    # just for test
    try: 
        copyfile.filecopy()
    except: 
        print("WARNING! You must install (filecopy) module by type in command promport 'pip install (filecopy)'")

# disabled, beacuse this feature does not make sense
# def launcher():
#     i=1
#     randomint=1
#     while i<6:
#         print('Please, be patient! Program is loading...')
#         x='####'
#         x=x*i
#         print(x)
#         randomint=random.randint(1,3)
#         time.sleep(randomint)
#         i+=1
#         os.system("cls")
#     print("Program is loaded")
