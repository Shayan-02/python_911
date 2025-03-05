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

fname_lbl = Label(mohammad, text="firstname", font=(("vazir", 16, "bold"))).grid(row=0, column=0, pady=20, padx=20)
fname_ent = Entry(mohammad, font=(("vazir", 14, "bold")), justify="right")
fname_ent.grid(row=0, column=1)
lname_lbl = Label(mohammad, text="lastname", font=(("vazir", 16, "bold"))).grid(row=1, column=0)
lname_ent = Entry(mohammad, font=(("vazir", 14, "bold")), justify="right")
lname_ent.grid(row=1, column=1)
fullName_btn = Button(
    mohammad,
    text="click me",
    font=(("vazir", 16, "bold")),
    bg="lightgreen",
    fg="red",
    command=showFullName,
).grid(row=2, column=1, pady=40)
fullName_lbl = Label(mohammad, text="", font=(("vazir", 16, "bold")))
fullName_lbl.grid(row=3, column=1)

mohammad.mainloop()
