"""
# ------------------------------------------------------
#  Copyright : Thomas LÉPINE  (thomas.lep4@gmail.com)
# ------------------------------------------------------
"""
__author__ = ("Thomas LÉPINE")
__contact__ = ("thomas.lep4@gmail.com")
__version__ = "1.0.0"
__copyright__ = "Thomas Lépine"
__date__ = "2020/12"

from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image
import sys

''' VARIABLES GLOBALES '''
MAIN_WINDOW = None
WINDOWS_OPTIONS = {'width': 1000, 'height': 680, 'background-compressionImg': "#5C8199"}
image_list = []
canvas = None
''' ################# '''
''' ######### COMPRESSION DES IMAGES ######### '''
''' Récupère le/les fichiers : '''
def getFilesImages():
    global image_list
    filePathImport = filedialog.askopenfilenames(
        parent=MAIN_WINDOW, title='Choisissez un/des fichier(s)')
    # Transformation de la liste de chaine en liste Python
    lstFilePathImport = list(filePathImport)
    image_list = []
    for file in lstFilePathImport:
        try:
            img = Image.open(file)
        except:
            error("Un fichier sélectionné n'est pas dans le format image ou n'est pas convertissable" +
                  "\n\nFichier :\n" + str(file) + "\n\nMessage d'erreur du système : " + str(sys.exc_info()[0]))
        else:
            image_list.append(img.convert('RGB'))

''' Compression des images '''
def convertToPdf():
    global image_list
    if len(image_list) == 0:  # Aucun fichier n'a été selectionné
        error("Aucune image n'a été selectionné\n\nMerci de selectionner une ou plusieurs images avant")
    else:
        filePathExport = filedialog.asksaveasfilename(
            defaultextension='.pdf', filetypes=[("Fichier PDF", "*.pdf")])
        # Transformation de la liste d'image en un pdf
        image_list[0].save(filePathExport, save_all=True, append_images=image_list[1:])

''' ERROR : '''
def error(messageError="Erreur rencontrée"):
    messagebox.showinfo(title="Erreur", icon='error', message=messageError)


''' HELP : '''
def helpCompressionImg():
    messagebox.showinfo(title="Aide", icon='question', message="Ce programme permet de convertir des images en un fichier pdf.\n\n1 : Chargez la ou les images souhaitées à l'aide du boutton \"Fichier(s)\".\n\n2 : Cliquez sur \"Convertir en PDF\" et selectionnez le dossier dans lequel vous souhaitez enregistrer le PDF.\n\nEt voilà ! Vous pouvez ensuite quitter l'application (n'hésitez pas à aller vérifier que la convertion a bien fontionné !)\n\n\nProgramme développé par Thomas Lépine (thomas.lep4@gmail.com)")

