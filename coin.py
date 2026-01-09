import tkinter as tk
import cls.button as bt


root = tk.Tk()

coin = [
    100, 500, 1000, 5000 ,10000, "카드"
]

#버튼 만들기(100, 500, 1000, 5000, 10000, 카드)
for i in range(len(coin)):
    coin_bnt = coin[i]

    bnt = bt.button(root, coin_bnt, 5, 1, 0, i)
    bnt.number_btn_maker()


root.mainloop()
























#     card_bnt = bt.button(insert_button_frm, "카드", 5, 1, 0, 5)
# def insert_coin(insert_button_frm):
#     #100원 코인
#     one_bnt = bt.button(insert_button_frm, "100", 5, 1, 0, 0)
#     one_bnt.number_btn_maker()

#     #500 코인
#     two_bnt = bt.button(insert_button_frm, "500", 5, 1, 0, 1)
#     two_bnt.number_btn_maker()

#     #1000원 지폐
#     three_bnt = bt.button(insert_button_frm, "1000", 5, 1, 0, 2)
#     three_bnt.number_btn_maker()

#     #5000원 지페
#     four_bnt = bt.button(insert_button_frm, "5000", 5, 1, 0, 3)
#     four_bnt.number_btn_maker()

#     #10000원 지페
#     five_bnt = bt.button(insert_button_frm, "10000", 5, 1, 0, 4)
#     five_bnt.number_btn_maker()

#     #카드