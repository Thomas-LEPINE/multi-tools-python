"""
# ------------------------------------------------------
#  Copyright : Thomas LÉPINE  (thomas.lep4@gmail.com)
# ------------------------------------------------------
"""
__author__ = ("Thomas LÉPINE")
__contact__ = ("thomas.lep4@gmail.com")
__version__ = "0.4.0"
__copyright__ = "Thomas Lépine"
__date__ = "2020/12"

try:
    # pour python 3.x
    from tkinter import *
    from tkinter import filedialog, messagebox
except ImportError:
    # pour python 2.x
    from Tkinter import *
    from Tkinter import filedialog, messagebox
from PIL import Image
import sys
# import this
# import antigravity

''' VARIABLES GLOBALES '''
MAIN_WINDOW = None
WINDOWS_OPTIONS = {'width': 1000, 'height': 680, 'background-menu': "#AAA", 'background-imgToPdf': "#996B6B"}
image_list = []
canvas = None
''' ################# '''

''' ############ FONCTIONS ############### '''
''' ######### IMAGE TO PDF ######### '''
''' Récupère le/les fichiers : '''
def getFilesImages():
    global image_list
    filePathImport = filedialog.askopenfilenames(
        parent=MAIN_WINDOW, title='Choisissez un/des fichier(s)')
    # Transformation de la liste de chaine en liste Python
    lstFilePathImport = list(filePathImport)
    image_list = [] # Réinitialisation de la liste
    for file in lstFilePathImport:
        try :
            img = Image.open(file)
        except :
            image_list = [] # Réinitialisation de la liste
            error("Un fichier sélectionné n'est pas dans le format image ou n'est pas convertissable" +
                  "\n\nFichier :\n" + str(file) + "\n\nMessage d'erreur du système : " + str(sys.exc_info()[0]))
            break
        else :
            image_list.append(img.convert('RGB'))

''' Enregistre au format PDF '''
def convertToPdf():
    global image_list
    if len(image_list) == 0:  # Aucun fichier n'a été selectionné
        error("Aucune image n'a été selectionné\n\nMerci de selectionner une ou plusieurs images avant")
    else:
        filePathExport = filedialog.asksaveasfilename(
            defaultextension='.pdf', filetypes=[("Fichier PDF", "*.pdf")])
        # Transformation de la liste d'image en un pdf
        image_list[0].save(filePathExport, save_all=True,
                          append_images=image_list[1:])

''' HELP : '''
def helpImgToPdf():
    messagebox.showinfo(title="Aide", icon='question', message="Ce programme permet de convertir des images en un fichier pdf.\n\n1 : Chargez la ou les images souhaitées à l'aide du boutton \"Fichier(s)\".\n\n2 : Cliquez sur \"Convertir en PDF\" et selectionnez le dossier dans lequel vous souhaitez enregistrer le PDF.\n\nEt voilà ! Vous pouvez ensuite quitter l'application (n'hésitez pas à aller vérifier que la convertion a bien fontionné !)\n\n\nProgramme développé par Thomas Lépine (thomas.lep4@gmail.com)")

''' ######### MENU ######### '''
''' GO TO IMAGE TO PDF : '''
def test():
    global canvas
    canvas.pack_forget()
    setupImgToPDF()
   

''' ######### GLOBAL ######### '''
''' Quitte l'application : '''
def exit():
    global MAIN_WINDOW
    msgBox = messagebox.askquestion(
        'Quitter l\'application', 'Êtes-vous sûr et certain de vouloir quitter l\'application ?', icon='warning')
    if msgBox == 'yes':
       MAIN_WINDOW.destroy()
       MAIN_WINDOW = None

''' ERROR : '''
def error(messageError="Erreur rencontrée"):
    messagebox.showinfo(title="Erreur", icon='error', message=messageError)

''' BACK TO THE MENU : '''
def goToMenu():
    global canvas
    global image_list
    image_list = [] # Réinitialisation de la liste
    canvas.pack_forget()
    setupMenu()
    
''' ########################### '''

# SETUPS : ---------------------------------------------
def firstSetup():
    # Options de la fenêtre :
    global MAIN_WINDOW
    MAIN_WINDOW.iconbitmap("./assets/logo_multi_tools.ico")
    MAIN_WINDOW.config(background=WINDOWS_OPTIONS['background-menu'])
    MAIN_WINDOW.geometry(
        str(WINDOWS_OPTIONS['width']) + "x" + str(WINDOWS_OPTIONS['height']))
    MAIN_WINDOW.minsize(1000, 600)
    MAIN_WINDOW.title('Multi tools - Menu')
    setupMenu()


