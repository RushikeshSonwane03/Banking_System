from datetime import date

from tkcalendar import DateEntry
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

import mysql.connector

today = date.today()

def format_date(date_str):
    str1 = date_str[0:4]
    str2 = date_str[4:7]
    str3 = date_str[7:]
    return str1 + str3 + str2


def get_age():
    date = b_date.get()
    y = date[6:]
    m = date[0:2]
    d = date[3:5]
    age = today.year - y - ((today.month, today.day) < (m, d))
    t6.config(state='normal')
    t6.delete('1.0', END)
    t6.insert(END, age)
    t6.config(state='disabled')


def clrfield():
    t2.delete(0, END)
    t3.delete(0, END)
    t4.delete(0, END)
    t5.delete(0, END)
    t6.delete(0, END)
    t7.delete(0, END)
    t8.delete(0, END)
    b_date.delete(0, END)
    gender.delete(0, END)


def maxrec():
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="k2it_python_project"
    )
    mycur = mydb.cursor()
    mycur.execute("select max(apno) from Applicant")
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


def saverec():
    s1 = t1.get()
    s2 = t2.get()
    s3 = t3.get()
    s4 = t4.get()
    s5 = t5.get()
    s6 = t6.get()
    s7 = t7.get()
    s8 = t8.get()
    birth_date = format_date(str(b_date.get_date()))
    gender_selected = gender.get()
    print(gender_selected)

    if s2 == "":
        messagebox.showinfo("Warn...", "Plz Enter Applicant Name")
        return
    if s3 == "":
        messagebox.showinfo("Warn...", "Plz Enter Applicant Address")
        return
    if s4 == "":
        messagebox.showinfo("Warn...", "Plz Enter Applicant City")
        return
    if s5 == "":
        messagebox.showinfo("Warn...", "Plz Enter Contact No")
        return
    if s6 == "":
        messagebox.showinfo("Warn...", "Plz Enter Applicant Age(yrs)")
        return
    if s7 == "":
        messagebox.showinfo("Warn...", "Plz Enter Nomini Name")
        return
    if s8 == "":
        messagebox.showinfo("Warn...", "Plz Enter OpBal")
        return
    if gender_selected == "":
        messagebox.showinfo("Warn...", "Plz Select Gender")
        return
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="k2it_python_project"
    )
    mycur = mydb.cursor()
    mycur.execute("insert into applicant values(" + s1 + ",'" + s2 + "','" + s3 + "','" + s4 + "','" + s5 + "','" + birth_date + "','" + s6 + "','" + gender_selected + "','" + s7 + "','" + s8 + "','active')")
    mydb.commit()
    messagebox.showinfo("Confirm...", "Rec is Saved")
    maxrec()


def uprec():
    s1 = t1.get()
    s2 = t2.get()
    s3 = t3.get()
    s4 = t4.get()
    s5 = t5.get()
    s6 = t6.get()
    s7 = t7.get()
    s8 = t8.get()
    birth_date = format_date(str(b_date.get_date()))
    gender_selected = gender.get()
    print(gender_selected)
    # print(s1 + '\n' + s2 + '\n' + s3 + '\n' + s4 + '\n' + s5 + '\n' + s6 + '\n' + s7 + '\n' + s8)
    # print(birth_date)

    if s2 == "":
        messagebox.showinfo("Warn...", "Plz Enter Applicant Name")
        return
    if s3 == "":
        messagebox.showinfo("Warn...", "Plz Enter Applicant Address")
        return
    if s4 == "":
        messagebox.showinfo("Warn...", "Plz Enter Applicant City")
        return
    if s5 == "":
        messagebox.showinfo("Warn...", "Plz Enter Contact No")
        return
    if s6 == "":
        messagebox.showinfo("Warn...", "Plz Enter Applicant Age(yrs)")
        return
    if s7 == "":
        messagebox.showinfo("Warn...", "Plz Enter Nomini Name")
        return
    if s8 == "":
        messagebox.showinfo("Warn...", "Plz Enter OpBal")
        return
    if gender_selected == "":
        messagebox.showinfo("Warn...", "Plz Select Gender")
        return
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="k2it_python_project"
    )
    mycur = mydb.cursor()
    mycur.execute("update Applicant set apname='" + s2 + "',apadd='" + s3 + "',city='" + s4 + "',contact='" + s5 + "', bdate='" + birth_date + "',age='" + s6 + "',gender='" + gender_selected + "',nomini='" + s7 + "',apbal='" + s8 + "' where apno=" + s1)
    mydb.commit()
    messagebox.showinfo("Confirm...", "Rec is Updated")
    maxrec()

