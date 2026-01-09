import tkinter as tk

class frame:
    def __init__(self, main, width, height, row, column, expand):
        self.main = main
        self.width = width
        self.height = height
        self.row = row
        self.column = column
        self.expand = expand

    def frm_maekr(self):
        frm = tk.Frame(self.main, width=self.main, height=self.height)
        frm.grid(row =self.row, column= self.column, expand=self.expand)
    