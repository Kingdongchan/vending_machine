import tkinter as tk

root = tk.Tk()
root.title("자판기")
root.geometry("800x600")

#프레임 형성(메인프레임, 사이드 프레임)
#메인프레임 -> 사이드프레임보다 커야하고 상품이 16가지가 들어가야함
main_frm = tk.Frame(root, width=550 ,bg="lightgray")
main_frm.pack(side="left", fill="y", expand = True)

#사이드 프레임(프레임 안에 입력칸, 결제칸, 번호칸, 현금을 누를 수 있는 칸이 필요함)
#사이드 프레임 
side_frm = tk.Frame(root, width=250, bg="gray")
side_frm.pack(side="left", fill="y", expand= True)
root.mainloop()