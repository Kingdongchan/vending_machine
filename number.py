import tkinter as tk
import cls.button as bt


root= tk.Tk()

button = [
    "1", "2", "3",
    "4", "5", "6",
    "7", "8", "9",
    "Del", "0", "결정", "취소"
]


for index, i in enumerate(button):
    r = index//3+1
    c = index%3

    number_btn = bt.button(i, 10, 5, r, c)
    number_btn.number_btn_maker(root)
    
root.mainloop()