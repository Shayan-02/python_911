from tkinter import *

f = open("./j30/t2.txt", 'r', encoding='utf-8')

def click():
    with open('./j30/t.txt', 'a', encoding="utf-8") as t:
        text = e1.get()
        t.write(f"{text}\n")
        # print(text)

# f.write("\nsalam")
s = f.read()

root = Tk()
root.geometry("200x300")

lbl = Label(root, text=s)
lbl.pack()

e1 = Entry(root, width=20)
e1.pack()

b1 = Button(root, text="کلیک کنید", command=click)
b1.pack()

root.mainloop()

f.close()
