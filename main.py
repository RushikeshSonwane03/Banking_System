from tkinter import *
from tkinter import messagebox
# from PIL import ImageTk, Image

win = Tk()
win.title("Banking System")
f0 = ("Arial", 30, 'bold')
f1 = ("Arial", 20, 'bold')
f2 = ("timesnewroman", 20, 'normal')
f3 = ("Arial", 15, 'bold')
bg = PhotoImage(file="images\Blue_White_Split.png")
bank_img = PhotoImage(file="images\Electronic-Banking.png")
# render = ImageTk.PhotoImage(bg)

def log_in():
    uname = t1.get()
    passw = t2.get()
    if uname != 'admin':
        messagebox.showerror("Login Failed!!!", "Please Enter Valid Username")
    elif passw != '@123':
        messagebox.showerror("Login Failed!!!", "Please Enter Valid Password")
    else:
        win.destroy()
        import options


def register():
    win.destroy()
    import register_new_user


login_bg = Label(win, image=bg)
login_bg.pack()

bank_logo = Label(win, image=bank_img)
bank_logo.place(x=50, y=50)

l0 = Label(win, text='Customer Log In', bd=5, fg='black', bg='white', font=f0)
l0.place(x=600, y=100)

l1 = Label(win, text='UserName', bd=5, fg='black', bg='yellow', font=f1)
l1.place(x=600, y=200)

t1 = Entry(win, font=f2)
t1.place(x=600, y=250)

l2 = Label(win, text='Password', bd=5, fg='black', bg='yellow', font=f1)
l2.place(x=600, y=350)

t2 = Entry(win,show='*', font=f2)
t2.place(x=600, y=400)

b1 = Button(win, text="Submit", font=f3, command=log_in)
b1.place(x=700, y=480)

b2 = Button(win, text='Register As New Customer', fg='black', bg='yellow', font=f1, command=register)
b2.place(x=50, y=450)

win.geometry("1000x600+100+50")

win.mainloop()
