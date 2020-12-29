# ------------------------------------------------------
#  Copyright : Thomas LÉPINE  (thomas.lep4@gmail.com)
# ------------------------------------------------------

from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
from PIL import Image
import sys

''' VARIABLES GLOBALES '''
imageList = []
mainWindow = None
canvas = None
windowsOptions = {'width': 1000, 'height': 600, 'background-menu': "#AAA", 'background-imgToPdf': "#996B6B"}
''' ################# '''

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
    setupMenu()
    
''' ########################### '''

# SETUPS : ---------------------------------------------
def firstSetup():
    # Options de la fenêtre :
    global windowsOptions
    global mainWindow
    mainWindow.iconbitmap("./assets/logo_multi_tools.ico")
    mainWindow.config(background=windowsOptions['background-menu'])
    mainWindow.geometry(
        str(windowsOptions['width']) + "x" + str(windowsOptions['height']))
    mainWindow.minsize(880, 500)
    mainWindow.title('Multi tools - Menu')
    setupMenu()


def setupMenu():
    global mainWindow
    global canvas
    global windowsOptions
    mainWindow.config(background=windowsOptions['background-menu'])
    mainWindow.title('Multi tools - Menu')
    butonsOptionsMenu = {
        'policeButons': "Ebrima",
        'sizeButons': 15,
        'textButon1': " Convertion \nimage(s) en PDF",
        'colorButon1': "#5C8199",
    }
    #Création de la "boîte" frame
    canvas = Frame(mainWindow, background=windowsOptions['background-menu'])

    ########### HEADER
    header = Frame(canvas, background=windowsOptions['background-menu'])
    width = windowsOptions['width']/4
    height = windowsOptions['height']/4.5
    #Image ---------------------------------------------
    image = PhotoImage(file="./assets/logo_multi_tools.png").zoom(2).subsample(17)
    imageCanvas = Canvas(header, width=width, height=height,
                         background=windowsOptions['background-menu'], border=0, highlightthickness=0)
    imageCanvas.create_image(width/2, height/2, image=image)
    imageCanvas.grid(row=0, column=0, sticky=W)
    ####### --------------------------------------------
    #Titre ---------------------------------------------
    titre = Label(header, text='  ~ MENU ~  ', background=windowsOptions['background-menu'], font=('Ink Free', 30, 'bold'), fg='#000')  # border=2, relief=SUNKEN
    titre.grid(row=0, column=1, sticky=W)
    ####### --------------------------------------------
    #Image ---------------------------------------------
    image2 = PhotoImage(file="./assets/logo_multi_tools.png").zoom(2).subsample(17)
    imageCanvas2 = Canvas(header, width=width, height=height, background=windowsOptions['background-menu'], border=0, highlightthickness=0)
    imageCanvas2.create_image(width/2, height/2, image=image2)
    imageCanvas2.grid(row=0, column=2, sticky=W)
    ####### ---------------------------------------------
    header.grid(row=0, column=0, sticky=N)
    ############## ---------------------------------------------

    ''' BOUTONS : '''
    buttonsFrame = Frame(canvas, background=windowsOptions['background-menu'])

    # Images To Pdf
    butonImgToPDF = Frame(buttonsFrame, background=windowsOptions['background-menu']) # , bd=1, relief=SUNKEN
    imageButtonImgToPdf = PhotoImage(file="./assets/logo_img2pdf.png").zoom(1).subsample(17)
    imgToPdfButton = Button(butonImgToPDF, image=imageButtonImgToPdf, command=test, background=butonsOptionsMenu['colorButon1'])
    imgToPdfButton.pack()
    labelButtonImgToPdf = Label(butonImgToPDF, text=butonsOptionsMenu['textButon1'] , background=windowsOptions['background-menu'], fg='black', font=(butonsOptionsMenu['policeButons'], butonsOptionsMenu['sizeButons'], 'bold'))
    labelButtonImgToPdf.pack()
    butonImgToPDF.grid(row=0, column=0, sticky=W, padx=windowsOptions['width']/50)

    # WIP
    butonImgToPDF = Frame(buttonsFrame, background=windowsOptions['background-menu']) # , bd=1, relief=SUNKEN
    imageButtonImgToPdf = PhotoImage(file="./assets/logo_img2pdf.png").zoom(1).subsample(17)
    imgToPdfButton = Button(butonImgToPDF, image=imageButtonImgToPdf, command=test, background=butonsOptionsMenu['colorButon1'])
    imgToPdfButton.pack()
    labelButtonImgToPdf = Label(butonImgToPDF, text=butonsOptionsMenu['textButon1'] , background=windowsOptions['background-menu'], fg='black', font=(butonsOptionsMenu['policeButons'], butonsOptionsMenu['sizeButons'], 'bold'))
    labelButtonImgToPdf.pack()
    butonImgToPDF.grid(row=0, column=1, sticky=W, padx=windowsOptions['width']/50)

    # WIP
    butonImgToPDF = Frame(buttonsFrame, background=windowsOptions['background-menu']) # , bd=1, relief=SUNKEN
    imageButtonImgToPdf = PhotoImage(file="./assets/logo_img2pdf.png").zoom(1).subsample(17)
    imgToPdfButton = Button(butonImgToPDF, image=imageButtonImgToPdf, command=test, background=butonsOptionsMenu['colorButon1'])
    imgToPdfButton.pack()
    labelButtonImgToPdf = Label(butonImgToPDF, text=butonsOptionsMenu['textButon1'] , background=windowsOptions['background-menu'], fg='black', font=(butonsOptionsMenu['policeButons'], butonsOptionsMenu['sizeButons'], 'bold'))
    labelButtonImgToPdf.pack()
    butonImgToPDF.grid(row=0, column=2, sticky=W, padx=windowsOptions['width']/50)

    # WIP
    butonImgToPDF = Frame(buttonsFrame, background=windowsOptions['background-menu']) # , bd=1, relief=SUNKEN
    imageButtonImgToPdf = PhotoImage(file="./assets/logo_img2pdf.png").zoom(1).subsample(17)
    imgToPdfButton = Button(butonImgToPDF, image=imageButtonImgToPdf, command=test, background=butonsOptionsMenu['colorButon1'])
    imgToPdfButton.pack()
    labelButtonImgToPdf = Label(butonImgToPDF, text=butonsOptionsMenu['textButon1'] , background=windowsOptions['background-menu'], fg='black', font=(butonsOptionsMenu['policeButons'], butonsOptionsMenu['sizeButons'], 'bold'))
    labelButtonImgToPdf.pack()
    butonImgToPDF.grid(row=0, column=3, sticky=W, padx=windowsOptions['width']/50)

    # WIP
    butonImgToPDF = Frame(buttonsFrame, background=windowsOptions['background-menu']) # , bd=1, relief=SUNKEN
    imageButtonImgToPdf = PhotoImage(file="./assets/logo_img2pdf.png").zoom(1).subsample(17)
    imgToPdfButton = Button(butonImgToPDF, image=imageButtonImgToPdf, command=test, background=butonsOptionsMenu['colorButon1'])
    imgToPdfButton.pack()
    labelButtonImgToPdf = Label(butonImgToPDF, text=butonsOptionsMenu['textButon1'] , background=windowsOptions['background-menu'], fg='black', font=(butonsOptionsMenu['policeButons'], butonsOptionsMenu['sizeButons'], 'bold'))
    labelButtonImgToPdf.pack()
    butonImgToPDF.grid(row=0, column=4, sticky=W, padx=windowsOptions['width']/50)

    # WIP
    butonImgToPDF = Frame(buttonsFrame, background=windowsOptions['background-menu']) # , bd=1, relief=SUNKEN
    imageButtonImgToPdf = PhotoImage(file="./assets/logo_img2pdf.png").zoom(1).subsample(17)
    imgToPdfButton = Button(butonImgToPDF, image=imageButtonImgToPdf, command=test, background=butonsOptionsMenu['colorButon1'])
    imgToPdfButton.pack()
    labelButtonImgToPdf = Label(butonImgToPDF, text=butonsOptionsMenu['textButon1'] , background=windowsOptions['background-menu'], fg='black', font=(butonsOptionsMenu['policeButons'], butonsOptionsMenu['sizeButons'], 'bold'))
    labelButtonImgToPdf.pack()
    butonImgToPDF.grid(row=1, column=0, sticky=W, padx=windowsOptions['width']/50, pady=(windowsOptions['height']/20, 0))

    buttonsFrame.grid(row=1, column=0, sticky=W, pady=windowsOptions['height']/8)
    ''' ####### '''

    ########### FOOTER
    footer = Frame(canvas, background=windowsOptions['background-menu']) # , bd=1, relief=SUNKENs
    labelFooter = Label(footer, text="Powered by Thomas Lépine (thomas.lep4@gmail.com)", background=windowsOptions['background-menu'], fg='black', font=(butonsOptionsMenu['policeButons'], 10, 'bold'), justify='right')
    labelFooter.pack(anchor=SE)
    footer.grid(row=2, column=0, sticky=SE)
    ############## ---------------------------------------------
    canvas.pack(expand=YES)
    mainWindow.mainloop()