def serrec():
    s1 = t1.get()
    if s1 == "":
        messagebox.showinfo("Warn...", "Plz Enter Applicant No")
        return
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="k2it_python_project"
    )
    mycur = mydb.cursor()
    mycur.execute("Select * from Applicant where apno=" + s1)
    data = mycur.fetchone()
    print(data)
    clrfield()
    if data is None:
        messagebox.showinfo("Warm...", "Rec is not found")
    else:
        t2.insert(0, data[1])
        t3.insert(0, data[2])
        t4.insert(0, data[3])
        t5.insert(0, data[4])
        b_date.insert(0, data[5])
        t6.insert(0, data[6])
        gender.insert(0, data[7])
        t7.insert(0, data[8])
        t8.insert(0, data[9])


def delrec():
    ans = messagebox.askyesnocancel("Confirm...", "Are you sure Delete ?")
    if ans:
        s1 = t1.get()
        mydb = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            database="k2it_python_project"
        )
        mycur = mydb.cursor()
        mycur.execute("Delete from Applicant where apno=" + s1)
        mydb.commit()
        messagebox.showinfo("Confirm...", "Rec is Deleted")
        maxrec()


def exit_fun():
    ans = messagebox.askyesnocancel("Confirm Exit", "Are you sure you want to exit ? ")
    if ans:
        win.destroy()
        import main


win = Tk()
win.title("Applicant Registration Form")
win.geometry("1000x600+100+50")
f0 = ("Arial", 30, 'bold', 'italic')
f1 = ("Arial", 15, 'bold')
f2 = ("timesnewroman", 12, 'normal')

bgimg = PhotoImage(file="images\zabc.png")

limg = Label(win, image=bgimg)
limg.pack()

l1 = Label(win, text="Applicant Registration Form", font=f0)
l1.place(x=50, y=30)

l2 = Label(win, text="ApNo", font=f1)
l2.place(x=100, y=100)

t1 = Entry(win, font=f2)
t1.place(x=280, y=100)

l3 = Label(win, text="ApName", font=f1)
l3.place(x=100, y=150)

t2 = Entry(win, font=f2)
t2.place(x=280, y=150)

l4 = Label(win, text="Address", font=f1)
l4.place(x=100, y=200)

t3 = Entry(win, font=f2)
t3.place(x=280, y=200)

l5 = Label(win, text="City", font=f1)
l5.place(x=100, y=250)

t4 = Entry(win, font=f2)
t4.place(x=280, y=250)

l6 = Label(win, text="Contact", font=f1)
l6.place(x=100, y=300)

t5 = Entry(win, font=f2)
t5.place(x=280, y=300)

l7 = Label(win, text="BirthDate", font=f1)
l7.place(x=100, y=350)

b_date = DateEntry(win, selectmode='day', date_pattern='MM-dd-yyyy')
b_date.set_date(date.today())
b_date.place(x=280, y=350)

l12 = Label(win, text='---', font=f1, fg='white', bg='red')
l12.place(x=400, y=345)

l8 = Label(win, text="Gender", font=f1)
l8.place(x=100, y=400)

Genders = ['Male', 'Female', 'Others']
gender = Combobox(win, values=Genders, postcommand=get_age)
gender.place(x=280, y=400)

l9 = Label(win, text="Age (yrs)", font=f1)
l9.place(x=100, y=450)

t6 = Entry(win, font=f2)
t6.place(x=280, y=450)

l10 = Label(win, text="Nomini", font=f1)
l10.place(x=100, y=500)

t7 = Entry(win, font=f2)
t7.place(x=280, y=500)

l11 = Label(win, text="OpBal", font=f1)
l11.place(x=100, y=550)

t8 = Entry(win, font=f2)
t8.place(x=280, y=550)

b1 = Button(win, text="ADD", bd=5, font=f1, command=maxrec)
b1.place(x=500, y=400)

b2 = Button(win, text="SAVE", bd=5, font=f1, command=saverec)
b2.place(x=500, y=470)

b3 = Button(win, text="UPDATE", bd=5, font=f1, command=uprec)
b3.place(x=590, y=470)

b4 = Button(win, text="SEARCH", bd=5, font=f1, command=serrec)
b4.place(x=500, y=540)

b5 = Button(win, text="DELETE", bd=5, font=f1, command=delrec)
b5.place(x=620, y=540)

b6 = Button(win, text="EXIT", bd=5, font=f1, command=exit_fun)
b6.place(x=740, y=540)

win.mainloop()
