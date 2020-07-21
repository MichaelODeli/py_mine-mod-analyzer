import os
from mine_modanalyzer_res import base
from mine_modanalyzer_res import minefunc
from mine_modanalyzer_res import modfunc
os.system("cls")
# base.launcher()
base.welcome()

# try: 
#     apdir=os.getenv('APPDATA')
#     modlocation = apdir+r"/.minecraft/mods"
#     e=1
# except:
#     print("There is no folder with Minecraft and (or) a folder with mods. The application may not work correctly.")
#     print("If you have a folder with the game in a different directory (default: AppData-. Minecraft-mods), then install it in the settings file (in development)")
e=1
while e==1: 
    try: 
        console_input=[ ]
        console_input = list(map(str,input(' >>>  ').split()))
    except KeyboardInterrupt:
        break

    if console_input==[ ]:
        print("Empty command. Try again. To quit - input 'q', to get help - input 'help'.")

    if console_input[0]=="help" or console_input[0]=="info":
        print("Please, read README.md from this github link. There will no any help commands.")
        print("Я не хочу нагружать программу лишними командами")
    
    elif console_input[0]=="q" or console_input[0]=="exit":
        break

    elif console_input[0]=="mine":
        try:
            if console_input[1]=="install":
                minefunc.mineinstall()
            elif console_input[1]=="setcategory":
                minefunc.minesetcategory()
            elif console_input[1]=="launch":
                minefunc.minelaunch()
            elif console_input[1]=="setdir":
                try:
                    if console_input[2]=="b":
                        minefunc.setdirback()
                    elif console_input[2]=="m":
                        minefunc.setdirmod()
                except IndexError:
                    print("Not enough arguments.")
        except IndexError:
            print("Not enough arguments.")

    elif console_input[0]=="mod":
        try:
            if console_input[1]=="name":
                modfunc.renamer()
            elif console_input[1]=="install":
                modfunc.modinstall()
            elif console_input[1]=="remove" or console_input[1]=="delete":
                modfunc.remmod()
            elif console_input[1]=="disable":
                modfunc.dismod()
            elif console_input[1]=="enable":
                modfunc.enamod()
            elif console_input[1]=="info":
                modfunc.infomod()
            elif console_input[1]=="backup":
                modfunc.backmod()
            elif console_input[1]=="check":
                modfunc.checkmod()   
            elif console_input[1]=="update":
                modfunc.updmod()
            elif console_input[1]=="list":
                try:
                    if console_input[2]=="disable":
                        modfunc.listmoddis()
                    elif console_input[2]=="enable":
                        modfunc.listmodena()
                except:
                    modfunc.listmodall()
        except IndexError:
            print("Error. Try again.")
    
    elif console_input[0]=="getmcmod":
        modfunc.mcmodanalyze()

    else:
        print("Unknown command. Try again or type 'info'.")
input("Press Enter key to shutdown. ")