def setupImgToPDF():
    global mainWindow
    global canvas
    global windowsOptions
    mainWindow.config(background=windowsOptions['background-imgToPdf'])
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

    #Création de la "boîte" frame
    canvas = Frame(mainWindow, background=windowsOptions['background-imgToPdf'])
    ####### ---------------------------------------------

    ########### HEADER
    header = Frame(canvas, background=windowsOptions['background-imgToPdf'])
    width = windowsOptions['width']/4
    height = windowsOptions['height']/4.5
    #Image ---------------------------------------------
    image = PhotoImage(file="./assets/logo_multi_tools.png").zoom(2).subsample(17)
    imageCanvas = Canvas(header, width=width, height=height,
                         background=windowsOptions['background-imgToPdf'], border=0, highlightthickness=0)
    imageCanvas.create_image(width/2, height/2, image=image)
    imageCanvas.grid(row=0, column=0, sticky=W)
    ####### --------------------------------------------
    #Titre ---------------------------------------------
    titre = Label(header, text=' Outil de convertion \n  ~ Image(s) -> PDF ~  ',
                  background=windowsOptions['background-imgToPdf'], font=('Ink Free', 30, 'bold'), fg='#000')  # border=2, relief=SUNKEN
    titre.grid(row=0, column=1, sticky=W)
    ####### --------------------------------------------
    #Image ---------------------------------------------
    image2 = PhotoImage(file="./assets/logo_img2pdf.png").zoom(2).subsample(17)
    imageCanvas2 = Canvas(header, width=width, height=height, background=windowsOptions['background-imgToPdf'], border=0, highlightthickness=0)
    imageCanvas2.create_image(width/2, height/2, image=image2)
    imageCanvas2.grid(row=0, column=2, sticky=W)
    ####### ---------------------------------------------
    header.grid(row=0, column=0, sticky=W)
    ############## ---------------------------------------------

    #Boutons ---------------------------------------------
    buttonsFrame = Frame(canvas, background=windowsOptions['background-imgToPdf'])
    # ---
    getFileButton = Button(buttonsFrame, text=butonsOptionsImgToPDF['textButon1'], command=getFiles, background=butonsOptionsImgToPDF['colorButon1'], font=(
        butonsOptionsImgToPDF['policeButons'], butonsOptionsImgToPDF['sizeButons'], 'bold'), fg='black')
    getFileButton.pack(pady=windowsOptions['height']/20)
    convertButton = Button(buttonsFrame, text=butonsOptionsImgToPDF['textButon2'], command=convertToPdf, background=butonsOptionsImgToPDF['colorButon2'], fg='black', font=(
        butonsOptionsImgToPDF['policeButons'], butonsOptionsImgToPDF['sizeButons'], 'bold'))
    convertButton.pack(pady=windowsOptions['height']/80)
    # ---
    bottomButonsFrame = Frame(
        buttonsFrame, background=windowsOptions['background-imgToPdf'])
    helpButton = Button(bottomButonsFrame, text=butonsOptionsImgToPDF['textButonHelp'], command=helpImgToPdf, background=butonsOptionsImgToPDF['colorButonHelp'], fg='black', font=(
        butonsOptionsImgToPDF['policeButons'], butonsOptionsImgToPDF['sizeButons'], 'bold'))
    helpButton.grid(row=0, column=0, sticky=W)

    espaceG = Label(bottomButonsFrame, text='              ',
                    background=windowsOptions['background-imgToPdf'])
    espaceG.grid(row=0, column=1, sticky=W)

    backMenuButton = Button (bottomButonsFrame, text=butonsOptionsImgToPDF['textButonMenu'], command=goToMenu, background=butonsOptionsImgToPDF['colorButonMenu'], fg='black', font=(butonsOptionsImgToPDF['policeButons'], butonsOptionsImgToPDF['sizeButons'], 'bold'))
    backMenuButton.grid(row=0, column=2, sticky=W)

    espaceD = Label(bottomButonsFrame, text='              ', background = windowsOptions['background-imgToPdf'])
    espaceD.grid(row=0, column=3, sticky=W)

    exitButton = Button(bottomButonsFrame, text=butonsOptionsImgToPDF['textButonExit'], command=exit, background=butonsOptionsImgToPDF['colorButonExit'], fg='black', font=(
        butonsOptionsImgToPDF['policeButons'], butonsOptionsImgToPDF['sizeButons'], 'bold'))
    exitButton.grid(row=0, column=4, sticky=W)
    bottomButonsFrame.pack(pady=windowsOptions['height']/15)

    buttonsFrame.grid(row=2, column=0, sticky=S)
    ####### ---------------------------------------------

    canvas.pack(expand=YES)
    mainWindow.mainloop()


def startMenu():
    global mainWindow
    mainWindow = Tk()
    firstSetup() # Lancement de la fenêtre

# ----- START UP :
startMenu() # Lancement du logiciel