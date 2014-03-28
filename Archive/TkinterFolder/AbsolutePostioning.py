"""
Layout management in Tkinter
To organise our widgets, we use specialised non visible objects called layoutmanagers

Two kinds of widgets
    -Containers
    -And their children

Tkinter has three built-in layout managers
    -pack
        -organises widgets in vertical and horizontal boxes
    -grid
        -places widgets in a two dimensional grid.
    -place managers
        -absolute positioning

"""

#Absolute Positioning
#This is not really good when it comes to resizing stuff.
#<problem>PIL library doesn't seem to work, tried installing the library, no success


from PIL import Image, ImageTk
from Tkinter import Tk, Label, BOTH
from ttk import Frame, Style

class Example(Frame):

    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Absolute Positioning")
        self.pack(fill=BOTH, expand = 1)
        Style().configure("TFrame", background ="#333")

        bard = Image.open("bardejov.jpg")
        bardejob = ImageTk.PhotoImage(bard)
        label1=Label(self, image=bardejov)
        label1.image = bardgejov
        label1.place(x=20,y=20)

        rot=Image.open("rotunda.jpg")
        rotunda = ImageTk.PhotoImage(rot)
        label2=Label(self, image=rotunda)
        label2.image = rotunda
        label2.place(x=40,y=160)

        minc = Image.open("mincol.jpg")
        mincol = ImageTk.PhotoImage(minc)
        label3 = Label(self, image=mincol)
        label3.image = mincol
        label3.place(x=170,y=50)

def main():
    root = Tk()
    root.geometry("300x280+300+300")
    app = Example(root)
    root.mainloop()

if __name__ =='__main__':
    main()
        
        