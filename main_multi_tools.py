# ------------------------------------------------------
#  Copyright : Thomas LÉPINE  (thomas.lep4@gmail.com)
# ------------------------------------------------------

from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
from PIL import Image
import sys

imageList = []
mainWindow = None
canvas = None
''' ############ FONCTIONS ############### '''
''' ######### IMAGE TO PDF ######### '''
''' Récupère le/les fichiers : '''
def getFiles():
    global imageList
    filePathImport = filedialog.askopenfilenames(
        parent=mainWindow, title='Choisissez un/des fichier(s)')
    # Transformation de la liste de chaine en liste Python
    lstFilePathImport = list(filePathImport)
    imageList = []
    for file in lstFilePathImport:
        try:
            img = Image.open(file)
        except:
            error("Un fichier sélectionné n'est pas dans le format image ou n'est pas convertissable" +
                  "\n\nFichier :\n" + str(file) + "\n\nMessage d'erreur du système : " + str(sys.exc_info()[0]))
        else:
            imageList.append(img.convert('RGB'))

''' Enregistre au format PDF '''
def convertToPdf():
    global imageList
    if len(imageList) == 0:  # Aucun fichier n'a été selectionné
        error("Aucune image n'a été selectionné\n\nMerci de selectionner une ou plusieurs images avant")
    else:
        filePathExport = filedialog.asksaveasfilename(
            defaultextension='.pdf', filetypes=[("Fichier PDF", "*.pdf")])
        # Transformation de la liste d'image en un pdf
        imageList[0].save(filePathExport, save_all=True,
                          append_images=imageList[1:])

''' HELP : '''
def helpImgToPdf():
    messagebox.showinfo(title="Aide", icon='question', message="Ce programme permet de convertir des images en un fichier pdf.\n\n1 : Chargez la ou les images souhaitées à l'aide du boutton \"Fichier(s)\".\n\n2 : Cliquez sur \"Convertir en PDF\" et selectionnez le dossier dans lequel vous souhaitez enregistrer le PDF.\n\nEt voilà ! Vous pouvez ensuite quitter l'application (n'hésitez pas à aller vérifier que la convertion a bien fontionné !)\n\n\nProgramme développé par Thomas Lépine (thomas.lep4@gmail.com)")

''' ######### MENU ######### '''
''' GO TO IMAGE TO PDF : '''
def test():
    global mainWindow
    global canvas
    canvas.pack_forget()
    setupImgToPDF()
   

''' ######### GLOBAL ######### '''
''' Quitte l'application : '''
def exit():
    global mainWindow
    msgBox = messagebox.askquestion(
        'Quitter l\'application', 'Êtes-vous sûr et certain de vouloir quitter l\'application ?', icon='warning')
    if msgBox == 'yes':
       mainWindow.destroy()
       mainWindow = None

''' ERROR : '''
def error(messageError="Erreur rencontrée"):
    messagebox.showinfo(title="Erreur", icon='error', message=messageError)

''' BACK TO THE MENU : '''
def goToMenu():
    global mainWindow
    global canvas
    canvas.pack_forget()
    setupMain()
    
''' ########################### '''

# SETUPS : ---------------------------------------------
def firstSetup():
    # Options de la fenêtre :
    # Bleu foncé : 004875 \\ Marron : 996B6B
    windowOptions = {'width': 900, 'height': 550, 'background': "#AAA"}

    global mainWindow
    mainWindow.iconbitmap("./assets/logo_multi_tools.ico")
    mainWindow.config(background=windowOptions['background'])
    mainWindow.geometry(
        str(windowOptions['width']) + "x" + str(windowOptions['height']))
    mainWindow.minsize(880, 500)
    mainWindow.title('Multi tools - Menu')
    setupMain()


def setupMain():
    global mainWindow
    global canvas
    mainWindow.title('Multi tools - Menu')
    # Bleu foncé : 004875 \\ Marron : 996B6B
    windowOptions = {'width': 900, 'height': 550, 'background': "#AAA"}
    butonsOptionsMenu = {
        'policeButons': "Ebrima",
        'sizeButons': 15,
        'textButon1': "        GO TO       ",
        'colorButon1': "#5C8199",
    }
    #Création de la "boîte" frame
    canvas = Frame(mainWindow, background=windowOptions['background'])
    butonsFrame = Frame(canvas, background=windowOptions['background'])
    helpButton = Button(butonsFrame, text=butonsOptionsMenu['textButon1'], command=test, background=butonsOptionsMenu['colorButon1'], fg='black', font=(
        butonsOptionsMenu['policeButons'], butonsOptionsMenu['sizeButons'], 'bold'))
    helpButton.grid(row=0, column=0, sticky=W)
    testB = Button(butonsFrame, text=butonsOptionsMenu['textButon1'], command=test, background=butonsOptionsMenu['colorButon1'], fg='black', font=(
        butonsOptionsMenu['policeButons'], butonsOptionsMenu['sizeButons'], 'bold'))
    testB.grid(row=0, column=2, sticky=W)
    butonsFrame.pack()
    canvas.pack(expand=YES)
    ####### ---------------------------------------------
    mainWindow.mainloop()


