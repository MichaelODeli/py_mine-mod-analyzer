import os
from mine_modanalyzer_res import base
from mine_modanalyzer_res import minefunc
from mine_modanalyzer_res import modfunc
# выносим все в единый py-файл, это должно повлиять на работоспособность и не надо будет тянуть кучу файлов
os.system("cls")
# base.launcher()
base.welcome()
try: 
    apdir=os.getenv('APPDATA')
    modlocation = apdir+r"/.minecraft/mods"
    e=1
except:
    print("There is no folder with Minecraft and (or) a folder with mods. The application may not work correctly.")
    print("If you have a folder with the game in a different directory (default: AppData-. Minecraft-mods), then install it in the settings file (in development)")
while e==1:
    console_input=[ ]
    console_input = list(map(str,input(' >>>  ').split()))
    if console_input[0]=="help":
        print("You can view additional information on github. https://github.com/MichaelODeli/py_mine-mod-analyzer")

    elif console_input[0]=="q" or console_input[0]=="exit":
        break

    elif console_input[0]=="mine":
        if console_input[1]=="install":
            print("Feature in development.")
        elif console_input[1]=="setcategory":
            print("Feature in development.")
        elif console_input[1]=="launch":
            print("Feature in development.")
        elif console_input[1]=="setdirectory":
            if console_input[2]=="game":
                print("Feature in development.")
            elif console_input[2]=="mod":
                print("Feature in development.")
            elif console_input[2]=="backup":
                print("Feature in development.")

    elif console_input[0]=="mod":
        if console_input[1]=="name":
            print("Feature in development.")
        elif console_input[1]=="install":
            print("Feature in development.")
        elif console_input[1]=="remove":
            print("Feature in development.")
        elif console_input[1]=="disable":
            modfunc.dismod()
        elif console_input[1]=="enable":
            modfunc.enamod()
        elif console_input[1]=="info":
            print("Feature in development.")
        elif console_input[1]=="backup":
            print("Feature in development.")
        elif console_input[1]=="check":
            print("Feature in development.")
        elif console_input[1]=="update":
            print("Feature in development.")
        elif console_input[1]=="list":
            try:
                if console_input[2]=="disable":
                    modfunc.listmoddis()
                elif console_input[2]=="enable":
                    modfunc.listmodena()
            except:
                modfunc.listmodall()

    

    else:
        print("Unknown command. Try again or type 'info'.")
input("Press Enter to exit ")