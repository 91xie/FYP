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
#Using the pack manager
#organise in vertical and horizontal boxes.

from Tkinter import Tk, RIGHT, BOTH, RAISED, LEFT
from ttk import Frame, Button, Style

class Example(Frame):

    def __init__(self,parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        #<standard set up>
        self.parent.title("Buttons")
        self.style = Style()
        self.style.theme_use("default")
        #</standard set up>

        #if you put buttons here, it will initiate the buttons.
        #then it will initiate the frame. You would get two columns.
        #buttons appear in the second "lowered" area and not the raised frame.

        
        
        #<adding an additional frame>
        frame = Frame(self, relief=RAISED, borderwidth=1)
        
        frame.pack(fill=BOTH, expand =1)
        #</adding an additional frame>

        #<standard self.pack>
        self.pack(fill=BOTH, expand =1)
        #</standard self.pack>

        #<buttons are placed here>
        closeButton = Button (self, text = "Close")
        closeButton.pack(side=RIGHT, padx=5, pady =5)
        okButton = Button(self, text = "OK")
        okButton.pack(side=RIGHT)
        #Note that the order at which this command is used changes
        #the layout.
        #</buttons are placed here>
        
        
        
def main():
    root = Tk()
    root.geometry("300x200+300+300")
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()
