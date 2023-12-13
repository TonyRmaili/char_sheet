import tkinter as tk
from grider import WidgetMaker 

class TkGui2:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("v2")
        self.root.geometry("400x300")
        
        WidgetMaker(widget_type='entry',master=self.root,text='hej',row=0,column=0,width=5)
    
    def run(self):
        self.root.mainloop()

if __name__=='__main__':
    gui = TkGui2()
    gui.run()
