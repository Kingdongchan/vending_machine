import tkinter as tk
import cls.frame as frm

# 16개의 상품의 번호와 상품이름 가격들이 적혀 있어야함
# 패널에는 번호와 상품명만 출력
# 상품보다 현금이 많이 들어오면 불을 들어오게 끔
# 배출구에 구매한 상품이 배출

#재고

def main_frame_product (main_frm):

    #프레임이 2개로 나눠져야함
    #상단 - 상품을 진열하는 곳
    #하단 - 배출구 -> 오른쪽 하단에 있어야함
    #상품을 진열할 곳
    
    top_frm = tk.Frame(main_frm, width= 600, height=500, bg="lightgray")
    top_frm.grid(row=0, column=0, stick="nsew" )


    main_frm.grid_rowconfigure(0, weight=9)
    main_frm.grid_rowconfigure(1, weight=1)
    main_frm.grid_columnconfigure(0, weight=1)


    #상단 상품을 진열하는 곳 만들기
    menu = [
        {"id":1, "상품":"코카콜라", "price": 1400}, 
        {"id":2, "상품":"갈아만든 배", "price": 1300},
        {"id":3, "상품":"사이다", "price": 1200}, 
        {"id":4, "상품":"미에로화이바", "price":900},
        {"id":5, "상품":"초코송이", "price": 1300}, 
        {"id":6, "상품":"에너지바", "price": 1300},
        {"id":7, "상품":"다이제 씬", "price": 1500}, 
        {"id":8, "상품":"빠다코코낫", "price":1600},
        {"id":9, "상품":"신라면", "price": 1300}, 
        {"id":10, "상품":"참깨라면", "price": 1300}, 
        {"id":11, "상품":"불닭볶음면", "price": 1500}, 
        {"id":12, "상품":"육개장사발면", "price": 1300},
        {"id":13, "상품":"오레오", "price": 1600}, 
        {"id":14, "상품":"화이트하임", "price": 1500}, 
        {"id":15, "상품":"통크", "price": 1300}, 
        {"id":16, "상품":"초코쿠키", "price": 1300}
    ]

    # 메뉴판 16개 생성
    for i in range(len(menu)):
        prd = menu[i]["상품"]
        prd_number = menu[i]["id"]

        r = i//4 
        c = i%4

        #모든 프레임에 가중치 주기(pack ->)
        for j in range(4):
            top_frm.grid_columnconfigure(j, weight=1)
            top_frm.grid_rowconfigure(j, weight=1)

        # 프레임마다 상품 이름 넣기
        menu_frm = frm.frame(top_frm, 30, 30, r, c, True, "gray", f"{prd_number}. {prd}")
        menu_frm.frm_maekr()

    #배출구를 만들 곳
    bt_frm = tk.Frame(main_frm, bg="black")
    bt_frm.grid(row=1, column=0, sticky="nsew")

    bt_frm.grid_columnconfigure(0, weight=1)
    bt_frm.grid_rowconfigure(0, weight=1)
    # bt_frm.grid_rowconfigure(0, weight=1)
    #배출구
    out_prd = frm.frame(bt_frm, 100, 100 , 0, 0, False, "white", None)
    out_prd.frm_bt_maker()
