from tkinter import messagebox
n = int(input("enter a number: "))

if n == 0:
    messagebox.showerror("invalid input", "n must not 0")
print("continue")
