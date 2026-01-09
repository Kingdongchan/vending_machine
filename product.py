import tkinter as tk
import cls.frame as frm


root =tk.Tk()
root.geometry("550x600")

menu = [
    "코카콜라", "갈아만든 배", "사이다", "미에로화이바",
    "초코송이", "에너지바", "다이제 씬", "빠다코코낫",
    "신라면", "참꺠라면", "불닭볶음면", "육개장사발면",
    "오레오", "화이트하임", "통크", "초코쿠키"
]

#메뉴판 16개 생성
for i in range(1,17):
    r = i//4 
    c = i%4

    


root.mainloop()