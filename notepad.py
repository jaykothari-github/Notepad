from tkinter import *
from tkinter.messagebox import * 
from tkinter.filedialog import *
import os

rw = Tk()
rw.title("NoteBook")
rw.geometry("800x500+300+100")

texta = Text(rw, wrap="none")
texta.pack(expand=True, fill=BOTH)
menu = Menu(rw)

def newFile():
    global file 
    rw.title("Untitle NoteBook")
    file = None
    texta.delete(1.0,END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Docs","*.txt")])
    
    if file =="":
        file=None
    else:
        rw.title(os.path.basename(file) +" - NoteBook")
        texta.delete(1.0,END)
        f = open(file,"r")
        texta.insert(1.0,f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitle.txt',defaultextension=".txt",
                                filetypes=[("All Files","*.*"),("Text Docs","*.txt")])
        if file == "":
            file = None

        else:
            f = open(file,"w")
            f.write(texta.get(1.0,END))
            f.close()
            rw.title(os.path.basename(file)+" - NoteBook")
        
    else:
        f = open(file,"w")
        f.write(texta.get(1.0,END))
        f.close()


def exitapp():
    rw.destroy()

def cut():
    texta.event_generate(("<<cut>>"))

def copy():
    texta.event_generate(("<<copy>>"))

def paste():
    texta.event_generate(("<<paste>>"))

def hmenu():
    showinfo("About Notepad","JK's Notes")

# File Menu Commands-
filem = Menu(menu,tearoff=0)

filem.add_command(label="New", command=newFile)
filem.add_command(label="Open", command=openFile)
filem.add_command(label="Save As", command=saveFile)

filem.add_separator()
filem.add_command(label="Exit", command=exitapp)
menu.add_cascade(label="File",menu=filem)

# Edit menu Commands-
editm = Menu(menu,tearoff=0)

editm.add_command(label="Cut", command=cut)
editm.add_command(label="Copy", command=copy)
editm.add_command(label="Paste", command=paste)

menu.add_cascade(label="Edit",menu=editm)


# Help Menu Commands-
helpm = Menu(menu,tearoff=0)

helpm.add_command(label="About", command=hmenu)

menu.add_cascade(label="Help",menu=helpm)

rw.config(menu=menu)

# Scroll-
# y axis-
scrolly=Scrollbar(texta)
scrolly.pack(side=RIGHT, fill=Y)
scrolly.config(command=texta.yview)

# x axis-
scrollx=Scrollbar(texta,orient=HORIZONTAL)
scrollx.pack(side=BOTTOM, fill=X)
scrollx.config(command=texta.xview)
texta.config(xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

rw.mainloop()