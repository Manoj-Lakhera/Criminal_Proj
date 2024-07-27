import tkinter
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import Connect

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')
        self.root.title('Python MySQL Read Operation')

        self.conn = Connect()
        self.cur = self.conn.cursor()

        self.mainLabel = Label(self.root, text='View Admin',font=('Arial',28,'bold'))
        self.mainLabel.pack(pady=20)

        self.searchFrame = Frame(self.root)
        self.searchFrame.pack(pady=20)

        self.lbl = Label(self.searchFrame, text='Search', font=('Arial', 14))
        self.lbl.grid(row=0, column=0, pady=10, padx=10)
        self.txt1 = Entry(self.searchFrame, font=('Arial', 14))
        self.txt1.grid(row=0, column=1, pady=10, padx=10)
        self.btn1 = Button(self.searchFrame, text='Search', font=('Arial', 14), command=self.searchAdmin)
        self.btn1.grid(row=0, column=2, pady=10, padx=10)
        self.btn2 = Button(self.searchFrame, text='Refresh', font=('Arial', 14), command=self.resetAdmin)
        self.btn2.grid(row=0, column=3, pady=10, padx=10)
        self.btn3 = Button(self.searchFrame, text='Delete', font=('Arial', 14), command=self.deleteAdmin)
        self.btn3.grid(row=0, column=4, pady=10, padx=10)


        self.adminTable = ttk.Treeview(self.root, columns=['id', 'name', 'email', 'mobile','role'])
        self.adminTable.pack(expand=True, fill='both', padx=20, pady=20)
        self.adminTable.heading('id', text="ID")
        self.adminTable.heading('name', text="Name")
        self.adminTable.heading('email', text="Email")
        self.adminTable.heading('mobile', text="Mobile")
        self.adminTable.heading('role', text="Role")
        self.adminTable['show'] = 'headings'
        self.getValues()
        self.adminTable.bind('<Double-1>',self.updateWindow)

        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 14), rowheight=40)
        style.configure("Treeview.Heading", font=("Arial", 14))

        self.root.mainloop()

    def getValues(self):
        q = f"select id,name,email,mobile,role from admin"
        self.cur.execute(q)
        result = self.cur.fetchall()
        for row in self.adminTable.get_children():
            self.adminTable.delete(row)

        index = 0
        for row in result:
            self.adminTable.insert("", index=index, values=row)
            index += 1

    def resetAdmin(self):
        self.txt1.delete(0, 'end')
        self.getValues()

    def searchAdmin(self):
        text = self.txt1.get()
        q = f"select id,name,email,mobile,role from admin where id like '%{text}%' or name like '%{text}%' or email like '%{text}%' or mobile like '%{text}%' or role like '%{text}%'"
        self.cur.execute(q)
        result = self.cur.fetchall()

        for row in self.adminTable.get_children():
            self.adminTable.delete(row)

        index = 0
        for row in result:
            self.adminTable.insert("", index=index, values=row)
            index += 1

    def deleteAdmin(self):
        row = self.adminTable.selection()
        if len(row) == 0:
            msg.showwarning("Warning", "No Data Found")
        else:
            row_id = row[0]
            items = self.adminTable.item(row_id)
            data = items["values"]
            confirm = msg.askyesno("Warning", "Do you want to delete?")
            if confirm:
                q = f"delete from city where id ='{data[0]}'"
                self.cur.execute(q)
                self.conn.commit()
                self.resetAdmin()
                msg.showinfo("Delete", "Deletion Successful")
            else:
                msg.showinfo("Delete", "Deletion Failed")

    def updateWindow(self,e):
        row = self.adminTable.selection()
        row_id = row[0]
        items = self.adminTable.item(row_id)
        data = items["values"]
        self.root1 = tkinter.Tk()
        self.root1.geometry("650x650")
        self.root1.title("Admin")
        self.title = tkinter.Label(self.root1, text="Update Admin", font=("Arial", "20", "bold"))
        self.title.pack(pady=10)

        self.formFont = ("Arial", 14)

        self.conn = Connect()
        self.cur = self.conn.cursor()

        self.formFrame = tkinter.PanedWindow(self.root1)
        self.formFrame.pack()

        self.lb1 = tkinter.Label(self.formFrame, text="Enter ID", font=self.formFont)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1 = tkinter.Entry(self.formFrame, font=self.formFont)
        self.txt1.grid(row=0, column=1, padx=10, pady=10)
        self.txt1.insert(0, data[0])
        self.txt1.configure(state="readonly")

        self.lb2 = tkinter.Label(self.formFrame, text="Enter Name", font=self.formFont)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2 = tkinter.Entry(self.formFrame, font=self.formFont)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)
        self.txt2.insert(0, data[1])

        self.lb3 = tkinter.Label(self.formFrame, text="Enter Email", font=self.formFont)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3 = tkinter.Entry(self.formFrame, font=self.formFont)
        self.txt3.grid(row=2, column=1, padx=10, pady=10)
        self.txt3.insert(0, data[2])

        self.lb4 = tkinter.Label(self.formFrame, text="Enter Mobile", font=self.formFont)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4 = tkinter.Entry(self.formFrame, font=self.formFont)
        self.txt4.grid(row=3, column=1, padx=10, pady=10)
        self.txt4.insert(0, data[3])

        self.lb5 = tkinter.Label(self.formFrame, text="Enter Role", font=self.formFont)
        self.lb5.grid(row=4, column=0, padx=10, pady=10)

        # Define role values
        role_values = ["Admin", "Super Admin"]

        # Create the combobox
        self.role_combobox = ttk.Combobox(self.formFrame, values=role_values, font=self.formFont)
        self.role_combobox.grid(row=4, column=1, padx=10, pady=10)
        self.role_combobox.insert(0, data[4])

        self.buttonFrame = tkinter.Frame(self.root1)
        self.buttonFrame.pack()

        self.btn = tkinter.Button(self.buttonFrame, text="Update", font=self.formFont, command=self.getFormValues)
        self.btn.grid(row=0, column=0, padx=10, pady=10)

        self.root1.mainloop()

    def getFormValues(self):
        self.id = self.txt1.get()
        self.name = self.txt2.get()
        self.email = self.txt3.get()
        self.mobile = self.txt4.get()
        self.role = self.role_combobox.get()

        if self.name == "" or self.email == "" or self.mobile == "" or self.role == '':
            msg.showwarning("Warning", "Enter your Values")
        else:
            q = f"update admin set name='{self.name}' , email='{self.email}' , mobile='{self.mobile}' , role='{self.role}'where id='{self.id}'"
            self.cur.execute(q)
            self.conn.commit()
            self.getValues()
            msg.showinfo("Success","Updation Successful",parent=self.root1)
            self.root1.destroy()

if __name__ == "__main__":
    obj = Main()