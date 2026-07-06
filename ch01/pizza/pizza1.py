import tkinter as tk
from tkinter import messagebox

# 피자 가격
pizza_price = {
    "콤비네이션": 3500,
    "페퍼로니": 3800,
    "불고기": 4200,
    "치즈": 3000
}

drink_price = 2000


def order():
    pizza = pizza_var.get()

    try:
        count = int(slice_spin.get())
    except:
        messagebox.showerror("오류", "조각 수를 입력하세요.")
        return

    total = pizza_price[pizza] * count

    order_text = f"피자 : {pizza}\n"
    order_text += f"조각 : {count}개\n"

    if drink_var.get():
        total += drink_price
        order_text += "음료 : 추가\n"
    else:
        order_text += "음료 : 없음\n"

    order_text += "-" * 25 + "\n"
    order_text += f"총 금액 : {total:,}원"

    result.config(text=order_text)


def reset():
    pizza_var.set("콤비네이션")
    slice_spin.delete(0, tk.END)
    slice_spin.insert(0, "1")
    drink_var.set(False)
    result.config(text="")


window = tk.Tk()
window.title("조각 피자 주문 프로그램")
window.geometry("400x430")
window.resizable(False, False)

title = tk.Label(window,
                 text="🍕 조각 피자 주문",
                 font=("맑은 고딕", 18, "bold"))
title.pack(pady=10)

# 피자 종류
frame1 = tk.LabelFrame(window, text="피자 종류")
frame1.pack(fill="x", padx=15, pady=10)

pizza_var = tk.StringVar(value="콤비네이션")

for p in pizza_price.keys():
    tk.Radiobutton(frame1,
                   text=f"{p} ({pizza_price[p]}원)",
                   variable=pizza_var,
                   value=p).pack(anchor="w")

# 조각 수
frame2 = tk.LabelFrame(window, text="조각 수")
frame2.pack(fill="x", padx=15, pady=10)

slice_spin = tk.Spinbox(frame2,
                        from_=1,
                        to=10,
                        width=5)
slice_spin.pack(pady=5)

# 음료
frame3 = tk.LabelFrame(window, text="추가 메뉴")
frame3.pack(fill="x", padx=15, pady=10)

drink_var = tk.BooleanVar()

tk.Checkbutton(frame3,
               text=f"음료 추가 (+{drink_price}원)",
               variable=drink_var).pack(anchor="w")

# 버튼
frame4 = tk.Frame(window)
frame4.pack(pady=10)

tk.Button(frame4,
          text="주문하기",
          width=12,
          command=order).grid(row=0, column=0, padx=5)

tk.Button(frame4,
          text="초기화",
          width=12,
          command=reset).grid(row=0, column=1, padx=5)

# 결과
result = tk.Label(window,
                  text="",
                  justify="left",
                  font=("맑은 고딕", 11))
result.pack(pady=10)

window.mainloop()