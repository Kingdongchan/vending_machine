import tkinter as tk
import cls.button as bt


root= tk.Tk()

button = [
    "1", "2", "3",
    "4", "5", "6",
    "7", "8", "9",
    "Del", "0", "결정"
]

ent = tk.Entry(root)
ent.grid(row=0, column=0, columnspan=4)

for index, i in enumerate(button):
    r = index//3+1
    c = index%3

    number_btn = bt.button(root, i, 3, 1, r, c)
    number_btn.number_btn_maker()


cancel_btn = bt.button(root, "취소", 3, 1, 4, 3)
cancel_btn.number_btn_maker()

root.mainloop()