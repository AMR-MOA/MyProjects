from tkinter import *
player1_box = []
player2_box = []

window = Tk()
window.title("XO GAME")
window.geometry("600x590+335+25")
window.resizable(False, False)
window.config(bg="#123654")

lbl1 = Label(text="XO GAME", bg="#123654", fg="white", font=("Arial", 25))
lbl1.place(x=215, y=0)
lbl2 = Label(text="PLAYER'S ROLE:", bg="#123654", fg="white", font=("Arial", 25))
lbl2.place(x=165, y=70)
lbl3 = Label(text="PLAYER 1", bg="#123654", fg="white", font=("Arial", 25))
lbl3.place(x=215, y=120)
lbl4 = Label(text="""THE PROGRAM WAS PROGRAMMED
BY: AMMAR ALOTAIBI""", bg="#123654", fg="white", font=("Arial", 17))
lbl4.place(x=100, y=530)


def winner():
    if 1 in player1_box and 2 in player1_box and 3 in player1_box or\
    4 in player1_box and 5 in player1_box and 6 in player1_box or\
    7 in player1_box and 8 in player1_box and 9 in player1_box or\
    1 in player1_box and 4 in player1_box and 7 in player1_box or\
    2 in player1_box and 5 in player1_box and 8 in player1_box or\
    3 in player1_box and 6 in player1_box and 9 in player1_box or\
    1 in player1_box and 5 in player1_box and 9 in player1_box or\
    3 in player1_box and 5 in player1_box and 7 in player1_box:
        lbl3.config(text="PLAYER 1 WON")
    elif 1 in player2_box and 2 in player2_box and 3 in player2_box or\
    4 in player2_box and 5 in player2_box and 6 in player2_box or\
    7 in player2_box and 8 in player2_box and 9 in player2_box or\
    1 in player2_box and 4 in player2_box and 7 in player2_box or\
    2 in player2_box and 5 in player2_box and 8 in player2_box or\
    3 in player2_box and 6 in player2_box and 9 in player2_box or\
    1 in player2_box and 5 in player2_box and 9 in player2_box or\
    3 in player2_box and 5 in player2_box and 7 in player2_box:
        lbl3.config(text="PLAYER 2 WON")
    else:
        draw()


def draw():
    if len(player1_box) == 5 and len(player2_box) == 4:
        lbl3.config(text="DRAW")


def k1():
    a = lbl3.cget("text")
    if a == "PLAYER 1":
        player1_box.append(1)
        btn1.config(text="X", bg="orange", font=("Arial", 12), state=DISABLED)
        lbl3.config(text="PLAYER 2")
        winner()
    if a == "PLAYER 2":
        player2_box.append(1)
        btn1.config(text="O", bg="light green", font=("Arial", 12), state=DISABLED)
        lbl3.config(text="PLAYER 1")
        winner()


def k2():
    a = lbl3.cget("text")
    if a == "PLAYER 1":
        player1_box.append(2)
        btn2.config(text="X", bg="orange", font=("Arial", 12), state=DISABLED)
        lbl3.config(text="PLAYER 2")
        winner()
    if a == "PLAYER 2":
        player2_box.append(2)
        btn2.config(text="O", bg="light green", font=("Arial", 12), state=DISABLED)
        lbl3.config(text="PLAYER 1")
        winner()


def k3():
    a = lbl3.cget("text")
    if a == "PLAYER 1":
        player1_box.append(3)
        btn3.config(text="X", bg="orange",  font=("Arial", 12), state=DISABLED)
        lbl3.config(text="PLAYER 2")
        winner()
    if a == "PLAYER 2":
        player2_box.append(3)
        btn3.config(text="O", bg="light green", font=("Arial", 12), state=DISABLED)
        lbl3.config(text="PLAYER 1")
        winner()


def k4():
    a = lbl3.cget("text")
    if a == "PLAYER 1":
        player1_box.append(4)
        btn4.config(text="X", bg="orange", font=("Arial", 12), state=DISABLED)
        lbl3.config(text="PLAYER 2")
        winner()
    if a == "PLAYER 2":
        player2_box.append(4)
        btn4.config(text="O", bg="light green", font=("Arial", 12), state=DISABLED)
        lbl3.config(text="PLAYER 1")
        winner()


def k5():
    a = lbl3.cget("text")
    if a == "PLAYER 1":
        player1_box.append(5)
        btn5.config(text="X", bg="orange", font=("Arial", 12), state=DISABLED)
        lbl3.config(text="PLAYER 2")
        winner()
    if a == "PLAYER 2":
        player2_box.append(5)
        btn5.config(text="O", bg="light green", font=("Arial", 12), state=DISABLED)
        lbl3.config(text="PLAYER 1")
        winner()


