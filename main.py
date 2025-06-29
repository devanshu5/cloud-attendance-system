
import mysql.connector
from tkinter import *
from tkinter import messagebox

def mark_attendance():
    name = entry_name.get()
    if name:
        cursor.execute("INSERT INTO attendance (name) VALUES (%s)", (name,))
        db.commit()
        messagebox.showinfo("Success", "Attendance marked")
    else:
        messagebox.showwarning("Input error", "Please enter your name")

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="attendance_system"
)
cursor = db.cursor()

root = Tk()
root.title("Attendance System")
Label(root, text="Enter Name:").pack()
entry_name = Entry(root)
entry_name.pack()
Button(root, text="Mark Attendance", command=mark_attendance).pack()
root.mainloop()
