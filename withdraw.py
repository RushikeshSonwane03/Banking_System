from datetime import date
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

import mysql.connector
from tkcalendar import DateEntry

my_bal = int()

def upd_bal():
    s3 = ap_no.get()
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="k2it_python_project"
    )
    mycur = mydb.cursor()
    mycur.execute("select apbal from Applicant where apno =" + s3)
    mydata = mycur.fetchone()
    global my_bal
    my_bal = mydata[0]
    balance = "Balance : $" + str(mydata[0])
    l7.config(text=balance)


def format_date(date_str):
    str1 = date_str[0:4]
    str2 = date_str[4:7]
    str3 = date_str[7:]
    return str1 + str3 + str2


def apno_combobox():
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="k2it_python_project"
    )
    mycur = mydb.cursor()
    mycur.execute("select apno from Applicant where status = 'Active'")
    mydata = mycur.fetchall()
    apno = []
    for i in range(len(mydata)):
        apno.append(mydata[i][0])
    return apno


def clrfield():
    sl_date.delete(0, END)
    ap_no.delete(0, END)
    particular.delete(0, END)
    t5.delete(0, END)
    l7.config(text="Balance :")

def maxrec():
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="k2it_python_project"
    )
    mycur = mydb.cursor()
    mycur.execute("select max(sl_no) from Withdraw")
    mydata = mycur.fetchone()
    if mydata[0] is None:
        t1.delete(0, END)
        t1.insert(0, "1")
    else:
        cnt = int(mydata[0])
        cnt += 1
        t1.delete(0, END)
        t1.insert(0, "" + str(cnt))
        clrfield()


def withd():
    global money
    upd_bal()
    s1 = t1.get()
    s2 = format_date(str(sl_date.get_date()))
    s3 = ap_no.get()
    s4 = particular.get()
    s5 = t5.get()
    if s4 == "":
        messagebox.showinfo("Warn...", "Plz Select Particular")
        return
    if s5 == "":
        messagebox.showinfo("Warn...", "Plz Enter Amount")
        return

    if my_bal < int(s5):
        messagebox.showwarning("Warning...", 'Insufficient Balance')
    else:
        money = str(my_bal - int(s5))
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="k2it_python_project"
    )
    mycur = mydb.cursor()
    mycur.execute("Insert into Withdraw values(" + s1 + ",'" + s2 + "'," + s3 + ",'" + s4 + "'," + s5 + ")")
    mydb.commit()
    mycur.execute("Update Applicant set apbal =" + money + " where apno ="+s3)
    mydb.commit()
    messagebox.showinfo("Confirm...", "Amount Withdrawl")
    maxrec()



def exit_fun():
    ans = messagebox.askyesnocancel("Confirm Exit", "Are you sure you want to exit ? ")
    if ans:
        win.destroy()
        import options


win = Tk()
win.title("Withdraw Page")
win.geometry("1000x600+100+50")
f0 = ("Arial", 30, 'bold', 'italic')
f1 = ("Arial", 15, 'bold')
f2 = ("timesnewroman", 12, 'normal')

bgimg = PhotoImage(file="images\zabc.png")

limg = Label(win, image=bgimg)
limg.pack()

frame = Frame(win, bg="cyan", width=515, height=450)
frame.place(x=50, y=80)

l1 = Label(win, text="Withdraw Page", font=f0)
l1.place(x=150, y=50)

l2 = Label(win, text="Sl No", font=f1)
l2.place(x=100, y=150)

t1 = Entry(win, font=f2)
t1.place(x=280, y=150)

l3 = Label(win, text="Sl Date", font=f1)
l3.place(x=100, y=200)

sl_date = DateEntry(win, selectmode='day', date_pattern='MM-dd-yyyy')
sl_date.set_date(date.today())
sl_date.place(x=280, y=200)

l4 = Label(win, text="Ap No", font=f1)
l4.place(x=100, y=250)

apno_list = apno_combobox()
ap_no = Combobox(win, values=apno_list)
ap_no.place(x=280, y=250)

l5 = Label(win, text="Particular", font=f1)
l5.place(x=100, y=300)

particular_list = ['Cash', 'Cheque', 'Card']
particular = Combobox(win, values=particular_list)
particular.place(x=280, y=300)

l6 = Label(win, text="Amount", font=f1)
l6.place(x=100, y=350)

t5 = Entry(win, font=f2)
t5.place(x=280, y=350)

l7 = Label(win, text="Balance :", font=("Arial", 18, 'bold'), bg="cyan")
l7.place(x=100, y=400)

b1 = Button(win, text="ADD", bd=5, font=f1, command=maxrec)
b1.place(x=100, y=450)

b2 = Button(win, text="BAL", bd=5, font=f1, command=upd_bal)
b2.place(x=175, y=450)

b3 = Button(win, text="WITHDRAW", bd=5, font=f1, command=withd)
b3.place(x=250, y=450)

b5 = Button(win, text="EXIT", bd=5, font=f1, command=exit_fun)
b5.place(x=400, y=450)

win.mainloop()
