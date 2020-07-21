import os
import fnmatch
import zipfile
import configparser
# apdir=os.getenv('APPDATA') #non-refactor
# modlocation = apdir+r"/.minecraft/mods" #non-refactor

# released
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
def mcmodanalyze():
    modname=str(input("Enter FULL name of mod - "))
    modjar=zipfile.ZipFile(modname, "r")
    modjar.extract(path="temp",member="mcmod.info")
    modjar.close()
    infomodname = modname.replace('.jar', '')
    configlocat="temp/mcmod("+infomodname+").info"
    try: 
        os.remove(configlocat)
    except: 
        temp=1
        temp+=1
    os.rename("temp/mcmod.info", configlocat)
    fileconf=open(configlocat,"r")
    n=0
    rline=[ ]
    rline=fileconf.read().splitlines()
    while n!=len(rline):
        par1='"name":' in rline[n]
        if par1==True:
            modname_conf=rline[n]
        par2='"mcversion":' in rline[n]
        if par2==True:
            version_conf=rline[n]
        n+=1
    try:
        modname_conf=modname_conf.replace('"', '')
        modname_conf=modname_conf.replace('name: ', '')
        modname_conf=modname_conf.replace(',', '')
        print(modname_conf)
    except: temp+=1
    try:
        version_conf=version_conf.replace('"', '')
        version_conf=version_conf.replace('mcversion: ', '')
        version_conf=version_conf.replace(',', '')
        print(version_conf)
    except: temp+=1
    # нужно чуть-чуть переделать эту функцию, сначала посчитав количество файлов
    # потом, заносим под каждый номер в массив и берем оттуда название файла(мода) для его анализа
    # у нас есть теперь проанализированный мод, потом заносим название мода и его данные в конфигурационный файл
    # будем использовать модуль configparser и заносим все данные в файл
    # и потом, при общем переименовании, берем из конфигурационного файла название и версию майна (или версию мода, потом подумаем)
    # придется, для переименования дублировать данный метод. или обойтись без конфига, постоянно перезаписывать
    # кстати, это лучше. опять же, думаем, разумно ли использовать файл, если его постоянно перезаписывать
def infomod():
    modname=str(input("Enter FULL name of mod - "))
    modjar=zipfile.ZipFile(modname, "r")
    modjar.extract(path="temp",member="mcmod.info")
    modjar.close()
    infomodname = modname.replace('.jar', '')
    configlocat="temp/mcmod("+infomodname+").info"
    try: 
        os.remove(configlocat)
    except: 
        temp=1
        temp+=1
    os.rename("temp/mcmod.info", configlocat)
    fileconf=open(configlocat,"r")
    n=0
    rline=[ ]
    rline=fileconf.read().splitlines()
    while n!=len(rline):
        rline[n]=rline[n]
        rline[n]=rline[n].replace('"', '')
        rline[n]=rline[n].replace('{', '')
        rline[n]=rline[n].replace('}', '')
        rline[n]=rline[n].replace(',', '')
        rline[n]=rline[n].replace('[', '')
        rline[n]=rline[n].replace(']', '')
        print(rline[n])
        # rline[n]=rline[n].replace(',', '')
        n+=1

# developing now
def backmod():
    print("Feature in development. NOW!")

# feature functions
def checkmod():
    print("Feature in development.")
def updmod():
    print("Feature in development.")
def renamer():
    print("Feature in development.")
def modinstall():
    print("Feature in development.")