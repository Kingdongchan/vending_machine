import tkinter as tk

class button:
    def __init__ (self, main, text, width, height, row, column, command=None):
        self.main = main
        self.text = text
        self.width = width
        self.height = height
        self.row = row
        self.column =  column
        self.command = command

    def number_btn_maker(self):
        btn = tk.Button(self.main, text=self.text, width=self.width, height=self.height, command=self.command)
        btn.grid(row=self.row, column=self.column)

        