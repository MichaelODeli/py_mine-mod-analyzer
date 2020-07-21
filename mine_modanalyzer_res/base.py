import random
import os
import time
verfile=open('ver.txt', 'r')
ver=verfile.read()
verfile.close
def launcher():
    i=1
    randomint=1
    while i<6:
        # В будущем тут будет цикл for и будем анализировать каждый файл из папки с модификациями.
        # Пока что, тут рандомный тикер.
        print('Please, be patient! Program is loading...')
        x='####'
        x=x*i
        print(x)
        randomint=random.randint(1,3)
        time.sleep(randomint)
        i+=1
        os.system("cls")
    print("Program is loaded")

def header():
    print("Minecraft Mod Analyzer "+ver+". To get help, enter here 'help'.")
    print("Settings and locations you can set in 'settings.ini' file")
    print("----------------------------------------------")
