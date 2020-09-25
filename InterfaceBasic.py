
from tkinter import *
from pathlib import Path
import openpyxl
import csv
import pandas as pd
import xlsxwriter
from C2 import*
import numpy as np
from Assister import*
from ExcelTransform import*

root = Tk()
root.title("Integrator and Peak Finder!")



e = Entry(root, width =35, borderwidth =5)
e.grid(row = 1, column = 0, columnspan = 3, padx = 10, pady = 10)

def MassFinder(Name,num):
    pathlist = Path(Name).glob('**/*.txt')
    for path in pathlist:
         # because path is object not string
        path_in_str = str(path)
        input_file = path_in_str
        fname = input_file
        count = 0
        g = []
        with open(fname, 'r') as f:
            for line in f:
                g.append(line.split( ))
                count += 1
        df = pd.DataFrame(g) #For any file gets the data frame version

        numofmass = num #Number of Mass 
        numofpoints = int(df.iloc[10,3]) #Length of data vector
        identity = [input_file]
        masslist = []
        for num in range(0,numofmass):
            mass = df.iloc[8+num*(numofpoints+8),2]
            masslist.append(mass)
        break
    return masslist
def run1():
    global location
    location = e.get()
    info1 = Label(root, text = 'How many points are there in your file?').grid(row = 3, column = 0, columnspan = 2)
    global e6
    e6 = Entry(root, width = 35, borderwidth = 5)
    e6.grid(row = 4, column = 0, columnspan = 3, padx = 10, pady = 10)
    extrabutton = Button(root, text = 'Ok', padx = 5, pady = 5, command = finalfinder)
    extrabutton.grid(row = 5, column = 2)

def finalfinder():
    global num1
    num1 = int(e6.get())
    global Masses
    Masses = MassFinder(location, num1)
    finalinfo = Label(root, text = "What do you want to name you file?").grid(row = 6, column = 0, columnspan = 2)
    global e4
    e4 = Entry(root, width = 35, borderwidth =5)
    e4.grid(row =14, column = 0, columnspan = 3, padx = 10, pady = 10)
    finalbutton = Button(root, text = 'Ok', padx = 5, pady = 5, command = ff)
    finalbutton.grid(row = 7, column = 2)
def ff():
    global name
    name = e4.get()
    finalinfo = Label(root, text = "Macro(No)? If so: 'ExcelSheetname!macroname' ").grid(row = 5, column = 0, columnspan = 2)
    global e5
    e5 = Entry(root, width = 35, borderwidth =5)
    e5.grid(row =8, column = 0, columnspan = 3, padx = 10, pady = 10)
    finalbutton = Button(root, text = 'Ok', padx = 5, pady = 5, command = final)
    finalbutton.grid(row = 9, column = 2)

def final():
    global Macro
    Macro = e5.get()
    if Macro.lower() == "no":
        ExcelTransform(location, Masses,name+"_plot")
    else:
        ExcelTransform(location, Masses,name+"_plot",macro = Macro)
    Finish = Label(root, text = "Done! Check your file Directory").grid(row = 10,column = 3, columnspan = 2)



instruction = Label(root, text = "Enter File Directory").grid(row = 0, column = 0, columnspan = 2)

startbutton = Button(root,text='Ok', padx = 5, pady = 5, command = run1)
startbutton.grid(row = 2,column = 2)





root.mainloop()