def setupMenu():
    global MAIN_WINDOW
    global canvas
    MAIN_WINDOW.config(background=WINDOWS_OPTIONS['background-menu'])
    MAIN_WINDOW.title('Multi tools - Menu')
    butonsOptionsMenu = {
        'policeButons': "Ebrima",
        'sizeButons': 15,
        'textButonImgToPdf': " Convertion \nimage(s) en PDF",
        'colorButonImgToPdf': "#5C8199",
        'textButonCompressionImg': " Compression \nimage(s)",
        'colorButonCompressionImg': "#5C8199",

        'textButonWip': " WIP ",
        'colorButonWip': "#ccc",
    }
    #Création de la "boîte" frame
    canvas = Frame(MAIN_WINDOW, background=WINDOWS_OPTIONS['background-menu'])

    ########### HEADER
    header = Frame(canvas, background=WINDOWS_OPTIONS['background-menu'])
    width = WINDOWS_OPTIONS['width']/4
    height = WINDOWS_OPTIONS['height']/4.5
    #Image ---------------------------------------------
    image = PhotoImage(file="./assets/cpu_vieux.png").zoom(2).subsample(18)
    imageCanvas = Canvas(header, width=width, height=height,
                         background=WINDOWS_OPTIONS['background-menu'], border=0, highlightthickness=0)
    imageCanvas.create_image(width/2, height/2, image=image)
    imageCanvas.grid(row=0, column=0, sticky=W)
    ####### --------------------------------------------
    #Titre ---------------------------------------------
    titre = Label(header, text='  ~ MENU ~  ', background=WINDOWS_OPTIONS['background-menu'], font=('Ink Free', 30, 'bold'), fg='#000')  # border=2, relief=SUNKEN
    titre.grid(row=0, column=1, sticky=W)
    ####### --------------------------------------------
    #Image ---------------------------------------------
    image2 = PhotoImage(file="./assets/cle_molette.png").zoom(2).subsample(18)
    imageCanvas2 = Canvas(header, width=width, height=height, background=WINDOWS_OPTIONS['background-menu'], border=0, highlightthickness=0)
    imageCanvas2.create_image(width/2, height/2, image=image2)
    imageCanvas2.grid(row=0, column=2, sticky=W)
    ####### ---------------------------------------------
    header.grid(row=0, column=0, sticky=N)
    ############## ---------------------------------------------

    ''' BOUTONS : '''
    buttonsFrame = Frame(canvas, background=WINDOWS_OPTIONS['background-menu'])

    # Images To Pdf
    butonImgToPDF = Frame(buttonsFrame, background=WINDOWS_OPTIONS['background-menu'])
    imageButtonImgToPdf = PhotoImage(file="./assets/logo_img2pdf.png").zoom(1).subsample(12)
    imgToPdfButton = Button(butonImgToPDF, image=imageButtonImgToPdf, command=test, background=butonsOptionsMenu['colorButonImgToPdf'])
    imgToPdfButton.pack()
    labelButtonImgToPdf = Label(butonImgToPDF, text=butonsOptionsMenu['textButonImgToPdf'] , background=WINDOWS_OPTIONS['background-menu'], fg='black', font=(butonsOptionsMenu['policeButons'], butonsOptionsMenu['sizeButons'], 'bold'))
    labelButtonImgToPdf.pack()
    butonImgToPDF.grid(row=0, column=0, sticky=W, padx=WINDOWS_OPTIONS['width']/50)

    # Compression Images
    butonCompressionImages = Frame(buttonsFrame, background=WINDOWS_OPTIONS['background-menu'])
    imageButtonCompressionImages = PhotoImage(file="./assets/logo_compression_images.png").zoom(1).subsample(12)
    imageToCompressionImagesButton = Button(butonCompressionImages, image=imageButtonCompressionImages, command=test, background=butonsOptionsMenu['colorButonCompressionImg'])
    imageToCompressionImagesButton.pack()
    labelButtonCompressionImages = Label(butonCompressionImages, text=butonsOptionsMenu['textButonCompressionImg'] , background=WINDOWS_OPTIONS['background-menu'], fg='black', font=(butonsOptionsMenu['policeButons'], butonsOptionsMenu['sizeButons'], 'bold'))
    labelButtonCompressionImages.pack()
    butonCompressionImages.grid(row=0, column=1, sticky=W, padx=WINDOWS_OPTIONS['width']/50)

    # WIP
    butonWIP = Frame(buttonsFrame, background=WINDOWS_OPTIONS['background-menu']) # , bd=1, relief=SUNKEN
    imageButtonWIP = PhotoImage(file="./assets/logo_img2pdf.png").zoom(1).subsample(12)
    imageToWIPButton = Button(butonWIP, image=imageButtonWIP, command=test, background=butonsOptionsMenu['colorButonWip'])
    imageToWIPButton.pack()
    labelButtonWIP = Label(butonWIP, text=butonsOptionsMenu['textButonWip'] , background=WINDOWS_OPTIONS['background-menu'], fg='black', font=(butonsOptionsMenu['policeButons'], butonsOptionsMenu['sizeButons'], 'bold'))
    labelButtonWIP.pack()
    butonWIP.grid(row=0, column=2, sticky=W, padx=WINDOWS_OPTIONS['width']/50)

    # WIP
    butonWIP = Frame(buttonsFrame, background=WINDOWS_OPTIONS['background-menu']) # , bd=1, relief=SUNKEN
    imageButtonWIP = PhotoImage(file="./assets/logo_img2pdf.png").zoom(1).subsample(12)
    imageToWIPButton = Button(butonWIP, image=imageButtonWIP, command=test, background=butonsOptionsMenu['colorButonWip'])
    imageToWIPButton.pack()
    labelButtonWIP = Label(butonWIP, text=butonsOptionsMenu['textButonWip'] , background=WINDOWS_OPTIONS['background-menu'], fg='black', font=(butonsOptionsMenu['policeButons'], butonsOptionsMenu['sizeButons'], 'bold'))
    labelButtonWIP.pack()
    butonWIP.grid(row=0, column=3, sticky=W, padx=WINDOWS_OPTIONS['width']/50)

    # WIP
    butonWIP = Frame(buttonsFrame, background=WINDOWS_OPTIONS['background-menu']) # , bd=1, relief=SUNKEN
    imageButtonWIP = PhotoImage(file="./assets/logo_img2pdf.png").zoom(1).subsample(12)
    imageToWIPButton = Button(butonWIP, image=imageButtonWIP, command=test, background=butonsOptionsMenu['colorButonWip'])
    imageToWIPButton.pack()
    labelButtonWIP = Label(butonWIP, text=butonsOptionsMenu['textButonWip'] , background=WINDOWS_OPTIONS['background-menu'], fg='black', font=(butonsOptionsMenu['policeButons'], butonsOptionsMenu['sizeButons'], 'bold'))
    labelButtonWIP.pack()
    butonWIP.grid(row=0, column=4, sticky=W, padx=WINDOWS_OPTIONS['width']/50)

    # WIP
    butonWIP = Frame(buttonsFrame, background=WINDOWS_OPTIONS['background-menu']) # , bd=1, relief=SUNKEN
    imageButtonWIP = PhotoImage(file="./assets/cle_molette.png").zoom(1).subsample(12)
    imageToWIPButton = Button(butonWIP, image=imageButtonWIP, command=test, background=butonsOptionsMenu['colorButonWip'])
    imageToWIPButton.pack()
    labelButtonWIP = Label(butonWIP, text=butonsOptionsMenu['textButonWip'] , background=WINDOWS_OPTIONS['background-menu'], fg='black', font=(butonsOptionsMenu['policeButons'], butonsOptionsMenu['sizeButons'], 'bold'))
    labelButtonWIP.pack()
    butonWIP.grid(row=1, column=0, sticky=W, padx=WINDOWS_OPTIONS['width']/50, pady=(WINDOWS_OPTIONS['height']/15, 0))

    # WIP
    butonWIP = Frame(buttonsFrame, background=WINDOWS_OPTIONS['background-menu']) # , bd=1, relief=SUNKEN
    imageButtonWIP = PhotoImage(file="./assets/cle_molette.png").zoom(1).subsample(12)
    imageToWIPButton = Button(butonWIP, image=imageButtonWIP, command=test, background=butonsOptionsMenu['colorButonWip'])
    imageToWIPButton.pack()
    labelButtonWIP = Label(butonWIP, text=butonsOptionsMenu['textButonWip'] , background=WINDOWS_OPTIONS['background-menu'], fg='black', font=(butonsOptionsMenu['policeButons'], butonsOptionsMenu['sizeButons'], 'bold'))
    labelButtonWIP.pack()
    butonWIP.grid(row=1, column=1, sticky=W, padx=WINDOWS_OPTIONS['width']/50, pady=(WINDOWS_OPTIONS['height']/15, 0))

    # WIP
    butonWIP = Frame(buttonsFrame, background=WINDOWS_OPTIONS['background-menu']) # , bd=1, relief=SUNKEN
    imageButtonWIP = PhotoImage(file="./assets/cle_molette.png").zoom(1).subsample(12)
    imageToWIPButton = Button(butonWIP, image=imageButtonWIP, command=test, background=butonsOptionsMenu['colorButonWip'])
    imageToWIPButton.pack()
    labelButtonWIP = Label(butonWIP, text=butonsOptionsMenu['textButonWip'] , background=WINDOWS_OPTIONS['background-menu'], fg='black', font=(butonsOptionsMenu['policeButons'], butonsOptionsMenu['sizeButons'], 'bold'))
    labelButtonWIP.pack()
    butonWIP.grid(row=1, column=2, sticky=W, padx=WINDOWS_OPTIONS['width']/50, pady=(WINDOWS_OPTIONS['height']/15, 0))

    # WIP
    butonWIP = Frame(buttonsFrame, background=WINDOWS_OPTIONS['background-menu']) # , bd=1, relief=SUNKEN
    imageButtonWIP = PhotoImage(file="./assets/cle_molette.png").zoom(1).subsample(12)
    imageToWIPButton = Button(butonWIP, image=imageButtonWIP, command=test, background=butonsOptionsMenu['colorButonWip'])
    imageToWIPButton.pack()
    labelButtonWIP = Label(butonWIP, text=butonsOptionsMenu['textButonWip'] , background=WINDOWS_OPTIONS['background-menu'], fg='black', font=(butonsOptionsMenu['policeButons'], butonsOptionsMenu['sizeButons'], 'bold'))
    labelButtonWIP.pack()
    butonWIP.grid(row=1, column=3, sticky=W, padx=WINDOWS_OPTIONS['width']/50, pady=(WINDOWS_OPTIONS['height']/15, 0))

    # WIP
    butonWIP = Frame(buttonsFrame, background=WINDOWS_OPTIONS['background-menu']) # , bd=1, relief=SUNKEN
    imageButtonWIP = PhotoImage(file="./assets/cle_molette.png").zoom(1).subsample(12)
    imageToWIPButton = Button(butonWIP, image=imageButtonWIP, command=test, background=butonsOptionsMenu['colorButonWip'])
    imageToWIPButton.pack()
    labelButtonWIP = Label(butonWIP, text=butonsOptionsMenu['textButonWip'] , background=WINDOWS_OPTIONS['background-menu'], fg='black', font=(butonsOptionsMenu['policeButons'], butonsOptionsMenu['sizeButons'], 'bold'))
    labelButtonWIP.pack()
    butonWIP.grid(row=1, column=4, sticky=W, padx=WINDOWS_OPTIONS['width']/50, pady=(WINDOWS_OPTIONS['height']/15, 0))

    buttonsFrame.grid(row=1, column=0, sticky=W, pady=WINDOWS_OPTIONS['height']/10)
    ''' ####### '''

    ########### FOOTER
    footer = Frame(canvas, background=WINDOWS_OPTIONS['background-menu']) # , bd=1, relief=SUNKENs
    labelFooter = Label(footer, text="Powered by Thomas Lépine (thomas.lep4@gmail.com)", background=WINDOWS_OPTIONS['background-menu'], fg='black', font=(butonsOptionsMenu['policeButons'], 10, 'italic'), justify='right')
    labelFooter.pack(anchor=SE)
    footer.grid(row=2, column=0, sticky=SE)
    ############## ---------------------------------------------
    canvas.pack(expand=YES)
    MAIN_WINDOW.mainloop()


