import tkinter as tk
import cls.button as bt

def number_bnt(number_frm):

    button = [
        "1", "2", "3",
        "4", "5", "6",
        "7", "8", "9",
        "Del", "0", "결정"
]
    #버튼을 누르면 숫자가 나오는 입력창
    ent = tk.Entry(number_frm, state="disabled")
    ent.grid(row=0, column=0, columnspan=4)

    #버튼 만들기 로직
    for index, i in enumerate(button):
        r = index//3+1
        c = index%3
        
        number_btn = bt.button(number_frm, i, 3, 1, r, c, lambda idx=i:in_entry(idx))
        number_btn.number_btn_maker()

    #취소 버튼 
    cancel_btn = bt.button(number_frm, "취소", 3, 1, 4, 3)
    cancel_btn.number_btn_maker()



#버튼 누르면 entry에 들어가는 함수
    def in_entry (num):
        ent.config(state="normal")

        #만약 텍스트가 숫자면 숫자
        #del이면 텍스트 창을 초기화
        #결정이면 음료 배출(나중에 만들 예정)
        if num == "Del":
            ent.delete(0, tk.END)
        else:
            ent.insert(tk.END, num)

        ent.config(state="disabled")