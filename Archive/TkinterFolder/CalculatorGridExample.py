#Grid Example Calculator

from Tkinter import Tk, W, E
from ttk import Frame, Button, Label, Style
from ttk import Entry

class Example(Frame):

    def __init__(self,parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Calculator")
        Style().configure("TButton,",padding =(0,5,0,5))

        #<creating the grid system>
        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)

        self.rowconfigure(0,pad=3)
        self.rowconfigure(1,pad=3)
        self.rowconfigure(2,pad=3)
        self.rowconfigure(3,pad=3)
        self.rowconfigure(4,pad=4)
        #</creating the grid system>
        
        #<inserting a text box>
        entry= Entry(self)
        entry.grid(row=0,columnspan=4, sticky=W+E)
        #Aslo adjusting the position of the text box.
        #I'm assuming sticky=W+E means stick to West and East?
        #</inserting a text box>

        #<creating the buttons and putting them into a grid>
        cls = Button(self, text="Cls")
        cls.grid(row=1, column=0)
        bck = Button(self, text="Back")
        bck.grid(row=1, column=1)
        lbl = Button(self)
        lbl.grid(row=1, column=2)    
        clo = Button(self, text="Close")
        clo.grid(row=1, column=3)        
        sev = Button(self, text="7")
        sev.grid(row=2, column=0)        
        eig = Button(self, text="8")
        eig.grid(row=2, column=1)         
        nin = Button(self, text="9")
        nin.grid(row=2, column=2) 
        div = Button(self, text="/")
        div.grid(row=2, column=3) 
        
        fou = Button(self, text="4")
        fou.grid(row=3, column=0)        
        fiv = Button(self, text="5")
        fiv.grid(row=3, column=1)         
        six = Button(self, text="6")
        six.grid(row=3, column=2) 
        mul = Button(self, text="*")
        mul.grid(row=3, column=3)    
        
        one = Button(self, text="1")
        one.grid(row=4, column=0)        
        two = Button(self, text="2")
        two.grid(row=4, column=1)         
        thr = Button(self, text="3")
        thr.grid(row=4, column=2) 
        mns = Button(self, text="-")
        mns.grid(row=4, column=3)         
        
        zer = Button(self, text="0")
        zer.grid(row=5, column=0)        
        dot = Button(self, text=".")
        dot.grid(row=5, column=1)         
        equ = Button(self, text="=")
        equ.grid(row=5, column=2) 
        pls = Button(self, text="+")
        pls.grid(row=5, column=3)
        #</creating the buttons and putting them into a grid>

        #<self pack is needed, nothing displays if this is not included>
        self.pack()
        #pack() method shows the frame widget and gives its initial size
        #If no other parameters are given, the size will be just enough to show
        #all children, assuming that frame is a children.
        #</self pack is needed, nothing displays if this is not included>
        
def main():
    root = Tk()
    app = Example(root)
    root.mainloop()

if __name__ =='__main__':
    main()
