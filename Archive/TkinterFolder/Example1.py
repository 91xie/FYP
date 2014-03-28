#from zetcode.com/gui/tkinter

from Tkinter import Tk, Frame, BOTH
#Tk class is used to create a root window.
#Frame is a container for widgets.

class Example(Frame):
    def __init__(self,parent):
        #we will call the constructor of our inherited class using init
        Frame.__init__(self, parent, background = "white")
        #save a reference to the parent widget. the aprent widget is the TK root window in our case
        self.parent = parent
        #Delegate the creation of the UI
        self.initUI()#this function is run below
    def initUI(self):
        #setting the initialisation
        self.parent.title("Simple")
        #pack() method is one of three geometry managers in Tkinter.
        #it organizes widgets into horizontal and vertical boxes.
        #here we put the frame widget, accessed via the self attribute
        # to the Tk root window. It is expanded in BOTH directions.
        self.pack(fill = BOTH, expand = 1)

def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()
