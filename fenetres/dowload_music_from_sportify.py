# ------------------------------------------------------
#  Copyright : Thomas LÉPINE  (thomas.lep4@gmail.com)
# ------------------------------------------------------

from __future__ import unicode_literals
import subprocess
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import sys
import os
import youtube_dl

lienSporty = []
windowSpotiyDl = None

''' ERROR : '''
def error(messageError="Erreur rencontrée"):
    messagebox.showinfo(title="Erreur", icon = 'error' , message=messageError)

''' Enregistre au format PDF '''
def dlSpotifyToMp3(inputLink):
    print(inputLink)
    # os.system('pwd')
    # ydl_opts = {}
    # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #     ydl.download(['https://www.youtube.com/watch?v=dQw4w9WgXcQ'])
    # command = 'youtube-dl --extract-audio --id https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    # subprocess.call(command.split(), shell=False)
    command = "spotdl --song https://open.spotify.com/track/2rUsJXt4NeeDiIU6sBvrxo?si=4aac98a61fe14527"
    subprocess.call(command, shell=False)
    
    # error(texte)
    # else :
    # global lienSporty
    # if len(lienSporty) == 0 : # Aucun fichier n'a été selectionné
    #     error("Aucune image n'a été selectionné\n\nMerci de selectionner une ou plusieurs images avant")
    # else :
    #     filePathExport = filedialog.asksaveasfilename(defaultextension='.pdf', filetypes = [("Fichier PDF","*.pdf")])
    #     lienSporty[0].save(filePathExport, save_all=True, append_images=lienSporty[1:]) # Transformation de la liste d'image en un pdf

''' Quitte l'application : '''
def exit():
    global windowSpotiyDl
    msgBox = messagebox.askquestion('Quitter l\'application','Êtes-vous sûr et certain de vouloir quitter l\'application ?', icon = 'warning')
    if msgBox == 'yes':
       windowSpotiyDl.destroy()
       windowSpotiyDl = None

''' HELP : '''
def help():
    messagebox.showinfo(title="Aide", icon = 'question' , message="Ce programme permet de télécharger une musique ou une playlist Spotify (avec conversion de la/les musique(s) en .mp3).\n\n\nProgramme développé par Thomas Lépine (thomas.lep4@gmail.com)")

# Options de la fenêtre :
windowOptions = {'width':900, 'height':550, 'background':"#81b71a"}

# Options des bouttons :
butonsOptions = {
    'policeButons':"Ebrima",
    'sizeButons':15,
    'sizeInput':50,
    'textButonDownload':"  Téléchargement  ",
    'colorButonDownload':"#2D3819",
    'textButonHelp':"     Aide     ",
    'colorButonHelp':"#2CA1B8",
    'textButonExit':"   Quitter   ",
    'colorButonExit':"#B80753",
    'textButonMenu':"    Menu    ",
    'colorButonMenu':"#4B2CB8",
}

# SETUP : ---------------------------------------------
def setup():
    global windowSpotiyDl
    windowSpotiyDl.title('Tool : Download Spotift music(s)')
    windowSpotiyDl.iconbitmap("./assets/logo_multi_tools.ico")
    windowSpotiyDl.config(background=windowOptions['background'])
    windowSpotiyDl.geometry(str(windowOptions['width']) + "x" + str(windowOptions['height']))
    windowSpotiyDl.minsize(880, 500)
    ####### ---------------------------------------------

    #Création de la "boîte" frame
    canvas = Frame(windowSpotiyDl, background = windowOptions['background'])
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

    #Boutons & Champs ------------------------------------------
    butonsFrame = Frame(canvas, background = windowOptions['background'])
    # ---
    # INPUT LINK :
    inputAndLabel = Frame(butonsFrame, background = windowOptions['background'])
    labelForInput = Label(inputAndLabel, text='Renseignez le lien ci-dessous :', background = windowOptions['background'], font=(butonsOptions['policeButons'], butonsOptions['sizeButons'], 'bold'), fg='#000') # border=2, relief=SUNKEN
    labelForInput.grid(row=0, column=0, sticky=W)
    inputLink = StringVar()
    ihmLinkInput = Entry(inputAndLabel, width=butonsOptions['sizeInput'], exportselection=0, textvariable=inputLink)
    ihmLinkInput.grid(row=1, column=0, sticky=W)
    inputAndLabel.pack(pady=windowOptions['height']/20)

    # BUTTON DOWNLOAD
    convertButton = Button(butonsFrame, text=butonsOptions['textButonDownload'], command=lambda: dlSpotifyToMp3(inputLink.get()), background=butonsOptions['colorButonDownload'], fg='#9DC356', font=(butonsOptions['policeButons'], butonsOptions['sizeButons'], 'bold'))
    convertButton.pack(pady=windowOptions['height']/80)
    # ---
    bottomButonsFrame = Frame(butonsFrame, background = windowOptions['background'])
    helpButton = Button (bottomButonsFrame, text=butonsOptions['textButonHelp'], command=help, background=butonsOptions['colorButonHelp'], fg='black', font=(butonsOptions['policeButons'], butonsOptions['sizeButons'], 'bold'))
    helpButton.grid(row=0, column=0, sticky=W)

    espaceG = Label(bottomButonsFrame, text='              ', background = windowOptions['background'])
    espaceG.grid(row=0, column=1, sticky=W)

    exitButton = Button (bottomButonsFrame, text=butonsOptions['textButonExit'], command=exit, background=butonsOptions['colorButonExit'], fg='black', font=(butonsOptions['policeButons'], butonsOptions['sizeButons'], 'bold'))
    exitButton.grid(row=0, column=4, sticky=W)
    bottomButonsFrame.pack(pady=windowOptions['height']/15)

    butonsFrame.grid(row=2, column=0, sticky=S)
    ####### ---------------------------------------------

    canvas.pack(expand=YES)
    windowSpotiyDl.mainloop()


windowSpotiyDl = Tk()
setup() # Lancement de la fenêtre
