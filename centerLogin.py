import tkinter
from tkinter import messagebox as msg
from connection import *
from tkinter import ttk
import dashboard


class Main:
    def __init__(self):
        self.root = tkinter.Tk()
        #self.centerdetail = centerdetails
        self.root.geometry("500x500")
        self.root.title("Login")
        self.primarycolor = "#8EA8C3"
        self.secondaycolor = "#B1BFD7"
        self.txtcolor = "black"
        self.title = tkinter.Label(self.root, text="Center Login", font=("Arial", "20", "bold"),bg=self.primarycolor,fg=self.txtcolor,width=10)
        self.title.pack(pady=20)

        self.formFont = ("Arial", 14)


        self.root.configure(bg=self.secondaycolor)

        self.conn = Connect()
        self.cur = self.conn.cursor()

        self.formFrame = tkinter.Frame(self.root,bg=self.primarycolor,highlightthickness=2,highlightbackground="black")
        self.formFrame.pack()

        self.lb1 = tkinter.Label(self.formFrame, text="Enter Email", font=self.formFont,bg=self.primarycolor)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1 = tkinter.Entry(self.formFrame, font=self.formFont,relief="solid")
        self.txt1.grid(row=0, column=1, padx=10, pady=10)

        self.lb2 = tkinter.Label(self.formFrame, text="Enter Password", font=self.formFont,bg=self.primarycolor)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2 = tkinter.Entry(self.formFrame, font=self.formFont,relief="solid")
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.buttonFrame = tkinter.Frame(self.root, bg=self.secondaycolor)
        self.buttonFrame.pack()

        self.btn3=tkinter.Button(self.buttonFrame,text="Login",font=self.formFont,command=self.centerLogin,width=12,bg=self.primarycolor,fg=self.txtcolor,relief="raised")
        self.btn3.grid(row=0, column=0, padx=10, pady=30)

        # self.btn = tkinter.Button(self.root, text="Submit", font=self.formFont, command=self.getFormValues)
        # self.btn.pack(pady=10)

        self.root.mainloop()

    def centerLogin(self):
        email=self.txt1.get()
        password=self.txt2.get()
        q=f"select * from center where email='{email}' and password='{password}'"
        print(q)
        self.cur.execute(q)
        data=self.cur.fetchall()
        print(data)
        if len(data)==0:
            msg.showwarning("Warning", "Invalid Email/Password",parent=self.root)
        else:
            msg.showinfo("Success","Login Successful",parent=self.root)
            self.root.destroy()
            dashboard.centerdashboard(admindetails=data)


if __name__ == "__main__":
    obj = Main()