def setupCompressionImg():
    global MAIN_WINDOW
    global canvas
    MAIN_WINDOW.config(background=WINDOWS_OPTIONS['background-compressionImg'])
    MAIN_WINDOW.title('Multi tools - Compression d\'image(s)')
    # Options des bouttons :
    butonsOptionsCompressionImg = {
        'policeButons': "Ebrima",
        'sizeButons': 15,
        'textButon1': "        Fichier(s)        ",
        'colorButon1': "#E5B5A1",
        'textButon2': "  Convertir en PDF  ",
        'colorButon2': "#998B54",
        'textButonHelp': "     Aide     ",
        'colorButonHelp': "#CC8566",
        'textButonMenu': "    Menu    ",
        'colorButonMenu': "#666ECC",
        'textButonExit': "   Quitter   ",
        'colorButonExit': "#E55CE3",
    }

    #Création de la "boîte" frame
    canvas = Frame(MAIN_WINDOW, background=WINDOWS_OPTIONS['background-compressionImg'])
    ####### ---------------------------------------------

    ########### HEADER
    header = Frame(canvas, background=WINDOWS_OPTIONS['background-compressionImg'])
    width = WINDOWS_OPTIONS['width']/4
    height = WINDOWS_OPTIONS['height']/4.5

    image = PhotoImage(file="./assets/logo_multi_tools.png").zoom(2).subsample(17)
    imageCanvas = Canvas(header, width=width, height=height,
                         background=WINDOWS_OPTIONS['background-compressionImg'], border=0, highlightthickness=0)
    imageCanvas.create_image(width/2, height/2, image=image)
    imageCanvas.grid(row=0, column=0, sticky=W)

    titre = Label(header, text='  ~ Outil de compression d\'image(s) ~ ',
                  background=WINDOWS_OPTIONS['background-compressionImg'], font=('Ink Free', 30, 'bold'), fg='#000')  # border=2, relief=SUNKEN
    titre.grid(row=0, column=1, sticky=W)

    image2 = PhotoImage(file="./assets/logo_compression_images.png").zoom(2).subsample(17)
    imageCanvas2 = Canvas(header, width=width, height=height, background=WINDOWS_OPTIONS['background-compressionImg'], border=0, highlightthickness=0)
    imageCanvas2.create_image(width/2, height/2, image=image2)
    imageCanvas2.grid(row=0, column=2, sticky=W)

    header.grid(row=0, column=0, sticky=W)
    ############## ---------------------------------------------

    #Boutons ---------------------------------------------
    buttonsFrame = Frame(canvas, background=WINDOWS_OPTIONS['background-compressionImg'])
    # ---
    getFileButton = Button(buttonsFrame, text=butonsOptionsCompressionImg['textButon1'], command=getFilesImages, background=butonsOptionsCompressionImg['colorButon1'], font=(
        butonsOptionsCompressionImg['policeButons'], butonsOptionsCompressionImg['sizeButons'], 'bold'), fg='black')
    getFileButton.pack(pady=WINDOWS_OPTIONS['height']/20)
    convertButton = Button(buttonsFrame, text=butonsOptionsCompressionImg['textButon2'], command=convertToPdf, background=butonsOptionsCompressionImg['colorButon2'], fg='black', font=(
        butonsOptionsCompressionImg['policeButons'], butonsOptionsCompressionImg['sizeButons'], 'bold'))
    convertButton.pack(pady=WINDOWS_OPTIONS['height']/80)
    # ---
    bottomButonsFrame = Frame(
        buttonsFrame, background=WINDOWS_OPTIONS['background-compressionImg'])
    helpButton = Button(bottomButonsFrame, text=butonsOptionsCompressionImg['textButonHelp'], command=helpCompressionImg, background=butonsOptionsCompressionImg['colorButonHelp'], fg='black', font=(
        butonsOptionsCompressionImg['policeButons'], butonsOptionsCompressionImg['sizeButons'], 'bold'))
    helpButton.grid(row=0, column=0, sticky=W)

    espaceG = Label(bottomButonsFrame, text='              ', background=WINDOWS_OPTIONS['background-compressionImg'])
    espaceG.grid(row=0, column=1, sticky=W)

    # backMenuButton = Button (bottomButonsFrame, text=butonsOptionsCompressionImg['textButonMenu'], command=helpCompressionImg, background=butonsOptionsCompressionImg['colorButonMenu'], fg='black', font=(butonsOptionsCompressionImg['policeButons'], butonsOptionsCompressionImg['sizeButons'], 'bold'))
    # backMenuButton.grid(row=0, column=2, sticky=W, padx = WINDOWS_OPTIONS['width']/15)

    espaceD = Label(bottomButonsFrame, text='              ', background = WINDOWS_OPTIONS['background-compressionImg'])
    espaceD.grid(row=0, column=3, sticky=W)

    exitButton = Button(bottomButonsFrame, text=butonsOptionsCompressionImg['textButonExit'], command=exit, background=butonsOptionsCompressionImg['colorButonExit'], fg='black', font=(
        butonsOptionsCompressionImg['policeButons'], butonsOptionsCompressionImg['sizeButons'], 'bold'))
    exitButton.grid(row=0, column=4, sticky=W)
    bottomButonsFrame.pack(pady=(WINDOWS_OPTIONS['height']/5, 0))

    buttonsFrame.grid(row=2, column=0, sticky=S, pady=(WINDOWS_OPTIONS['height']/15, 0))
    ####### ---------------------------------------------

    ########### FOOTER
    footer = Frame(canvas, background = WINDOWS_OPTIONS['background-compressionImg']) # , bd=1, relief=SUNKEN
    labelFooter = Label(footer, text="Powered by Thomas Lépine (thomas.lep4@gmail.com)", background = WINDOWS_OPTIONS['background-compressionImg'], fg='black', font=(butonsOptionsCompressionImg['policeButons'], 10, 'italic'), justify='right')
    labelFooter.pack(anchor=SE)
    footer.grid(row=3, column=0, sticky=SE, pady=((WINDOWS_OPTIONS['height']/10, 0)))
    ############## ---------------------------------------------

    canvas.pack(expand=YES)
    MAIN_WINDOW.mainloop()

MAIN_WINDOW = Tk()
setupCompressionImg()