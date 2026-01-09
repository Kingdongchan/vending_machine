import tkinter as tk
 
# 현금, 카드을 넣었는지 확인할 수 있는 입력창 하나
# 평소에는 "돈을 넣어주십시오." 출력
    #현금이라면
        #금액을 확인하여 입력창에 더하기
    #카드라면
        #True 출력

def payment (payment_frm):
    global buy_insert

    #공간 생성
    buy_insert = tk.Entry(payment_frm, width=20, state="normal")
    buy_insert.pack(side="left")
    #"돈을 넣어주십시오." 넣기
    answer = "돈을 넣어주십시오."
    buy_insert.insert(0, answer)
    # 못만지게 disabled
    buy_insert.config(state="disabled")