def k6():
    a = lbl3.cget("text")
    if a == "PLAYER 1":
        player1_box.append(6)
        btn6.config(text="X", bg="orange", font=("Arial", 12), state=DISABLED)
        lbl3.config(text="PLAYER 2")
        winner()
    if a == "PLAYER 2":
        player2_box.append(6)
        btn6.config(text="O", bg="light green", font=("Arial", 12), state=DISABLED)
        lbl3.config(text="PLAYER 1")
        winner()


def k7():
    a = lbl3.cget("text")
    if a == "PLAYER 1":
        player1_box.append(7)
        btn7.config(text="X", bg="orange", font=("Arial", 12), state=DISABLED)
        lbl3.config(text="PLAYER 2")
        winner()
    if a == "PLAYER 2":
        player2_box.append(7)
        btn7.config(text="O", bg="light green", font=("Arial", 12), state=DISABLED)
        lbl3.config(text="PLAYER 1")
        winner()


def k8():
    a = lbl3.cget("text")
    if a == "PLAYER 1":
        player1_box.append(8)
        btn8.config(text="X", bg="orange", font=("Arial", 12), state=DISABLED)
        lbl3.config(text="PLAYER 2")
        winner()
    if a == "PLAYER 2":
        player2_box.append(8)
        btn8.config(text="O", bg="light green", font=("Arial", 12), state=DISABLED)
        lbl3.config(text="PLAYER 1")
        winner()


def k9():
    a = lbl3.cget("text")
    if a == "PLAYER 1":
        player1_box.append(9)
        btn9.config(text="X", bg="orange", font=("Arial", 12), state=DISABLED)
        lbl3.config(text="PLAYER 2")
        winner()
    if a == "PLAYER 2":
        player2_box.append(9)
        btn9.config(text="O", bg="light green", font=("Arial", 12), state=DISABLED)
        lbl3.config(text="PLAYER 1")
        winner()


def restart():
    btn1.config(text="1", font=("Arial", 12), bg="#123654", fg="#90ee90", width=8, height=4, state=NORMAL, command=k1)
    btn2.config(text="2", font=("Arial", 12), bg="#123654", fg="#90ee90", width=8, height=4, state=NORMAL, command=k2)
    btn3.config(text="3", font=("Arial", 12), bg="#123654", fg="#90ee90", width=8, height=4, state=NORMAL, command=k3)
    btn4.config(text="4", font=("Arial", 12), bg="#123654", fg="#90ee90", width=8, height=4, state=NORMAL, command=k4)
    btn5.config(text="5", font=("Arial", 12), bg="#123654", fg="#90ee90", width=8, height=4, state=NORMAL, command=k5)
    btn6.config(text="6", font=("Arial", 12), bg="#123654", fg="#90ee90", width=8, height=4, state=NORMAL, command=k6)
    btn7.config(text="7", font=("Arial", 12), bg="#123654", fg="#90ee90", width=8, height=4, state=NORMAL, command=k7)
    btn8.config(text="8", font=("Arial", 12), bg="#123654", fg="#90ee90", width=8, height=4, state=NORMAL, command=k8)
    btn9.config(text="9", font=("Arial", 12), bg="#123654", fg="#90ee90", width=8, height=4, state=NORMAL, command=k9)
    lbl3.config(text="PLAYER 1")


btn1 = Button(window, text="1", font=("Arial", 12), bg="#123654", fg="#90ee90", width=8, height=4, command=k1)
btn1.place(x=150, y=190)

btn2 = Button(window, text="2", font=("Arial", 12), bg="#123654", fg="#90ee90", width=8, height=4, command=k2)
btn2.place(x=260, y=190)

btn3 = Button(window, text="3", font=("Arial", 12), bg="#123654", fg="#90ee90", width=8, height=4, command=k3)
btn3.place(x=370, y=190)

btn4 = Button(window, text="4", font=("Arial", 12), bg="#123654", fg="#90ee90", width=8, height=4, command=k4)
btn4.place(x=150, y=300)

btn5 = Button(window, text="5", font=("Arial", 12), bg="#123654", fg="#90ee90", width=8, height=4, command=k5)
btn5.place(x=260, y=300)

btn6 = Button(window, text="6", font=("Arial", 12), bg="#123654", fg="#90ee90", width=8, height=4, command=k6)
btn6.place(x=370, y=300)

btn7 = Button(window, text="7", font=("Arial", 12), bg="#123654", fg="#90ee90", width=8, height=4, command=k7)
btn7.place(x=150, y=410)

btn8 = Button(window, text="8", font=("Arial", 12), bg="#123654", fg="#90ee90", width=8, height=4, command=k8)
btn8.place(x=260, y=410)

btn9 = Button(window, text="9", font=("Arial", 12), bg="#123654", fg="#90ee90", width=8, height=4, command=k9)
btn9.place(x=370, y=410)

btn_restart = Button(text="RESTART", font=("Arial", 12), bg="#123654", fg="#90ee90", width=8, height=4, command=restart)
btn_restart.place(x=510, y=10)

window.mainloop()
