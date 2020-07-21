import os
import fnmatch
import zipfile
import configparser

# released
def listmodall():
    print("All mods:")
    listOfMods = os.listdir() 
    pattern = "*.jar*"  
    for entry in listOfMods:  
        if fnmatch.fnmatch(entry, pattern):
            print(entry)
def listmoddis():
    print("Disabled mods:")
    listOfFiles = os.listdir()  
    pattern = "*.jardisable"  
    for entry in listOfFiles:  
        if fnmatch.fnmatch(entry, pattern):
            print(entry)
def listmodena():
    print("Enabled mods:")
    listOfFiles = os.listdir()  
    pattern = "*.jar"  
    for entry in listOfFiles:  
        if fnmatch.fnmatch(entry, pattern):
            print(entry)
def dismod():
    try:   
        modname=str(input("Enter modname WITH '.jar!' "))
        os.rename(modname, modname+'disable')
        print("Mod "+modname+" was disabled")
    except: print("Error. Try again.")
def enamod():
    try:   
        oldmodname=str(input("Enter modname WITH .jardisable ! ")) 
        newmodname = oldmodname.replace('disable', '')
        os.rename(oldmodname, newmodname)
        print("Mod "+newmodname+" was enabled.")
    except:
        print("Error. Try again.")
def remmod():
    remmodname=str(input("Enter full modname to remove (from list) - "))
    try: 
        really=input("Do you want to delete this mod? If yes - type full mod name again. ")
        if remmodname==really:
            os.remove(remmodname)
            print("Mod was deleted.")
        else: print("Abort.")
    except:
        print("An error occurated. Try again.")
def mcmodanalyze():
    try:
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
    except KeyError:
        print("No mcmod.info in mod file. Break")
    # нужно чуть-чуть переделать эту функцию, сначала посчитав количество файлов
    # потом, заносим под каждый номер в массив и берем оттуда название файла(мода) для его анализа
    # у нас есть теперь проанализированный мод, потом заносим название мода и его данные в конфигурационный файл
    # будем использовать модуль configparser и заносим все данные в файл
    # и потом, при общем переименовании, берем из конфигурационного файла название и версию майна (или версию мода, потом подумаем)
    # придется, для переименования дублировать данный метод. или обойтись без конфига, постоянно перезаписывать
    # кстати, это лучше. опять же, думаем, разумно ли использовать файл, если его постоянно перезаписывать
def infomod():
    try:
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
    except KeyError:
        print("No mcmod.info in mod file. Break")

# developing now
def renamerid():
    listOfFiles = os.listdir()  
    pattern = "*.jar"
    modlisting=[ ]
    for entry in listOfFiles:  
        if fnmatch.fnmatch(entry, pattern):
            modlisting.append(entry)
    # print(modlisting)

    for modname in modlisting:
        try: 
            temp=0
            modjar=zipfile.ZipFile(modname, "r")
            modjar.extract(path="temp",member="mcmod.info")
            modjar.close()
            infomodname = modname.replace('.jar', '')
            configlocat="temp/mcmod("+infomodname+").info"
            try: 
                os.remove(configlocat)
            except: 
                temp+=1
            os.rename("temp/mcmod.info", configlocat)
            fileconf=open(configlocat,"r")
            n=0
            rline=[ ]
            rline=fileconf.read().splitlines()
            # print(rline) for test
            modname_conf="no-name"
            while n!=len(rline):
                par1='"modid":' in rline[n]
                if par1==True:
                    modname_conf=rline[n]
                    modname_conf=modname_conf.replace(" ", "")
                    modname_conf=modname_conf.replace('\t', "")
                    # print(modname_conf) #test
                n+=1
            try:
                modname_conf=modname_conf.replace('"', '')
                modname_conf=modname_conf.replace('modid:', '')
                modname_conf=modname_conf.replace(',', '')
                # print(modname_conf) #test
            except: 
                temp+=1
            if modname_conf!="no-name": 
                # print(modname)
                newmodname=str(modname_conf)+".jar"
                # print(newmodname)
                os.rename(modname, newmodname)
            else:
                print("No modname speciefed in mcmod.info file for "+modname+". Renamer will break")
        except KeyError: 
            print("No mcmod.info in "+modname+". If you`re developer, please make this file")


# feature functions
def checkmod():
    print("Feature in development.")
def updmod():
    print("Feature in development.")
def modinstall():
    print("Feature in development.")
def backmod():
    print("Feature in development.")

# not working
def renamerver():
    print("Uncomment code for test and edit. I had a crash here.")
#     listOfFiles = os.listdir()  
#     pattern = "*.jar"
#     modlisting=[ ]
#     for entry in listOfFiles:  
#         if fnmatch.fnmatch(entry, pattern):
#             modlisting.append(entry)
#     print(modlisting)

#     for modname in modlisting:
#         try: 
#             modjar=zipfile.ZipFile(modname, "r")
#             modjar.extract(path="temp",member="mcmod.info")
#             modjar.close()
#             infomodname = modname.replace('.jar', '')
#             configlocat="temp/mcmod("+infomodname+").info"
#             temp=1
#             try: 
#                 os.remove(configlocat)
#             except: 
#                 temp+=1
#             os.rename("temp/mcmod.info", configlocat)
#             fileconf=open(configlocat,"r")
#             n=0
#             rline=[ ]
#             rline=fileconf.read().splitlines()
#             # print(rline) for test
#             ticker=len(rline)-1
#             while ticker!=-1:
#                 rline[ticker]=rline[ticker].replace(" ", "")
#                 ticker=ticker-1
#             modname_conf="no-name"
#             mcversion_conf="no-mcver"
#             version_conf="no-ver"
#             while n!=len(rline):
#                 par1='"modname":' in rline[n]
#                 if par1==True:
#                     modname_conf=modname_conf.replace(" ", "")
#                     modname_conf=rline[n]
#                 par2='"mcversion":' in rline[n]
#                 if par2==True:
#                     mcversion_conf=rline[n]
#                 par3='"version:"' in rline[n]
#                 if par3==True:
#                     version_conf=rline[n]
#                     print(version_conf)
#                 n+=1
#             try:
#                 modname_conf=modname_conf.replace('"', '')
#                 modname_conf=modname_conf.replace('modname: ', '')
#                 modname_conf=modname_conf.replace(',', '')
#             except: 
#                 print(Exception)
#             try:
#                 mcversion_conf=mcversion_conf.replace('"', '')
#                 mcversion_conf=mcversion_conf.replace('mcversion: ', '')
#                 mcversion_conf=mcversion_conf.replace(',', '')
#             except: 
#                 temp+=1
#             try:
#                 version_conf=version_conf.replace('"', '')
#                 version_conf=version_conf.replace('version: ', '')
#                 version_conf=version_conf.replace(',', '')
#                 print(version_conf)
#             except: 
#                 temp+=1
#             if modname_conf!="no-name": 
#                 print(modname)
#                 newmodname=str(modname_conf)+"_"+str(version_conf)+"_"+str(mcversion_conf)+".jar"
#                 print(newmodname)
#                 os.rename(modname, newmodname)
#             else:
#                 print("No modname speciefed in mcmod.info file for "+modname+". Renamer will break")
#         except KeyError: 
#             print("No mcmod.info in -modname- (will be provided in future updates)")