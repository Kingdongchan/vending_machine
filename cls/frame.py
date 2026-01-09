import tkinter as tk

insert_frm = tk.Frame(side_frm, width=250, height=250, bg="white")
insert_frm.pack(side="top", fill="x", expand=True)

class frame:
    def __inti__ (self, main, width, height, bg, side, fill, expand):
        self.main = main
        self.width = width
        self.height = height
        self.bg = bg
        self.side = side
        self.fill = fill
        self.expand =expand

    def frm_maker(self):
        frm = tk.Frame(self.main, width=self.width, height=self.height, bg=self.bg)
        frm.pack(side=self.side, fill=self.fill, expand=self.expand)