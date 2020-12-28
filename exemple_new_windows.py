import tkinter as tk
import convertisseurimg2pdf as imgToPdf

def createNewWindow():
    newWindowImgToPdf = tk.Toplevel(app)
    imgToPdf.setup(newWindowImgToPdf)

app = tk.Tk()
buttonExample = tk.Button(app, 
              text="Create new window",
              command=createNewWindow)
buttonExample.pack()

app.mainloop()