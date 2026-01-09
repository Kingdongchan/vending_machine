import tkinter as tk

class button:
    def __inti__ (self, text, width, height, row, column):
        self.text = self
        self.width = width
        self.height = height
        self.row = row
        self.column =  column

    def number_btn_maker(self, number_frm):
        btn = tk.Button(number_frm, text=self.text, width=self.width, height=self.height)
        btn.grid(row=self.row, column=self.column)