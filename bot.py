# Import based on what you wanna do


# imports for creating a bot to inject code into a notepad txt file

import pymem
import subprocess
import time


# function to automate running the injector
def automater(file):
    try:
        pm = pymem.Pymem(file)
        injector(injectedCode,pm)
    except:
        subprocess.Popen([file])
        pm = pymem.Pymem(file)
        injector(injectedCode,pm)
    

# function for injecting code into a text file
def injector(code,pm):
    pm.inject_python_interpreter()
    pm.inject_python_shellcode(code)


injectedCode =  """

import tkinter as tk

win = tk.Tk()
win.mainloop()

"""


fileType = 'notepad.exe'
while True:
    automater(fileType)
    time.sleep(10)  # Introduce a delay of 10 seconds between injections


