import os
import fnmatch
import zipfile
# apdir=os.getenv('APPDATA') #non-refactor
# modlocation = apdir+r"/.minecraft/mods" #non-refactor
def listmodall():
    print("All mods:")
    # listOfFiles = os.listdir(apdir+r"\.minecraft\mods") #non-refactor
    listOfMods = os.listdir() #refactory
    pattern = "*.jar*"  
    for entry in listOfMods:  
        if fnmatch.fnmatch(entry, pattern):
            print(entry)
def listmoddis():
    print("Disabled mods:")
    # listOfFiles = os.listdir(apdir+r"\.minecraft\mods") #non-refactor
    listOfFiles = os.listdir()  #refactory
    pattern = "*.jardisable"  
    for entry in listOfFiles:  
        if fnmatch.fnmatch(entry, pattern):
            print(entry)
def listmodena():
    print("Enabled mods:")
    # listOfFiles = os.listdir(apdir+r"\.minecraft\mods") #non-refactor
    listOfFiles = os.listdir()  #refactory
    pattern = "*.jar"  
    for entry in listOfFiles:  
        if fnmatch.fnmatch(entry, pattern):
            print(entry)
def dismod():
    try:   
        # modname="/"+str(input("Enter modname WITH .jar! ")) #non-refactor
        modname=str(input("Enter modname WITH '.jar!' "))#refactory
        # modnameslash="/"+modname #non-refactor
        # os.rename(modlocation+modnameslash, modlocation+modnameslash+'disable') #non-refactor
        os.rename(modname, modname+'disable')#refactory
        print("Mod "+modname+" was disabled")
    except: print("Error. Try again.")
def enamod():
    try:   
        oldmodname=str(input("Enter modname WITH .jardisable ! ")) 
        # modnameslash="/"+modname
        newmodname = oldmodname.replace('disable', '')
        # newmodnameslash="/"+newmodname
        os.rename(oldmodname, newmodname)#refactory
        print("Mod "+newmodname+" was enabled.")
    except:
        print("Error. Try again.")
def remmod():
    remmodname=str(input("Enter full modname to remove (from list) - "))
    try: 
        really=input("Do you REALLY want to delete this mod? If yes - type full mod name again. ")
        if remmodname==really:
            os.remove(remmodname)
            print("Mod was deleted.")
        else: print("Abort.")
    except:
        print("An error occurated. Try again.")
def backmod():
    print("Developing...")
def modextract():
    modname=str(input("Enter FULL name of mod - "))
    modjar=zipfile.ZipFile(modname, "r")
    modjar.extract(path="temp",member="mcmod.info")
    modjar.close()
    infomodname = modname.replace('.jar', '')
    configlocat="temp/mcmod("+infomodname+").inf"
    os.remove(configlocat)
    os.rename("temp/mcmod.info", configlocat)
    # x=open(configlocat,"r")
    # line3=[ ]
    # line3=x.readline(2)
    # print(line3)
    # нам нужно анализировать этот файл как inf с настройками от питона, в закладках браузера есть, посмотри

def anmcmod():
    print("Use after getmcmod")
