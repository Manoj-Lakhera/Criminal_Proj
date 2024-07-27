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

        self.mainLabel = Label(self.root, text='View Category',font=('Arial',28,'bold'))
        self.mainLabel.pack(pady=20)

        self.searchFrame = Frame(self.root)
        self.searchFrame.pack(pady=20)

        self.lbl = Label(self.searchFrame, text='Search', font=('Arial', 14))
        self.lbl.grid(row=0, column=0, pady=10, padx=10)
        self.txt1 = Entry(self.searchFrame, font=('Arial', 14))
        self.txt1.grid(row=0, column=1, pady=10, padx=10)
        self.btn1 = Button(self.searchFrame, text='Search', font=('Arial', 14), command=self.searchCategory)
        self.btn1.grid(row=0, column=2, pady=10, padx=10)
        self.btn2 = Button(self.searchFrame, text='Refresh', font=('Arial', 14), command=self.resetCategory)
        self.btn2.grid(row=0, column=3, pady=10, padx=10)
        self.btn3 = Button(self.searchFrame, text='Delete', font=('Arial', 14), command=self.deleteCategory)
        self.btn3.grid(row=0, column=4, pady=10, padx=10)


        self.categoryTable = ttk.Treeview(self.root, columns=['name','description'])
        self.categoryTable.pack(expand=True, fill='both', padx=20, pady=20)
        self.categoryTable.heading('name', text="Name")
        self.categoryTable.heading('description', text="Description")
        self.categoryTable['show'] = 'headings'
        self.getValues()

        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 14), rowheight=40)
        style.configure("Treeview.Heading", font=("Arial", 14))

        self.root.mainloop()

    def getValues(self):
        q = f"select * from category"
        self.cur.execute(q)
        result = self.cur.fetchall()
        for row in self.categoryTable.get_children():
            self.categoryTable.delete(row)

        index = 0
        for row in result:
            self.categoryTable.insert("", index=index, values=row)
            index += 1

    def resetCategory(self):
        self.txt1.delete(0, 'end')
        self.getValues()

    def searchCategory(self):
        text = self.txt1.get()
        q = f"select * from category where name like '%{text}%' or description like '%{text}%'"
        self.cur.execute(q)
        result = self.cur.fetchall()

        for row in self.categoryTable.get_children():
            self.categoryTable.delete(row)

        index = 0
        for row in result:
            self.categoryTable.insert("", index=index, values=row)
            index += 1

    def deleteCategory(self):
        row= self.categoryTable.selection()
        if len(row)==0:
            msg.showwarning("Warning","No Data Found")
        else:
            row_name=row[0]
            items=self.categoryTable.item(row_name)
            data=items["values"]
            confirm=msg.askyesno("Warning","Do you want to delete?")
            if confirm:
                q=f"delete from category where name ='{data[0]}'"
                self.cur.execute(q)
                self.conn.commit()
                self.resetCategory()
                msg.showinfo("Delete","Deletion Successful")
            else:
                msg.showinfo("Delete","Deletion Failed")


obj = Main()