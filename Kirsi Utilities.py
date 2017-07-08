###########
# Kirsi Utilities
# Version 0.1
# Made by Kirsi
# Links:
#   Discord: https://discord.gg/vj9z69Q
#   Github: https://github.com/mushi88
###########

import threading
import sys
import time
import os

Threads = {}
cls = True

def IsInt(Var):
    try:
        int(Var)
        return True
    except:
        return False

def PlatErr():
    print("Kirsi's Utilities currently only works on the Windows OS.")
    time.sleep(5)
    exit()

# --- Threading Functions --- #

def TaskKillThread(Task, Dud):
    while 1:
        os.system("taskkill /im "+Task+" /f >nul 2>nul")

def AutoStartThread(File, Location):
    while 1:
        os.system("start /wait "+File)

# --- Mainloop --- #

def MainLoop():
    while 1:
        if cls: os.system("cls")
        print("Enter the number corrisponding to what you wish to do:\n\
        1. Auto Kill a Task\n\
        2. Run a file, auto starting it when it closes.")

        Selection = input(">>> ")
        if IsInt(Selection):
            Selection = int(Selection)
            if Selection <= 2 and Selection > 0:
                if Selection == 1: Taskkill()
                if Selection == 2: Autostart()
            else:
                continue
        else:
            continue

# --- Util Funcs --- #

def Taskkill():
    if cls: os.system("cls")
    Task = input("Enter task (e.g. chrome.exe):\n>>> ")
    try:
        TempTask = Threads["TaskKill - "+Task]
        print("Task is already being killed.")
        time.sleep(5)
    except:
        Thread = threading.Thread(target = TaskKillThread, args = (Task, False))
        Thread.start()
        Threads["TaskKill - "+Task] = Thread

def Autostart():
    if cls: os.system("cls")
    print("Please note; this feature only works with files in the same \nfolder as Kirsi Utilities!\n")
    OFile = input("Drag and drop the file on this window.\nFile: ")
    try:
        TempTask = Threads["AutoRun - "+OFile]
        print("File is already being auto-started.")
        time.sleep(5)
    except:
        try:
            TempLocation = OFile.split("\\")
            Location  = ""
            File = ""
            Skip = False

            for x in range(len(TempLocation)):
                if not x == len(TempLocation) - 1:
                    Location += TempLocation[x] + "\\\\"
                else:
                    File = TempLocation[x]

            for char in Location:
                if char in "\"":
                    Location=Location.replace(char,'')
            for char in File:
                if char in "\"":
                    File=File.replace(char,'')

            TempFileName = File.split(".")
            FileName = ""

            for x in range(len(TempFileName)):
                if not x >= len(TempFileName) - 2:
                    FileName += TempFileName[x] + "."
                elif not x == len(TempFileName) - 1:
                    FileName += TempFileName[x]

            os.system('powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut(\''+os.getcwd()+'\\'+FileName+'.lnk\');$s.TargetPath=\''+Location+File+'\';$s.Save()"')

            os.system("cd '"+Location+"'")
            os.system("cd /d '"+Location+"'")

            FileName = FileName.replace(" ",'" "')

            Thread = threading.Thread(target = AutoStartThread, args = (os.getcwd()+'\\'+FileName+'.lnk', Location))
            Thread.start()
            Threads["TaskKill - "+OFile] = Thread
        except:
            if cls: os.system("cls")
            print("File not found!")
            time.sleep(5)

if sys.platform != "win32": PlatErr
MainLoop()
