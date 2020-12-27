# ------------------------------------------------------
#  Copyright : Thomas LÉPINE  (thomas.lep4@gmail.com)
# ------------------------------------------------------

# import tkinter as tk
# from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
from PIL import Image
from PIL import ImageTk

imageList = []

''' Récupère le/les fichiers : '''
def getFiles ():
    global imageList
    filePathImport = filedialog.askopenfilenames(parent=window, title='Choisissez un/des fichier(s)')
    lstFilePathImport = list(filePathImport) # Transformation de la liste de chaine en liste Python
    imageList = []
    for file in lstFilePathImport :
        img = Image.open(file)
        imageList.append(img.convert('RGB'))

''' Enregistre au format PDF '''
def convertToPdf ():
    global imageList
    filePathExport = filedialog.asksaveasfilename(defaultextension='.pdf', filetypes = [("Fichier PDF","*.pdf")])
    imageList[0].save(filePathExport, save_all=True, append_images=imageList[1:]) # Transformation de la liste d'image en un pdf

''' Quitte l'application : '''
def exit():
    msgBox = messagebox.askquestion('Quitter l\'application','Êtes-vous sûr et certain de vouloir quitter l\'application ?', icon = 'warning')
    if msgBox == 'yes':
       window.destroy()

# Options de la fenêtre
windowOptions = {'width':950, 'height':700, 'background':"#004875"}

# SETUP : ---------------------------------------------
window = Tk()
window.title('Tool : Image to PDF')
window.iconbitmap("./assets/logo_alligator_news_ico.ico")
window.config(background=windowOptions['background'])
window.geometry(str(windowOptions['width']) + "x" + str(windowOptions['height']))
window.minsize(480, 500)
####### ---------------------------------------------

#Création de la "boîte" frame
canvas = Frame(window, background = windowOptions['background'])
####### ---------------------------------------------

########### HEADER
headerFrame = Frame(canvas, background = windowOptions['background'])
width = 200
height = 100
#Image ---------------------------------------------
imageFrame = Frame(headerFrame, background = windowOptions['background'])
image = PhotoImage(file="./assets/alli.png").zoom(2).subsample(10)
imageCanvas = Canvas(imageFrame, width=width, height=height, background = windowOptions['background'], border=0, highlightthickness=0)
imageCanvas.create_image(width/2, height/2, image=image)
imageCanvas.pack()
imageFrame.grid(row=0, column=0, sticky=N)
####### --------------------------------------------
#Titre ---------------------------------------------
titreFrame = Frame(headerFrame, background = windowOptions['background'])
titre = Label(titreFrame, text='Outil de convertion\n~ Image(s) -> PDF ~', background='#C8C8C8', font=('Ink Free', 30, 'bold'), fg='#000')
titre.pack()
titreFrame.grid(row=0, column=1, sticky=N)
####### --------------------------------------------
#Image ---------------------------------------------
imageFrame2 = Frame(headerFrame, background = windowOptions['background'])
image2 = PhotoImage(file="./assets/alli.png").zoom(2).subsample(10)
imageCanvas2 = Canvas(imageFrame2, width=width, height=height, background = windowOptions['background'], border=0, highlightthickness=0)
imageCanvas2.create_image(width/2, height/2, image=image2)
imageCanvas2.pack()
imageFrame2.grid(row=0, column=2, sticky=N)
####### ---------------------------------------------
headerFrame.grid(row=0, column=0, sticky=N)
############## ---------------------------------------------

#Boutons ---------------------------------------------
butonsFrame = Frame(canvas, background = windowOptions['background'])

getFileButton = Button(butonsFrame, text="        Fichier(s)        ", command=getFiles, background='#E8927C', fg='black', font=('Ebrima', 14, 'bold'))
getFileButton.pack(pady=windowOptions['height']/20)
convertButton = Button(butonsFrame, text='   Convertion en PDF   ', command=convertToPdf, background='#0B8000', fg='black', font=('Ebrima', 14, 'bold'))
convertButton.pack(pady=windowOptions['height']/80)
exitButton = Button (butonsFrame, text='   Quitter   ', command=exit, background='#CD010D', fg='white', font=('Ebrima', 16, 'bold'))
exitButton.pack(pady=windowOptions['height']/10)
butonsFrame.grid(row=2, column=0, sticky=S)
####### ---------------------------------------------

canvas.pack(expand=YES)
window.mainloop()