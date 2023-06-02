from datetime import date
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

import mysql.connector
from tkcalendar import DateEntry

my_bal = int()

def upd_bal():
    t5.delete(0, END)
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
    reamount = str(mydata[0] - (mydata[0]*0.05))
    t5.insert(0, "$"+reamount)


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
    mycur.execute("select apno from Applicant where status = 'active'")
    mydata = mycur.fetchall()
    apno = []
    for i in range(len(mydata)):
        apno.append(mydata[i][0])
    return apno


def clrfield():
    Cl_Date.delete(0, END)
    ap_no.delete(0, END)
    t4.delete(0, END)
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
    mycur.execute("select max(cl_no) from close_acc")
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


def close():
    s1 = t1.get()
    s2 = format_date(str(Cl_Date.get_date()))
    s3 = ap_no.get()
    s4 = t4.get()
    s5 = t5.get()
    if s3 == "":
        messagebox.showinfo("Warn...", "Plz Enter Applicant No")
        return
    if s4 == "":
        messagebox.showinfo("Warn...", "Plz Select the Reason !")
        return
    ans = messagebox.askyesnocancel("Confirm Exit", "Are you sure you want to Close Account ? ")
    if ans:
        mydb = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            database="k2it_python_project"
        )
        mycur = mydb.cursor()
        mycur.execute("Insert into Close_Acc values(" + s1 + ",'" + s2 + "'," + s3 + ",'" + s4 + "'," + s5[1:] + ")")
        mydb.commit()
        mycur.execute("Update Applicant SET status = 'closed' where apno = " + s3)
        mydb.commit()
        messagebox.showinfo("Confirm...", "Account Deleted Successfully")
        maxrec()


def exit_fun():
    ans = messagebox.askyesnocancel("Confirm Exit", "Are you sure you want to exit ? ")
    if ans:
        win.destroy()
        import options


win = Tk()
win.title("Close Account Page")
win.geometry("1000x600+100+50")
f0 = ("Arial", 30, 'bold', 'italic')
f1 = ("Arial", 15, 'bold')
f2 = ("timesnewroman", 12, 'normal')

bgimg = PhotoImage(file="images\zabc.png")

limg = Label(win, image=bgimg)
limg.pack()

frame = Frame(win, bg="#0F5D92", width=515, height=450)
frame.place(x=50, y=80)

l1 = Label(win, text="Close Account Page", font=f0)
l1.place(x=120, y=50)

l2 = Label(win, text="Cl No", font=f1)
l2.place(x=100, y=150)

t1 = Entry(win, font=f2)
t1.place(x=280, y=150)

l3 = Label(win, text="Cl Date", font=f1)
l3.place(x=100, y=200)

Cl_Date = DateEntry(win, selectmode='day', date_pattern='MM-dd-yyyy')
Cl_Date.set_date(date.today())
Cl_Date.place(x=280, y=200)

l4 = Label(win, text="Ap No", font=f1)
l4.place(x=100, y=250)

apno_list = apno_combobox()
ap_no = Combobox(win, values=apno_list)
ap_no.place(x=280, y=250)

l5 = Label(win, text="Reason", font=f1)
l5.place(x=100, y=300)

reasons = ['Had a better Choice', 'Bad Service', 'Account got Hacked', 'Other']
t4 = Combobox(win, values=reasons)
t4.place(x=280, y=300)

l6 = Label(win, text="ReAmount", font=f1)
l6.place(x=100, y=350)

t5 = Entry(win, font=f2)
t5.place(x=280, y=350)

l7 = Label(win, text="Balance :", font=("Arial", 18, 'bold'), bg="#0F5D92")
l7.place(x=100, y=400)

b1 = Button(win, text="ADD", bd=5, font=f1, command=maxrec)
b1.place(x=120, y=450)

b2 = Button(win, text="BAL", bd=5, font=f1, command=upd_bal)
b2.place(x=195, y=450)

b3 = Button(win, text="CLOSE", bd=5, font=f1, command=close)
b3.place(x=270, y=450)

b5 = Button(win, text="EXIT", bd=5, font=f1, command=exit_fun)
b5.place(x=375, y=450)

win.mainloop()
