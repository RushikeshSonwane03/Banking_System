from tkinter import *
from tkinter import messagebox
import mysql.connector


def clrfield():
    t2.delete(0, END)
    t3.delete(0, END)
    t4.delete(0, END)
    t5.delete(0, END)


def maxrec():
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="k2it_python_project"
    )
    mycur = mydb.cursor()
    mycur.execute("select max(cno) from custmast")
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
    if s2 == "":
        messagebox.showinfo("Warn...", "Plz Enter Cust Name")
        return
    if s3 == "":
        messagebox.showinfo("Warn...", "Plz Enter Cust Address")
        return
    if s4 == "":
        messagebox.showinfo("Warn...", "Plz Enter Cust City")
        return
    if s5 == "":
        messagebox.showinfo("Warn...", "Plz Enter Contact No")
        return
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="k2it_python_project"
    )
    mycur = mydb.cursor()
    mycur.execute("insert into custmast values(" + s1 + ",'" + s2 + "','" + s3 + "','" + s4 + "','" + s5 + "')")
    mydb.commit()
    messagebox.showinfo("Confirm...", "Rec is Saved")
    maxrec()


def uprec():
    s1 = t1.get()
    s2 = t2.get()
    s3 = t3.get()
    s4 = t4.get()
    s5 = t5.get()
    if s2 == "":
        messagebox.showinfo("Warn...", "Plz Enter Cust Name")
        return
    if s3 == "":
        messagebox.showinfo("Warn...", "Plz Enter Cust Address")
        return
    if s4 == "":
        messagebox.showinfo("Warn...", "Plz Enter Cust City")
        return
    if s5 == "":
        messagebox.showinfo("Warn...", "Plz Enter Contact No")
        return
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="k2it_python_project"
    )
    mycur = mydb.cursor()
    mycur.execute(
        "update custmast set cname='" + s2 + "',cadd='" + s3 + "',city='"
        + s4 + "',contact='" + s5 + "' where cno=" + s1)
    mydb.commit()
    messagebox.showinfo("Confirm...", "Rec is Updated")
    maxrec()


def serrec():
    s1 = t1.get()
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="k2it_python_project"
    )
    mycur = mydb.cursor()
    mycur.execute("Select * from custmast where cno=" + s1)
    data = mycur.fetchone()
    if data is None:
        messagebox.showinfo("Warm...", "Rec is not found")
    else:
        t2.insert(0, data[1])
        t3.insert(0, data[2])
        t4.insert(0, data[3])
        t5.insert(0, data[4])


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
        mycur.execute("Delete from custmast where cno=" + s1)
        mydb.commit()
        messagebox.showinfo("Confirm...", "Rec is Deleted")
        maxrec()


def exit_fun():
    ans = messagebox.askyesnocancel("Confirm Exit", "Are you sure you want to exit ? ")
    if ans:
        win.destroy()
        import login


win = Tk()
win.title("Customer Entry Form")
win.geometry("600x600+100+50")
f0 = ("Arial", 30, 'bold', 'italic')
f1 = ("Arial", 15, 'bold')
f2 = ("timesnewroman", 12, 'normal')

bgimg = PhotoImage(file="images\keith-misner-h0Vxgz5tyXA-unsplash.png")

limg = Label(win, image=bgimg)
limg.pack()

l1 = Label(win, text="Customer Entry Form", font=f0)
l1.place(x=90, y=30)

l2 = Label(win, text="Cust_No", font=f1)
l2.place(x=100, y=150)

t1 = Entry(win, font=f2)
t1.place(x=280, y=150)

l3 = Label(win, text="Cust Name", font=f1)
l3.place(x=100, y=200)

t2 = Entry(win, font=f2)
t2.place(x=280, y=200)

l4 = Label(win, text="Address", font=f1)
l4.place(x=100, y=250)

t3 = Entry(win, font=f2)
t3.place(x=280, y=250)

l5 = Label(win, text="City", font=f1)
l5.place(x=100, y=300)

t4 = Entry(win, font=f2)
t4.place(x=280, y=300)

l6 = Label(win, text="Contact", font=f1)
l6.place(x=100, y=350)

t5 = Entry(win, font=f2)
t5.place(x=280, y=350)

b1 = Button(win, text="ADD", bd=5, font=f1, command=maxrec)
b1.place(x=50, y=425)

b2 = Button(win, text="SAVE", bd=5, font=f1, command=saverec)
b2.place(x=120, y=425)

b3 = Button(win, text="UPDATE", bd=5, font=f1, command=uprec)
b3.place(x=200, y=425)

b4 = Button(win, text="SER", bd=5, font=f1, command=serrec)
b4.place(x=310, y=425)

b5 = Button(win, text="DELETE", bd=5, font=f1, command=delrec)
b5.place(x=380, y=425)

b6 = Button(win, text="EXIT", bd=5, font=f1, command=exit_fun)
b6.place(x=490, y=425)

win.mainloop()
