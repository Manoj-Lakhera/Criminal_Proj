import tkinter
from tkinter import messagebox as msg
from connection import *
from tkinter import ttk


class Main:
    def __init__(self,email):
        self.email = email
        print(self.email)
        self.root = tkinter.Tk()
        self.root.geometry("600x600")
        self.root.title("Change Password")
        self.primarycolor = "#8EA8C3"
        self.secondaycolor = "#CBF7ED"
        self.txtcolor = "black"
        self.title = tkinter.Label(self.root, text="Change Admin Password", font=("Arial", "20", "bold"),
                                   bg=self.primarycolor, fg=self.txtcolor)
        self.title.pack(pady=40)

        self.formFont = ("Arial", 14)

        self.root.configure(bg=self.secondaycolor)

        self.conn = Connect()
        self.cur = self.conn.cursor()

        self.formFrame = tkinter.Frame(self.root, bg=self.primarycolor, highlightthickness=2,
                                       highlightbackground="black")
        self.formFrame.pack()

        self.lb1 = tkinter.Label(self.formFrame, text="Enter Email", font=self.formFont, bg=self.primarycolor)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1 = tkinter.Entry(self.formFrame, font=self.formFont, relief="solid")
        self.txt1.grid(row=0, column=1, padx=10, pady=10)
        self.txt1.insert(0,self.email)

        self.lb2 = tkinter.Label(self.formFrame, text="Enter Old Password", font=self.formFont, bg=self.primarycolor)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2 = tkinter.Entry(self.formFrame, font=self.formFont, relief="solid")
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.lb3 = tkinter.Label(self.formFrame, text="Enter New Password", font=self.formFont, bg=self.primarycolor)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3 = tkinter.Entry(self.formFrame, font=self.formFont, relief="solid")
        self.txt3.grid(row=2, column=1, padx=10, pady=10)

        self.lb4 = tkinter.Label(self.formFrame, text="Confirm Password", font=self.formFont, bg=self.primarycolor)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4 = tkinter.Entry(self.formFrame, font=self.formFont, show="*", relief="solid")
        self.txt4.grid(row=3, column=1, padx=10, pady=10)

        self.buttonFrame = tkinter.Frame(self.root, bg=self.secondaycolor)
        self.buttonFrame.pack()

        self.btn3 = tkinter.Button(self.buttonFrame, text="Submit", font=self.formFont, command=self.changePassword,
                                   width=12, bg=self.primarycolor, fg=self.txtcolor, relief="raised")
        self.btn3.grid(row=0, column=0, padx=10, pady=30)

        self.root.mainloop()

    def changePassword(self):
        email = self.txt1.get()
        self.oldpassword = self.txt2.get()
        self.newpassword = self.txt3.get()
        self.confirmpassword = self.txt4.get()

        if self.email == '' or self.oldpassword == "" or self.newpassword == '' or self.confirmpassword == "":
            msg.showwarning("Warning", "Please Enter Values.")

        else:
            q = f"select * from admin where email='{email}' and password='{self.oldpassword}'"
            self.cur.execute(q)
            s=self.cur.fetchall()
            if len(s) == 0:
                msg.showwarning("warning!", "This Pass doesnt exist!")
            else:
                if self.newpassword != self.confirmpassword:
                    msg.showwarning("password doesn't match!", "This Password doesn't match!")
                else:
                    q1 = f"update admin set password='{self.newpassword}'where email='{email}'"
                    self.cur.execute(q1)
                    self.conn.commit()
                    msg.showinfo("")


if __name__ == "__main__":
    obj = Main("k@gmail.com")