from datetime import date
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

import mysql.connector
from tkcalendar import DateEntry

my_bal = int()

def upd_bal():
    s1 = t1.get()
    s3 = ap_no.get()
    if s1 == '':
        messagebox.showinfo("Warn...", "Plz Enter Transaction No")
        return
    elif s3 == '':
        messagebox.showinfo("Warn...", "Plz Enter Applicant No")
        return
    else:
        mydb = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            database="k2it_python_project"
        )
        mycur = mydb.cursor()
        mycur.execute("select apbal from Applicant where apno =" + s3)
        mydata = mycur.fetchone()
        interest = str(int(mydata[0]*0.07))
        t6.insert(0, '7')
        t7.insert(0, "$" + interest)
        global my_bal
        my_bal = str(mydata[0] + int(interest))
        balance = "Balance : $" + my_bal
        l9.config(text=balance)


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
    t2.delete(0, END)
    cal.delete(0, END)
    cal1.delete(0, END)
    ap_no.delete(0, END)
    t6.delete(0, END)
    t7.delete(0, END)
    l9.config(text="Balance :")


def maxrec():
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="k2it_python_project"
    )
    mycur = mydb.cursor()
    mycur.execute("select max(tr_no) from interest")
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


def inst():
    s1 = t1.get()
    s2 = format_date(str(t2.get_date()))
    s3 = format_date(str(cal.get_date()))
    s4 = format_date(str(cal1.get_date()))
    s5 = ap_no.get()
    s6 = t6.get()
    s7 = t7.get()
    print(s1)
    print(s2)
    print(s3)
    print(s4)
    print(s5)
    print(s6)
    print(s7)
    if s1 == "":
        messagebox.showinfo("Warn...", "Plz Enter Transaction No")
        return
    if s2 == "":
        messagebox.showinfo("Warn...", "Plz Select Transaction Date")
        return
    if s5 == "":
        messagebox.showinfo("Warn...", "Plz Select Applicant Name")
        return
    mydb = mysql.connector.connect(
        user="root",
        password="Test@123",
        host="localhost",
        database="k2it_pythontkinderproject"
    )
    mycur = mydb.cursor()
    mycur.execute("Insert into interest values(" + s1 + ",'" + s2 + "'," + s5 + ",'" + s3 + "','" + s4 + "'," + s6 + "," + s7[1:] + ");")
    mydb.commit()
    mycur.execute("Update Applicant SET apbal=" + my_bal + " where apno = " + s5)
    mydb.commit()
    messagebox.showinfo("Confirm...", "Interest added successsfully")
    maxrec()



def exit_fun():
    ans = messagebox.askyesnocancel("Confirm Exit", "Are you sure you want to exit ? ")
    if ans:
        win.destroy()
        import options


win = Tk()
win.title("Interest Page")
win.geometry("1000x600+100+50")
f0 = ("Arial", 30, 'bold', 'italic')
f1 = ("Arial", 15, 'bold')
f2 = ("timesnewroman", 12, 'normal')

bgimg = PhotoImage(file="images\zabc.png")

limg = Label(win, image=bgimg)
limg.pack()

frame = Frame(win, bg="#191970", width=515, height=550)
frame.place(x=50, y=30)

l1 = Label(win, text="Interest Page", font=f0)
l1.place(x=150, y=10)

l2 = Label(win, text="Tr No", font=f1)
l2.place(x=100, y=100)

t1 = Entry(win, font=f2)
t1.place(x=280, y=100)

l3 = Label(win, text="Tr Date", font=f1)
l3.place(x=100, y=150)

t2 = DateEntry(win, selectmode='day', date_pattern='MM-dd-yyyy')
t2.set_date(date.today())
t2.place(x=280, y=150)

l4 = Label(win, text="Int From", font=f1)
l4.place(x=100, y=200)

cal = DateEntry(win, selectmode='day', date_pattern='MM-dd-yyyy')
cal.set_date(date.today())
cal.place(x=280, y=200)

l5 = Label(win, text="Int Till", font=f1)
l5.place(x=100, y=250)

cal1 = DateEntry(win, selectmode='day', date_pattern='MM-dd-yyyy')
cal1.set_date(date.today())
cal1.place(x=280, y=250)

l6 = Label(win, text="Ap No", font=f1)
l6.place(x=100, y=300)

apno_list = apno_combobox()
ap_no = Combobox(win, values=apno_list)
ap_no.place(x=280, y=300)

l7 = Label(win, text="Int Rate", font=f1)
l7.place(x=100, y=350)

t6 = Entry(win, font=f2)
t6.place(x=280, y=350)

l8 = Label(win, text="Int Amount", font=f1)
l8.place(x=100, y=400)

t7 = Entry(win, font=f2)
t7.place(x=280, y=400)

l9 = Label(win, text="Balance :", font=("Arial", 18, 'bold'), bg="#191970", fg='white')
l9.place(x=100, y=450)

b1 = Button(win, text="ADD", bd=5, font=f1, command=maxrec)
b1.place(x=120, y=500)

b2 = Button(win, text="BAL", bd=5, font=f1, command=upd_bal)
b2.place(x=195, y=500)

b3 = Button(win, text="INTEREST", bd=5, font=f1, command=inst)
b3.place(x=270, y=500)

b4 = Button(win, text="EXIT", bd=5, font=f1, command=exit_fun)
b4.place(x=400, y=500)

win.mainloop()
