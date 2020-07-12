import os
from mine_modanalyzer_res import base
from mine_modanalyzer_res import minefunc
from mine_modanalyzer_res import modfunc
os.system("cls")
base.launcher()
base.welcome()
e = 1

while e==1:
    console_input=[ ]
    console_input = list(map(str,input('>>> ').split()))
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
            if console_input[2]=="mod":
                print("Feature in development.")
            if console_input[2]=="backup":
                print("Feature in development.")

    elif console_input[0]=="mod":
        if console_input[1]=="name":
            print("Feature in development.")
        if console_input[1]=="install":
            print("Feature in development.")
        if console_input[1]=="remove":
            print("Feature in development.")
        if console_input[1]=="disable":
            print("Feature in development.")
        if console_input[1]=="enable":
            print("Feature in development.")
        if console_input[1]=="info":
            print("Feature in development.")
        if console_input[1]=="backup":
            print("Feature in development.")
        if console_input[1]=="check":
            print("Feature in development.")
        if console_input[1]=="update":
            print("Feature in development.")
        if console_input[1]=="list":
            print("Feature in development.")

    

    else:
        print("Unknown command. Try again or type 'info'.")
input()