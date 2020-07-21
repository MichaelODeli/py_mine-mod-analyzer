import os
from mine_modanalyzer_res import base #some base func
from mine_modanalyzer_res import minefunc #minecraft func (directory, and other)
from mine_modanalyzer_res import modfunc #mod functions
import configparser
os.system("cls") # clear console output
base.header()

# config reader
set_name='settings.ini' # settings name file
config=configparser.ConfigParser(comment_prefixes=';', inline_comment_prefixes=';') # set new variable
config.read("settings.ini")
username=config.get('main', 'user_name')
# mod_loc=config.get('location', 'mod_location') # set mod location as mod_loc
# back_loc=config.get("location", "backup_location") # set backup location as back_loc

e=1
while e==1: 
    try: 
        console_input=[ ]
        console_input = list(map(str,input(username+'@ModAnalyzer: ').split()))
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
                        minefunc.setdirback(set_name)
                    elif console_input[2]=="m":
                        minefunc.setdirmod(set_name)
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
                except IndexError:
                    modfunc.listmodall()
        except IndexError:
            print("Error. Not enough arguments. Watch our help page and enter the correct command.")
    
    else:
        print("Unknown command.  Watch our help page and enter the correct command.")
input("Press Enter key to shutdown. ")