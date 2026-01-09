import tkinter as tk

class frame:
    def __init__(self, main, width, height, row, column, expand, bg, text):
        self.main = main
        self.width = width
        self.height = height
        self.row = row
        self.column = column
        self.expand = expand
        self.bg = bg
        self.text = text

    def frm_maekr(self):
        frm = tk.Frame(self.main, width=self.width, height=self.height, bg=self.bg)
        frm.grid(row =self.row, column= self.column)

        label = tk.Label(frm, text=self.text)
        label.grid(row=0, column=0, sticky="s")
    
    def frm_bt_maker(self):        
        frm = tk.Frame(self.main, width=self.width, height=self.height, bg=self.bg)
        frm.grid(row =self.row, column= self.column, sticky="s")
 