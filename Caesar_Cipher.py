from tkinter import *

w1 = Tk()


def tashfeer():
    key = -2
    k = ""
    word = mytxt.get().upper()
    for i in word:
        num = ord(i) + key
        if num < 90:
            k = k + (chr(num))
        elif num > 90:
            num = (num - 90) + 65 - 1
            k = k + (chr(num))
    lbl2.config(text=k)


w1.wm_attributes("-transparentcolor", 'grey')
w1.title('برنامج التشفير')
w1.geometry("500x500+450+40")
w1.resizable(False, False)
w1.config(bg="#123654")

lbl1 = Label(text="Caesar cipher", font=("Arial", 30), bg="#123654", fg="white")
lbl1.place(x=120, y=10)

mytxt = Entry(width=30, justify="center", font=("arial", 20))
mytxt.place(x=24, y=80)

btn_cipher = Button(text="Click here to code ", width=20, height=2, font=("arial", 13), command=tashfeer)
btn_cipher.place(x=155, y=150)

lbl2 = Label(text="000000", font=("Arial", 30))
lbl2.place(x=179, y=220)

w1.mainloop()
