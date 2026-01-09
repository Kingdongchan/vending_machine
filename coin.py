import tkinter as tk
import cls.button as bt

import payment as pm
# 동전 넣는 것을 버튼 누르는 것을 대처하겠음
# 동전을 넣으면 결제칸에 돈이 증가해야됨

# 동전을 넣을때마다 증가하는 변수 지정
count = 0

def coin_bnt (insert_button_frm):

    coin = ["100", "500", "1000", "5000" , "10000", "카드"]

    #버튼 만들기(100, 500, 1000, 5000, 10000, 카드)
    for i in range(len(coin)):
        coin_bnt = coin[i]

        bnt = bt.button(insert_button_frm, coin_bnt, 4, 1, 0, i, lambda idx=coin_bnt: in_entry(idx))
        bnt.number_btn_maker()

        # 버튼을 누르면 입력 더해지는 창에 돈이 더해져야함.
        
#버튼 누르면 entry에 들어가는 함수
    def in_entry (num):
        #전역변수로 지정
        pm.buy_insert

        count = 0

        if num == "카드":
            pm.buy_insert.config(state="normal")
            
            answer = "상품을 골라주세요."
            
            pm.buy_insert.delete(0, tk.END)
            
            pm.buy_insert.insert(tk.END, answer)

            pm.buy_insert.config(state="disabled")        
        
        else:
            pm.buy_insert.config(state="normal")
            
            pm.buy_insert.delete(0, tk.END)

            pm.buy_insert.insert(0, coin_bnt)

            pm.buy_insert.config(state="disabled")          