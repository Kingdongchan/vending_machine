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
    {"id":1, "상품":"코카콜라"}, {"id":2, "상품":"갈아만든 배"},{"id":3, "상품":"사이다"}, {"id":4, "상품":"미에로화이바"},
    {"id":5, "상품":"초코송이"}, {"id":6, "상품":"에너지바"} , {"id":7, "상품":"다이제 씬"}, {"id":8, "상품":"빠다코코낫"},
    {"id":9, "상품":"신라면"}, {"id":10, "상품":"참꺠라면"}, {"id":11, "상품":"불닭볶음면"}, {"id":12, "상품":"육개장사발면"},
    {"id":13, "상품":"오레오"}, {"id":14, "상품":"화이트하임"}, {"id":15, "상품":"통크"}, {"id":16, "상품":"초코쿠키"}
]

# 메뉴판 16개 생성
for i in range(len(menu)):
    prd = menu[i]["상품"]

    r = i//4 
    c = i%4

    #모든 프레임에 가중치 주기(pack ->)
    for j in range(4):
        top_frm.grid_columnconfigure(j, weight=1)
        top_frm.grid_rowconfigure(j, weight=1)

    menu_frm = frm.frame(top_frm, 30, 30, r, c, True, "gray", prd)
    menu_frm.frm_maekr()

    

root.mainloop()