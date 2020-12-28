# ------------------------------------------------------
#  Copyright : Thomas LÉPINE  (thomas.lep4@gmail.com)
# ------------------------------------------------------

from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import tkinter
from PIL import Image
import sys
import convertisseurimg2pdf as imgToPdf

def createWindowImgToPdf():
    newWindowImgToPdf = Toplevel(mainApp)
    mainApp.state("iconic")
    #  http://tkinter.fdex.eu/doc/toplww.html#Toplevel.state
    imgToPdf.createWindowImgToPdf(newWindowImgToPdf)

def welcomeBackToMenu():
    mainApp.deiconify()

def setupMain():
    print("ok")

mainApp = Tk()
buttonExample = Button(mainApp, text="Convertisseur img2pdf", command=createWindowImgToPdf)
buttonExample.pack()



mainApp.mainloop()
