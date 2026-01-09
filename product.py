import tkinter as tk
import cls.frame as frm


root =tk.Tk()
root.geometry("550x600")

#프레임이 2개로 나눠져야함
#상단 - 상품을 진열하는 곳
#하단 - 배출구 -> 오른쪽 하단에 있어야함

#상품을 진열할 곳
top_frm = tk.Frame(root, width= 550, height= 500, bg="lightgray")
top_frm.pack(side="top", fill="both", expand=True)

#배출구를 만들 곳
bt_frm = tk.Frame(root, width= 550, height=100, bg="red")
bt_frm.pack(side="top", fill="both", expand=True)

#상단 상품을 진열하는 곳 만들기

menu = [
    "코카콜라", "갈아만든 배", "사이다", "미에로화이바",
    "초코송이", "에너지바", "다이제 씬", "빠다코코낫",
    "신라면", "참꺠라면", "불닭볶음면", "육개장사발면",
    "오레오", "화이트하임", "통크", "초코쿠키"
]

# 메뉴판 16개 생성
for i in range(len(menu)):
    prd = menu[i]

    r = i//4 
    c = i%4
    
    menu_frm = frm.frame(top_frm, 30, 30, r, c, True, "gray")
    menu_frm.frm_maekr()

    

root.mainloop()