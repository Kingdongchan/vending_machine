import tkinter as tk
import cls.button as bt

# 버튼 1,2,3,4,5,6,7,8,9, del, 결정, 취소 버튼이 있음
# 입력창은 건들 수 없고 버튼을 누르면 입력창에 번호가 나와야됨
# 결정을 누르면 입력창에 있는 번호와 맞는 상품이 나와야됨
    # 만약에 가격이 적으면 "상품을 구매할 수 없습니다"  입력창에 출력
    # 만약에 가격이 알맞다면 "감사합니다." 입력창에 출력, 잔돈 배출
# del를 누르면 -> 입력창 초기화
#취소를 누르면 잔돈 반환
    #현금이라면
        #잔돈이 부족하다면 -> "잔돈이 부족합니다 전화번호에 연락 부탁드립니다.", 입력창 초기화
        #잔돈이 적절하다면 -> "잔돈이 반환되었습니다." 출력, 입력창 초기화
    # 카드라면
        # True, False

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
        elif num == "결정":
            ent.delete(0, tk.END)
            #감사합니다. 배출구를 확인하세요.
            
            answer = "감사합니다."
            ent.insert(0, answer)
        
        elif num == "취소":
            ent.delete(0, tk.END)

        else:
            ent.insert(tk.END, num)

        ent.config(state="disabled")