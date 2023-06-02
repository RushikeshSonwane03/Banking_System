from tkinter import *
from tkinter import messagebox

# from PIL import ImageTk, Image

win = Tk()
win.title("Banking System")
f0 = ("Arial", 30, 'bold')
f1 = ("Arial", 20, 'bold')
f2 = ("timesnewroman", 20, 'normal')
f3 = ("Arial", 15, 'bold')
bg = PhotoImage(file="images\\zabc.png")
bank_img = PhotoImage(file="images\\Electronic-Banking.png")


# render = ImageTk.PhotoImage(bg)

def deposite_call():
    win.destroy()
    import deposit


def withdraw_call():
    win.destroy()
    import withdraw


def close_acc_call():
    win.destroy()
    import close_account


def interest_call():
    win.destroy()
    import interest


def exit_fun():
    ans = messagebox.askyesnocancel("Confirm Exit", "Are you sure you want to exit ? ")
    if ans:
        win.destroy()
        import main


login_bg = Label(win, image=bg)
login_bg.pack()

l0 = Label(win, text='Banking System', bd=5, fg='black', bg='white', font=f0)
l0.place(x=350, y=30)

b1 = Button(win, text="Deposite", bg='cyan', font=f3, bd=5, width=10, command=deposite_call)
b1.place(x=50, y=100)

b2 = Button(win, text="Withdraw", bg='cyan', font=f3, bd=5, width=10, command=withdraw_call)
b2.place(x=100, y=200)

b3 = Button(win, text="Close_Acc", bg='cyan', font=f3, bd=5, width=10, command=close_acc_call)
b3.place(x=150, y=300)

b4 = Button(win, text="Interest", bg='cyan', font=f3, bd=5, width=10, command=interest_call)
b4.place(x=250, y=400)

b5 = Button(win, text="Exit", bg='cyan', font=f3, bd=5, width=10, command=exit_fun)
b5.place(x=300, y=500)

win.geometry("1000x600+100+50")

win.mainloop()
