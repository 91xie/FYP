from Tkinter import Tk, BOTH
from ttk import Frame, Button, Style

class Example(Frame):

    #<standard set up>
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initUI()
    #</standard set up>

    def initUI(self):

        #<standard set up>
        self.parent.title("Quit Button")
        self.style = Style()
        self.style.theme_use("default")
        #</standard set up>

        #<assuming we use no or pack manager frame is normal>
        self.pack(fill=BOTH, expand=1)
        
        
        #<adding quit button>
        quitButton = Button(self, text="Quit",command = self.quit)#operation
        quitButton.place(x=50, y=50)#placing
        #</adding quit button>

        #<adding a start button, not going to do anything>
        
        #</adding a start button, not going to do anything>
def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()
