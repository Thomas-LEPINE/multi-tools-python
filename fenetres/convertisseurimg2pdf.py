# ------------------------------------------------------
#  Copyright : Thomas LÉPINE  (thomas.lep4@gmail.com)
# ------------------------------------------------------

from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
from PIL import Image
import sys

imageList = []
windowImg2Pdf = None

''' ERROR : '''
def error(messageError="Erreur rencontrée"):
    messagebox.showinfo(title="Erreur", icon = 'error' , message=messageError)

''' Récupère le/les fichiers : '''
def getFiles ():
    global imageList
    filePathImport = filedialog.askopenfilenames(parent=windowImg2Pdf, title='Choisissez un/des fichier(s)')
    lstFilePathImport = list(filePathImport) # Transformation de la liste de chaine en liste Python
    imageList = []
    for file in lstFilePathImport :
        try :
            img = Image.open(file)
        except :
            error("Un fichier sélectionné n'est pas dans le format image ou n'est pas convertissable" + "\n\nFichier :\n" + str(file) + "\n\nMessage d'erreur du système : " + str(sys.exc_info()[0]))
        else :
            imageList.append(img.convert('RGB'))

''' Enregistre au format PDF '''
def convertToPdf ():
    global imageList
    if len(imageList) == 0 : # Aucun fichier n'a été selectionné
        error("Aucune image n'a été selectionné\n\nMerci de selectionner une ou plusieurs images avant")
    else :
        filePathExport = filedialog.asksaveasfilename(defaultextension='.pdf', filetypes = [("Fichier PDF","*.pdf")])
        imageList[0].save(filePathExport, save_all=True, append_images=imageList[1:]) # Transformation de la liste d'image en un pdf

''' Quitte l'application : '''
def exit():
    global windowImg2Pdf
    msgBox = messagebox.askquestion('Quitter l\'application','Êtes-vous sûr et certain de vouloir quitter l\'application ?', icon = 'warning')
    if msgBox == 'yes':
       windowImg2Pdf.destroy()
       windowImg2Pdf = None

''' HELP : '''
def help():
    messagebox.showinfo(title="Aide", icon = 'question' , message="Ce programme permet de convertir des images en un fichier pdf.\n\n1 : Chargez la ou les images souhaitées à l'aide du boutton \"Fichier(s)\".\n\n2 : Cliquez sur \"Convertir en PDF\" et selectionnez le dossier dans lequel vous souhaitez enregistrer le PDF.\n\nEt voilà ! Vous pouvez ensuite quitter l'application (n'hésitez pas à aller vérifier que la convertion a bien fontionné !)\n\n\nProgramme développé par Thomas Lépine (thomas.lep4@gmail.com)")

# Options de la fenêtre :
windowOptions = {'width':900, 'height':550, 'background':"#996B6B"} # Bleu foncé : 004875 \\ Marron : 996B6B

# Options des bouttons :
butonsOptions = {
    'policeButons':"Ebrima",
    'sizeButons':15,
    'textButon1':"        Fichier(s)        ",
    'colorButon1':"#5C8199",
    'textButon2':"  Convertir en PDF  ",
    'colorButon2':"#6B9978",
    'textButonHelp':"     Aide     ",
    'colorButonHelp':"#996399",
    'textButonMenu':"    Menu    ",
    'colorButonMenu':"#639991",
    'textButonExit':"   Quitter   ",
    'colorButonExit':"#E55C5C",
    }