def setupImgToPDF():
    global mainWindow
    global canvas
    mainWindow.title('Multi tools - Image(s) to PDF')
    # Options des bouttons :
    butonsOptionsImgToPDF = {
        'policeButons': "Ebrima",
        'sizeButons': 15,
        'textButon1': "        Fichier(s)        ",
        'colorButon1': "#5C8199",
        'textButon2': "  Convertir en PDF  ",
        'colorButon2': "#6B9978",
        'textButonHelp': "     Aide     ",
        'colorButonHelp': "#996399",
        'textButonMenu': "    Menu    ",
        'colorButonMenu': "#639991",
        'textButonExit': "   Quitter   ",
        'colorButonExit': "#E55C5C",
    }

    # Options de la fenêtre :
    # Bleu foncé : 004875 \\ Marron : 996B6B
    windowOptionsImgToPDF = {'width': 900,
                             'height': 550, 'background': "#996B6B"}

    #Création de la "boîte" frame
    canvas = Frame(mainWindow, background=windowOptionsImgToPDF['background'])
    ####### ---------------------------------------------

    ########### HEADER
    headerFrame = Frame(canvas, background=windowOptionsImgToPDF['background'])
    width = 220
    height = 210
    #Image ---------------------------------------------
    image = PhotoImage(
        file="./assets/logo_multi_tools.png").zoom(2).subsample(17)
    imageCanvas = Canvas(headerFrame, width=width, height=height,
                         background=windowOptionsImgToPDF['background'], border=0, highlightthickness=0)
    imageCanvas.create_image(width/2, height/2, image=image)
    imageCanvas.grid(row=0, column=0, sticky=W)
    ####### --------------------------------------------
    #Titre ---------------------------------------------
    titre = Label(headerFrame, text=' Outil de convertion \n  ~ Image(s) -> PDF ~  ',
                  background=windowOptionsImgToPDF['background'], font=('Ink Free', 30, 'bold'), fg='#000')  # border=2, relief=SUNKEN
    titre.grid(row=0, column=1, sticky=W)
    ####### --------------------------------------------
    #Image ---------------------------------------------
    image2 = PhotoImage(file="./assets/logo_img2pdf.png").zoom(2).subsample(17)
    imageCanvas2 = Canvas(headerFrame, width=width, height=height,
                          background=windowOptionsImgToPDF['background'], border=0, highlightthickness=0)
    imageCanvas2.create_image(width/2, height/2, image=image2)
    imageCanvas2.grid(row=0, column=2, sticky=W)
    ####### ---------------------------------------------
    headerFrame.grid(row=0, column=0, sticky=W)
    ############## ---------------------------------------------

    #Boutons ---------------------------------------------
    butonsFrame = Frame(canvas, background=windowOptionsImgToPDF['background'])
    # ---
    getFileButton = Button(butonsFrame, text=butonsOptionsImgToPDF['textButon1'], command=getFiles, background=butonsOptionsImgToPDF['colorButon1'], font=(
        butonsOptionsImgToPDF['policeButons'], butonsOptionsImgToPDF['sizeButons'], 'bold'), fg='black')
    getFileButton.pack(pady=windowOptionsImgToPDF['height']/20)
    convertButton = Button(butonsFrame, text=butonsOptionsImgToPDF['textButon2'], command=convertToPdf, background=butonsOptionsImgToPDF['colorButon2'], fg='black', font=(
        butonsOptionsImgToPDF['policeButons'], butonsOptionsImgToPDF['sizeButons'], 'bold'))
    convertButton.pack(pady=windowOptionsImgToPDF['height']/80)
    # ---
    bottomButonsFrame = Frame(
        butonsFrame, background=windowOptionsImgToPDF['background'])
    helpButton = Button(bottomButonsFrame, text=butonsOptionsImgToPDF['textButonHelp'], command=helpImgToPdf, background=butonsOptionsImgToPDF['colorButonHelp'], fg='black', font=(
        butonsOptionsImgToPDF['policeButons'], butonsOptionsImgToPDF['sizeButons'], 'bold'))
    helpButton.grid(row=0, column=0, sticky=W)

    espaceG = Label(bottomButonsFrame, text='              ',
                    background=windowOptionsImgToPDF['background'])
    espaceG.grid(row=0, column=1, sticky=W)

    backMenuButton = Button (bottomButonsFrame, text=butonsOptionsImgToPDF['textButonMenu'], command=goToMenu, background=butonsOptionsImgToPDF['colorButonMenu'], fg='black', font=(butonsOptionsImgToPDF['policeButons'], butonsOptionsImgToPDF['sizeButons'], 'bold'))
    backMenuButton.grid(row=0, column=2, sticky=W)

    espaceD = Label(bottomButonsFrame, text='              ', background = windowOptionsImgToPDF['background'])
    espaceD.grid(row=0, column=3, sticky=W)

    exitButton = Button(bottomButonsFrame, text=butonsOptionsImgToPDF['textButonExit'], command=exit, background=butonsOptionsImgToPDF['colorButonExit'], fg='black', font=(
        butonsOptionsImgToPDF['policeButons'], butonsOptionsImgToPDF['sizeButons'], 'bold'))
    exitButton.grid(row=0, column=4, sticky=W)
    bottomButonsFrame.pack(pady=windowOptionsImgToPDF['height']/15)

    butonsFrame.grid(row=2, column=0, sticky=S)
    ####### ---------------------------------------------

    canvas.pack(expand=YES)
    mainWindow.mainloop()


def startMenu():
    global mainWindow
    mainWindow = Tk()
    firstSetup() # Lancement de la fenêtre

# ----- START UP :
startMenu() # Lancement du logiciel