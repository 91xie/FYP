#File Dialog

from Tkinter import Frame, Tk, BOTH, Text, Menu, END
import tkFileDialog

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("File Dialog")
        self.pack(fill=BOTH, expand =1)

        #<menubar is created here>
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        menubar.add_cascade(label="File",menu=fileMenu)
        #observe command "self.onOpen"
        #</menubar is created here>
        
        #<assuming this means the item's range for text>
        self.txt= Text(self)
        self.txt.pack(fill=BOTH, expand =1)
        #
        #</assuming this means the item's range for text>

    #<open file dialog function>
    def onOpen(self):
        ftypes = [('Python files','*.py'),('All files','*')]
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
        fl = dlg.show() #fl is filename

        if fl !='':
            text = self.readFile(fl)#text is read
            self.txt.insert(END, text)#text is set here
    #tkFileDialog.Open(self, filetypes = ftypes) is what you need
    #it creates the dialog object "dlg"
    #then you instruct this thing to "show()" which returns a
    #string
    #</open file dialog function>
            
    def readFile(self, filename):
            f = open(filename, "r")
            text = f.read()
            return text

def main():
    root = Tk()
    ex = Example(root)
    root.geometry("300x250+300+300")
    root.mainloop()

if __name__ == '__main__':
    main()
