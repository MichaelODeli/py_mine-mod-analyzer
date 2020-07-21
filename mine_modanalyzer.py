import os
from mine_modanalyzer_res import base #some base func
from mine_modanalyzer_res import minefunc #minecraft func (directory, and other)
from mine_modanalyzer_res import modfunc #mod functions
os.system("cls") #clear console output
# base.launcher()
base.header()

# тут в скором времени будет проверка файла с настройками, с помощью модуля ---
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
        # print("Я не хочу нагружать программу лишними командами") - translate it
    
    elif console_input[0]=="q" or console_input[0]=="exit":
        break

    elif console_input[0]=='clear':
        os.system("cls")
        base.header()

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
            if console_input[1]=="nameid":
                modfunc.renamerid()
            elif console_input[1]=="namever":
                modfunc.renamerver()
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
            print("Error. Not enough arguments. Watch our help page and enter the correct command.")
    
    elif console_input[0]=="getmcmod":
        modfunc.mcmodanalyze()
    
    else:
        print("Unknown command.  Watch our help page and enter the correct command.")
input("Press Enter key to shutdown. ")