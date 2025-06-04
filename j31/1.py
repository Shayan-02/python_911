import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

DB_NAME = "atm.db"


def format_currency(amount):
    return f"{int(amount):,}"


def setup_database():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            card TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            password TEXT NOT NULL,
            balance REAL DEFAULT 0
        )
    """
    )
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            card TEXT,
            type TEXT,
            amount REAL,
            time TEXT,
            FOREIGN KEY (card) REFERENCES users(card)
        )
    """
    )
    conn.commit()
    conn.close()


class ATMApp:
    def __init__(self, master):
        setup_database()
        self.master = master
        self.master.configure(bg="#e0f7fa")
        self.master.title(" **ATM** ")
        self.master.geometry("500x550")
        self.font = ("B Nazanin", 14)
        self.current_user = None
        self.login_screen()

    def clear(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def login_screen(self):
        self.clear()
        tk.Label(
            self.master, text="شماره کارت را وارد کنید", font=self.font, bg="#e0f7fa"
        ).pack(pady=10)
        self.card_entry = tk.Entry(self.master, font=self.font)
        self.card_entry.pack(pady=5)
        tk.Label(
            self.master, text="رمز عبور را وارد کنید", font=self.font, bg="#e0f7fa"
        ).pack(pady=10)
        self.pass_entry = tk.Entry(self.master, show="*", font=self.font)
        self.pass_entry.pack(pady=5)
        tk.Button(
            self.master,
            text="ورود",
            bg="#00796b",
            fg="white",
            font=self.font,
            command=self.login,
        ).pack(pady=10)
        tk.Button(
            self.master,
            text="ثبت‌نام",
            bg="#00796b",
            fg="white",
            font=self.font,
            command=self.register_screen,
        ).pack()

    def register_screen(self):
        self.clear()
        tk.Label(
            self.master, text="نام و نام خانوادگی", font=self.font, bg="#e0f7fa"
        ).pack(pady=5)
        self.name_entry = tk.Entry(self.master, font=self.font)
        self.name_entry.pack(pady=5)
        tk.Label(
            self.master, text="شماره کارت (۱۶ رقم)", font=self.font, bg="#e0f7fa"
        ).pack(pady=5)
        self.new_card_entry = tk.Entry(self.master, font=self.font)
        self.new_card_entry.pack(pady=5)
        tk.Label(
            self.master, text="رمز عبور (۴ رقم)", font=self.font, bg="#e0f7fa"
        ).pack(pady=5)
        self.new_pass_entry = tk.Entry(self.master, show="*", font=self.font)
        self.new_pass_entry.pack(pady=5)
        tk.Label(self.master, text="موجودی اولیه", font=self.font, bg="#e0f7fa").pack(
            pady=5
        )
        self.balance_entry = tk.Entry(self.master, font=self.font)
        self.balance_entry.pack(pady=5)
        tk.Button(
            self.master,
            text="ایجاد حساب",
            bg="#00796b",
            fg="white",
            font=self.font,
            command=self.register,
        ).pack(pady=10)
        tk.Button(
            self.master, text="بازگشت", font=self.font, command=self.login_screen
        ).pack()

    def register(self):
        name = self.name_entry.get()
        card = self.new_card_entry.get()
        password = self.new_pass_entry.get()
        balance = self.balance_entry.get()

        if not card.isdigit() or len(card) != 16:
            messagebox.showerror("خطا", "شماره کارت باید ۱۶ رقم باشد.")
            return
        if not password.isdigit() or len(password) != 4:
            messagebox.showerror("خطا", "رمز عبور باید ۴ رقم باشد.")
            return
        if not balance.replace(".", "", 1).isdigit():
            messagebox.showerror("خطا", "موجودی باید عددی باشد.")
            return

        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        try:
            c.execute(
                "INSERT INTO users (card, name, password, balance) VALUES (?, ?, ?, ?)",
                (card, name, password, float(balance)),
            )
            conn.commit()
            messagebox.showinfo("موفقیت", "حساب با موفقیت ایجاد شد.")
            self.login_screen()
        except sqlite3.IntegrityError:
            messagebox.showerror("خطا", "این شماره کارت قبلاً ثبت شده است.")
        finally:
            conn.close()

    def login(self):
        card = self.card_entry.get()
        password = self.pass_entry.get()
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE card=? AND password=?", (card, password))
        user = c.fetchone()
        conn.close()
        if user:
            self.current_user = card
            self.dashboard()
        else:
            messagebox.showerror("خطا", "شماره کارت یا رمز عبور اشتباه است.")

    def dashboard(self):
        self.clear()
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("SELECT name FROM users WHERE card=?", (self.current_user,))
        name = c.fetchone()[0]
        conn.close()
        tk.Label(
            self.master, text=f"خوش آمدید {name}", font=self.font, bg="#e0f7fa"
        ).pack(pady=10)
        tk.Button(
            self.master, text="موجودی", font=self.font, command=self.check_balance
        ).pack(pady=5)
        tk.Button(
            self.master, text="واریز", font=self.font, command=self.deposit_screen
        ).pack(pady=5)
        tk.Button(
            self.master, text="برداشت", font=self.font, command=self.withdraw_screen
        ).pack(pady=5)
        tk.Button(
            self.master, text="انتقال وجه", font=self.font, command=self.transfer_screen
        ).pack(pady=5)
        tk.Button(
            self.master,
            text="تغییر رمز",
            font=self.font,
            command=self.change_password_screen,
        ).pack(pady=5)
        tk.Button(
            self.master,
            text="حذف حساب",
            font=self.font,
            command=self.delete_account_screen,
        ).pack(pady=5)
        tk.Button(
            self.master,
            text="تاریخچه تراکنش‌ها",
            font=self.font,
            command=self.transaction_history,
        ).pack(pady=5)
        tk.Button(
            self.master, text="خروج", font=self.font, command=self.login_screen
        ).pack(pady=10)

    def check_balance(self):
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("SELECT balance FROM users WHERE card=?", (self.current_user,))
        balance = c.fetchone()[0]
        conn.close()
        messagebox.showinfo("موجودی", f"موجودی شما: {format_currency(balance)} تومان")

    def deposit_screen(self):
        self.clear()
        tk.Label(
            self.master, text="مبلغ واریزی را وارد کنید", font=self.font, bg="#e0f7fa"
        ).pack(pady=10)
        self.deposit_entry = tk.Entry(self.master, font=self.font)
        self.deposit_entry.pack(pady=5)
        tk.Button(self.master, text="تأیید", font=self.font, command=self.deposit).pack(
            pady=5
        )
        tk.Button(
            self.master, text="بازگشت", font=self.font, command=self.dashboard
        ).pack(pady=5)

    def deposit(self):
        amount = self.deposit_entry.get()
        if not amount.replace(".", "", 1).isdigit():
            messagebox.showerror("خطا", "مبلغ نامعتبر است.")
            return
        amount = float(amount)
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute(
            "UPDATE users SET balance = balance + ? WHERE card=?",
            (amount, self.current_user),
        )
        c.execute(
            "INSERT INTO transactions (card, type, amount, time) VALUES (?, 'واریز', ?, ?)",
            (self.current_user, amount, datetime.now().isoformat()),
        )
        conn.commit()
        conn.close()
        messagebox.showinfo("موفقیت", "واریز با موفقیت انجام شد.")
        self.dashboard()

    # ادامه کد در پیام بعدی

    def withdraw_screen(self):
        self.clear()
        tk.Label(
            self.master, text="مبلغ برداشت را وارد کنید", font=self.font, bg="#e0f7fa"
        ).pack(pady=10)
        self.withdraw_entry = tk.Entry(self.master, font=self.font)
        self.withdraw_entry.pack(pady=5)
        tk.Button(
            self.master, text="تأیید", font=self.font, command=self.withdraw
        ).pack(pady=5)
        tk.Button(
            self.master, text="بازگشت", font=self.font, command=self.dashboard
        ).pack(pady=5)

    def withdraw(self):
        amount = self.withdraw_entry.get()
        if not amount.replace(".", "", 1).isdigit():
            messagebox.showerror("خطا", "مبلغ نامعتبر است.")
            return
        amount = float(amount)
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("SELECT balance FROM users WHERE card=?", (self.current_user,))
        balance = c.fetchone()[0]
        if balance >= amount:
            c.execute(
                "UPDATE users SET balance = balance - ? WHERE card=?",
                (amount, self.current_user),
            )
            c.execute(
                "INSERT INTO transactions (card, type, amount, time) VALUES (?, 'برداشت', ?, ?)",
                (self.current_user, amount, datetime.now().isoformat()),
            )
            conn.commit()
            messagebox.showinfo("موفقیت", "برداشت با موفقیت انجام شد.")
        else:
            messagebox.showerror("خطا", "موجودی کافی نیست.")
        conn.close()
        self.dashboard()

    def transfer_screen(self):
        self.clear()
        tk.Label(
            self.master, text="شماره کارت مقصد", font=self.font, bg="#e0f7fa"
        ).pack(pady=5)
        self.dest_card_entry = tk.Entry(self.master, font=self.font)
        self.dest_card_entry.pack(pady=5)
        tk.Label(self.master, text="مبلغ انتقال", font=self.font, bg="#e0f7fa").pack(
            pady=5
        )
        self.transfer_amount_entry = tk.Entry(self.master, font=self.font)
        self.transfer_amount_entry.pack(pady=5)
        tk.Button(
            self.master, text="تأیید", font=self.font, command=self.transfer
        ).pack(pady=5)
        tk.Button(
            self.master, text="بازگشت", font=self.font, command=self.dashboard
        ).pack(pady=5)

    def transfer(self):
        dest_card = self.dest_card_entry.get()
        amount = self.transfer_amount_entry.get()
        if (
            not amount.replace(".", "", 1).isdigit()
            or not dest_card.isdigit()
            or len(dest_card) != 16
        ):
            messagebox.showerror("خطا", "اطلاعات نامعتبر است.")
            return
        amount = float(amount)
        if dest_card == self.current_user:
            messagebox.showerror("خطا", "نمی‌توانید به حساب خودتان انتقال دهید.")
            return

        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("SELECT balance FROM users WHERE card=?", (self.current_user,))
        sender_balance = c.fetchone()
        if not sender_balance or sender_balance[0] < amount:
            messagebox.showerror("خطا", "موجودی کافی نیست.")
            conn.close()
            return
        c.execute("SELECT * FROM users WHERE card=?", (dest_card,))
        if not c.fetchone():
            messagebox.showerror("خطا", "شماره کارت مقصد یافت نشد.")
            conn.close()
            return

        c.execute(
            "UPDATE users SET balance = balance - ? WHERE card=?",
            (amount, self.current_user),
        )
        c.execute(
            "UPDATE users SET balance = balance + ? WHERE card=?", (amount, dest_card)
        )
        c.execute(
            "INSERT INTO transactions (card, type, amount, time) VALUES (?, 'انتقال (خارج)', ?, ?)",
            (self.current_user, amount, datetime.now().isoformat()),
        )
        c.execute(
            "INSERT INTO transactions (card, type, amount, time) VALUES (?, 'انتقال (دریافتی)', ?, ?)",
            (dest_card, amount, datetime.now().isoformat()),
        )
        conn.commit()
        conn.close()
        messagebox.showinfo("موفقیت", "انتقال وجه با موفقیت انجام شد.")
        self.dashboard()

    def change_password_screen(self):
        self.clear()
        tk.Label(self.master, text="رمز عبور جدید", font=self.font, bg="#e0f7fa").pack(
            pady=10
        )
        self.new_pass_entry = tk.Entry(self.master, show="*", font=self.font)
        self.new_pass_entry.pack(pady=5)
        tk.Button(
            self.master, text="بروزرسانی", font=self.font, command=self.change_password
        ).pack(pady=5)
        tk.Button(
            self.master, text="بازگشت", font=self.font, command=self.dashboard
        ).pack(pady=5)

    def change_password(self):
        new_pass = self.new_pass_entry.get()
        if not new_pass.isdigit() or len(new_pass) != 4:
            messagebox.showerror("خطا", "رمز عبور باید ۴ رقم باشد.")
            return
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute(
            "UPDATE users SET password=? WHERE card=?", (new_pass, self.current_user)
        )
        conn.commit()
        conn.close()
        messagebox.showinfo("موفقیت", "رمز عبور با موفقیت تغییر یافت.")
        self.dashboard()

    def delete_account_screen(self):
        self.clear()
        tk.Label(
            self.master,
            text="برای حذف حساب، رمز عبور خود را وارد کنید",
            font=self.font,
            bg="#e0f7fa",
        ).pack(pady=10)
        self.del_pass_entry = tk.Entry(self.master, show="*", font=self.font)
        self.del_pass_entry.pack(pady=5)
        tk.Button(
            self.master,
            text="حذف حساب",
            fg="white",
            bg="red",
            font=self.font,
            command=self.delete_account,
        ).pack(pady=5)
        tk.Button(
            self.master, text="بازگشت", font=self.font, command=self.dashboard
        ).pack(pady=5)

    def delete_account(self):
        entered_pass = self.del_pass_entry.get()
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("SELECT password FROM users WHERE card=?", (self.current_user,))
        real_pass = c.fetchone()[0]
        if entered_pass == real_pass:
            c.execute("DELETE FROM transactions WHERE card=?", (self.current_user,))
            c.execute("DELETE FROM users WHERE card=?", (self.current_user,))
            conn.commit()
            conn.close()
            messagebox.showinfo("حذف شد", "حساب شما با موفقیت حذف شد.")
            self.current_user = None
            self.login_screen()
        else:
            conn.close()
            messagebox.showerror("خطا", "رمز عبور نادرست است.")

    def transaction_history(self):
        self.clear()
        tk.Label(
            self.master, text="تاریخچه تراکنش‌ها", font=self.font, bg="#e0f7fa"
        ).pack(pady=10)
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute(
            "SELECT type, amount, time FROM transactions WHERE card=? ORDER BY time DESC",
            (self.current_user,),
        )
        transactions = c.fetchall()
        conn.close()
        if not transactions:
            tk.Label(
                self.master, text="تراکنشی یافت نشد", font=self.font, bg="#e0f7fa"
            ).pack()
        else:
            for t in transactions:
                tk.Label(
                    self.master,
                    text=f"{t[2][:19]} | {t[0]} | {format_currency(t[1])}",
                    font=self.font,
                    bg="#e0f7fa",
                ).pack()
        tk.Button(
            self.master, text="بازگشت", font=self.font, command=self.dashboard
        ).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()