# SETUP : ---------------------------------------------
def setup():
    global windowImg2Pdf
    windowImg2Pdf.title('Tool : Image to PDF')
    windowImg2Pdf.iconbitmap("./assets/logo_multi_tools.ico")
    windowImg2Pdf.config(background=windowOptions['background'])
    windowImg2Pdf.geometry(str(windowOptions['width']) + "x" + str(windowOptions['height']))
    windowImg2Pdf.minsize(880, 500)
    ####### ---------------------------------------------

    #Création de la "boîte" frame
    canvas = Frame(windowImg2Pdf, background = windowOptions['background'])
    ####### ---------------------------------------------

    ########### HEADER
    headerFrame = Frame(canvas, background = windowOptions['background'])
    width = 220
    height = 210
    #Image ---------------------------------------------
    image = PhotoImage(file="./assets/logo_multi_tools.png").zoom(2).subsample(17)
    imageCanvas = Canvas(headerFrame, width=width, height=height, background = windowOptions['background'], border=0, highlightthickness=0)
    imageCanvas.create_image(width/2, height/2, image=image)
    imageCanvas.grid(row=0, column=0, sticky=W)
    ####### --------------------------------------------
    #Titre ---------------------------------------------
    titre = Label(headerFrame, text=' Outil de convertion \n  ~ Image(s) -> PDF ~  ', background = windowOptions['background'], font=('Ink Free', 30, 'bold'), fg='#000') # border=2, relief=SUNKEN
    titre.grid(row=0, column=1, sticky=W)
    ####### --------------------------------------------
    #Image ---------------------------------------------
    image2 = PhotoImage(file="./assets/logo_img2pdf.png").zoom(2).subsample(17)
    imageCanvas2 = Canvas(headerFrame, width=width, height=height, background = windowOptions['background'], border=0, highlightthickness=0)
    imageCanvas2.create_image(width/2, height/2, image=image2)
    imageCanvas2.grid(row=0, column=2, sticky=W)
    ####### ---------------------------------------------
    headerFrame.grid(row=0, column=0, sticky=W)
    ############## ---------------------------------------------

    #Boutons ---------------------------------------------
    butonsFrame = Frame(canvas, background = windowOptions['background'])
    # ---
    getFileButton = Button(butonsFrame, text=butonsOptions['textButon1'], command=getFiles, background=butonsOptions['colorButon1'], font=(butonsOptions['policeButons'], butonsOptions['sizeButons'], 'bold'), fg='black')
    getFileButton.pack(pady=windowOptions['height']/20)
    convertButton = Button(butonsFrame, text=butonsOptions['textButon2'], command=convertToPdf, background=butonsOptions['colorButon2'], fg='black', font=(butonsOptions['policeButons'], butonsOptions['sizeButons'], 'bold'))
    convertButton.pack(pady=windowOptions['height']/80)
    # ---
    bottomButonsFrame = Frame(butonsFrame, background = windowOptions['background'])
    helpButton = Button (bottomButonsFrame, text=butonsOptions['textButonHelp'], command=help, background=butonsOptions['colorButonHelp'], fg='black', font=(butonsOptions['policeButons'], butonsOptions['sizeButons'], 'bold'))
    helpButton.grid(row=0, column=0, sticky=W)

    espaceG = Label(bottomButonsFrame, text='              ', background = windowOptions['background'])
    espaceG.grid(row=0, column=1, sticky=W)

    # backMenuButton = Button (bottomButonsFrame, text=butonsOptions['textButonMenu'], command=help, background=butonsOptions['colorButonMenu'], fg='black', font=(butonsOptions['policeButons'], butonsOptions['sizeButons'], 'bold'))
    # backMenuButton.grid(row=0, column=2, sticky=W)

    # espaceD = Label(bottomButonsFrame, text='              ', background = windowOptions['background'])
    # espaceD.grid(row=0, column=3, sticky=W)

    exitButton = Button (bottomButonsFrame, text=butonsOptions['textButonExit'], command=exit, background=butonsOptions['colorButonExit'], fg='black', font=(butonsOptions['policeButons'], butonsOptions['sizeButons'], 'bold'))
    exitButton.grid(row=0, column=4, sticky=W)
    bottomButonsFrame.pack(pady=windowOptions['height']/15)

    butonsFrame.grid(row=2, column=0, sticky=S)
    ####### ---------------------------------------------

    canvas.pack(expand=YES)
    windowImg2Pdf.mainloop()


windowImg2Pdf = Tk()
setup() # Lancement de la fenêtre