def setupImgToPDF():
    global MAIN_WINDOW
    global canvas
    MAIN_WINDOW.config(background=WINDOWS_OPTIONS['background-imgToPdf'])
    MAIN_WINDOW.title('Multi tools - Image(s) to PDF')
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
    canvas = Frame(MAIN_WINDOW, background=WINDOWS_OPTIONS['background-imgToPdf'])
    ####### ---------------------------------------------

    ########### HEADER
    header = Frame(canvas, background=WINDOWS_OPTIONS['background-imgToPdf'])
    width = WINDOWS_OPTIONS['width']/4
    height = WINDOWS_OPTIONS['height']/4.5

    image = PhotoImage(file="./assets/logo_multi_tools.png").zoom(2).subsample(17)
    imageCanvas = Canvas(header, width=width, height=height,
                         background=WINDOWS_OPTIONS['background-imgToPdf'], border=0, highlightthickness=0)
    imageCanvas.create_image(width/2, height/2, image=image)
    imageCanvas.grid(row=0, column=0, sticky=W)

    titre = Label(header, text=' Outil de convertion \n  ~ Image(s) -> PDF ~  ',
                  background=WINDOWS_OPTIONS['background-imgToPdf'], font=('Ink Free', 30, 'bold'), fg='#000')  # border=2, relief=SUNKEN
    titre.grid(row=0, column=1, sticky=W)

    image2 = PhotoImage(file="./assets/logo_img2pdf.png").zoom(2).subsample(17)
    imageCanvas2 = Canvas(header, width=width, height=height, background=WINDOWS_OPTIONS['background-imgToPdf'], border=0, highlightthickness=0)
    imageCanvas2.create_image(width/2, height/2, image=image2)
    imageCanvas2.grid(row=0, column=2, sticky=W)

    header.grid(row=0, column=0, sticky=W)
    ############## ---------------------------------------------

    #Boutons ---------------------------------------------
    buttonsFrame = Frame(canvas, background=WINDOWS_OPTIONS['background-imgToPdf'])
    # ---
    getFileButton = Button(buttonsFrame, text=butonsOptionsImgToPDF['textButon1'], command=getFilesImages, background=butonsOptionsImgToPDF['colorButon1'], font=(
        butonsOptionsImgToPDF['policeButons'], butonsOptionsImgToPDF['sizeButons'], 'bold'), fg='black')
    getFileButton.pack(pady=WINDOWS_OPTIONS['height']/20)
    convertButton = Button(buttonsFrame, text=butonsOptionsImgToPDF['textButon2'], command=convertToPdf, background=butonsOptionsImgToPDF['colorButon2'], fg='black', font=(
        butonsOptionsImgToPDF['policeButons'], butonsOptionsImgToPDF['sizeButons'], 'bold'))
    convertButton.pack(pady=WINDOWS_OPTIONS['height']/80)
    # ---
    bottomButonsFrame = Frame(
        buttonsFrame, background=WINDOWS_OPTIONS['background-imgToPdf'])
    helpButton = Button(bottomButonsFrame, text=butonsOptionsImgToPDF['textButonHelp'], command=helpImgToPdf, background=butonsOptionsImgToPDF['colorButonHelp'], fg='black', font=(
        butonsOptionsImgToPDF['policeButons'], butonsOptionsImgToPDF['sizeButons'], 'bold'))
    helpButton.grid(row=0, column=0, sticky=W)

    backMenuButton = Button (bottomButonsFrame, text=butonsOptionsImgToPDF['textButonMenu'], command=goToMenu, background=butonsOptionsImgToPDF['colorButonMenu'], fg='black', font=(butonsOptionsImgToPDF['policeButons'], butonsOptionsImgToPDF['sizeButons'], 'bold'))
    backMenuButton.grid(row=0, column=2, sticky=W, padx = WINDOWS_OPTIONS['width']/15)

    exitButton = Button(bottomButonsFrame, text=butonsOptionsImgToPDF['textButonExit'], command=exit, background=butonsOptionsImgToPDF['colorButonExit'], fg='black', font=(
        butonsOptionsImgToPDF['policeButons'], butonsOptionsImgToPDF['sizeButons'], 'bold'))
    exitButton.grid(row=0, column=4, sticky=W)
    bottomButonsFrame.pack(pady=(WINDOWS_OPTIONS['height']/5, 0))

    buttonsFrame.grid(row=2, column=0, sticky=S, pady=(WINDOWS_OPTIONS['height']/15, 0))
    ####### ---------------------------------------------

    # ########### FOOTER
    # footer = Frame(canvas, background = WINDOWS_OPTIONS['background-imgToPdf']) # , bd=1, relief=SUNKENs
    # labelFooter = Label(footer, text="Powered by Thomas Lépine (thomas.lep4@gmail.com)", background = WINDOWS_OPTIONS['background-imgToPdf'], fg='black', font=(butonsOptionsImgToPDF['policeButons'], 10, 'italic'), justify='right')
    # labelFooter.pack(anchor=SE)
    # footer.grid(row=3, column=0, sticky=SE, pady=((WINDOWS_OPTIONS['height']/10, 0)))
    # ############## ---------------------------------------------

    canvas.pack(expand=YES)
    MAIN_WINDOW.mainloop()


def startMenu():
    global MAIN_WINDOW
    MAIN_WINDOW = Tk()
    firstSetup() # Lancement de la fenêtre

# ----- START UP :
startMenu() # Lancement du logiciel