import tkinter as tk
import cls.button as bt

# 동전 넣는 것을 버튼 누르는 것을 대처하겠음
# 동전을 넣으면 결제칸에 돈이 증가해야됨

def coin_bnt (insert_button_frm):

    coin = [
        100, 500, 1000, 5000 ,10000, "카드"
    ]

    #버튼 만들기(100, 500, 1000, 5000, 10000, 카드)
    for i in range(len(coin)):
        coin_bnt = coin[i]

        bnt = bt.button(insert_button_frm, coin_bnt, 4, 1, 0, i)
        bnt.number_btn_maker()

        # 버튼을 누르면 입력 더해지는 창에 돈이 더해져야함.
        