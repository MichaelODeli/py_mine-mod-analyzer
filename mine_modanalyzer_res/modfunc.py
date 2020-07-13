import os
import fnmatch
def listmodall():
    print("All mods:")
    apdir=os.getenv('APPDATA')
    listOfFiles = os.listdir(apdir+r"\.minecraft\mods")  
    pattern = "*.jar"  
    for entry in listOfFiles:  
        if fnmatch.fnmatch(entry, pattern):
            print(entry)
def listmoddis():
    print("Disabled mods:")
    apdir=os.getenv('APPDATA')
    listOfFiles = os.listdir(apdir+r"\.minecraft\mods")  
    pattern = "*.jar_backup"  
    for entry in listOfFiles:  
        if fnmatch.fnmatch(entry, pattern):
            print(entry)
def listmodena():
    print("Enabled mods:")
    apdir=os.getenv('APPDATA')
    listOfFiles = os.listdir(apdir+r"\.minecraft\mods")  
    pattern = "*.jar*"  
    for entry in listOfFiles:  
        if fnmatch.fnmatch(entry, pattern):
            print(entry)
