import os
import fnmatch
apdir=os.getenv('APPDATA')
modlocation = apdir+r"/.minecraft/mods"
def listmodall():
    print("All mods:")
    listOfFiles = os.listdir(apdir+r"\.minecraft\mods")  
    pattern = "*.jar"  
    for entry in listOfFiles:  
        if fnmatch.fnmatch(entry, pattern):
            print(entry)
def listmoddis():
    print("Disabled mods:")
    listOfFiles = os.listdir(apdir+r"\.minecraft\mods")  
    pattern = "*.jardisable"  
    for entry in listOfFiles:  
        if fnmatch.fnmatch(entry, pattern):
            print(entry)
def listmodena():
    print("Enabled mods:")
    listOfFiles = os.listdir(apdir+r"\.minecraft\mods")  
    pattern = "*.jar*"  
    for entry in listOfFiles:  
        if fnmatch.fnmatch(entry, pattern):
            print(entry)
def dismod():
    try:   
        modname="/"+str(input("Enter modname WITH .jar! "))
        modnameslash="/"+modname
        os.rename(modlocation+modnameslash, modlocation+modnameslash+'disable')
        print("Mod "+modname+" was disabled")
    except: print("Error. Try again.")
def enamod():
    try:   
        modname=str(input("Enter modname WITH .jardisable ! "))
        modnameslash="/"+modname
        newmodname = modname.replace('disable', '')
        newmodnameslash="/"+newmodname
        os.rename(modlocation+modnameslash, modlocation+newmodnameslash)
        print("Mod "+modname+" was enabled.")
    except: print("Error. Try again.")