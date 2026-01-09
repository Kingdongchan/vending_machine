import tkinter as tk

import number as nmb
import product as prd

root = tk.Tk()
root.title("자판기")
root.geometry("800x600")

#프레임 형성(메인프레임, 사이드 프레임)
#메인프레임 -> 사이드프레임보다 커야하고 상품이 16가지가 들어가야함
main_frm = tk.Frame(root, width=550 ,bg="lightgray")
main_frm.pack(side="left", fill="y", expand = True)

#메인프레임에 상품이랑 배출고 배치하기
prd.main_frame_product(main_frm)

#사이드 프레임(프레임 안에 입력칸, 결제칸, 번호칸, 현금을 누를 수 있는 칸이 필요함)
#사이드 프레임 
side_frm = tk.Frame(root, width=250, bg="white")
side_frm.pack(side="left", fill="y", expand= True)

#입력칸
insert_frm = tk.Frame(side_frm, width=250, height=250, bg="white")
insert_frm.pack(side="top", fill="x", expand=True)
#결제칸
payment_frm = tk.Frame(side_frm, width=250, height= 0, bg="white")
payment_frm.pack(side="top", fill="x", expand=True)
#번호칸
number_frm = tk.Frame(side_frm, width=250, height =250, bg = "white")
number_frm.pack(side= "top", fill="x", expand=True)

# 번호칸 number.py 불러오기
nmb.number_bnt(number_frm)

#현금칸
insert_button_frm = tk.Frame(side_frm, width=250, height= 30, bg = "white")
insert_button_frm.pack(sid= "top", fill="x", expand=True)

 
root.mainloop()
