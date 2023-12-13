import tkinter as tk

# widget types
# Entry,Button,Label,Menu
# is this needed?

class WidgetMaker:
    def __init__(self,widget_type,master,row,column,text=None,width=None):

        if widget_type =='label':
            self.create_label(master,text,row,column)   
        elif widget_type =='entry':
            self.create_entry(master,width,row,column)
        elif widget_type =='button':
            pass

    def create_label(self,master,text,row,column):
        label = tk.Label(master=master,text=text)
        label.grid(row=row, column=column)
    
    def create_entry(self,master,width,row,column):
        entry = tk.Label(master=master,width=width)
        entry.grid(row=row, column=column)