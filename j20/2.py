from tkinter import *

# import tkinter as tk


def showFullName():
    fullName = f"نام کامل شما {fname_ent.get()} {lname_ent.get()} است"
    fullName_lbl.config(text=fullName)


mohammad = Tk()
mohammad.title("fullname app")
mohammad.geometry("425x475")
mohammad.resizable(0, False)
# mohammad.config(bg="lightgreen")

fname_lbl = Label(mohammad, text="نام", font=(("vazir", 16, "bold"))).place(x=350, y=10)
fname_ent = Entry(mohammad, font=(("vazir", 14, "bold")), justify="right")
fname_ent.place(x=20, y=10)
lname_lbl = Label(mohammad, text="نام خانوادگی", font=(("vazir", 16, "bold"))).place(x=260, y=120)
lname_ent = Entry(mohammad, font=(("vazir", 14, "bold")), justify="right")
lname_ent.place(x=20, y=120)
fullName_btn = Button(
    mohammad,
    text="کلیک کنید",
    font=(("vazir", 16, "bold")),
    bg="lightgreen",
    fg="red",
    command=showFullName,
).place(x=150, y=200)
fullName_lbl = Label(mohammad, text="", font=(("vazir", 16, "bold")))
fullName_lbl.place(x=100, y=300)

mohammad.mainloop()
