# DASHBOARD
import tkinter
import admin
import center
import criminal
import viewAdmin
import viewcenter
import viewcriminal
import changepassword

class centerdashboard:
    def __init__(self,centerdetails):
        self.centerdetail = centerdetails
        self.root = tkinter.Tk()
        self.root.state("zoomed")
        self.root.title('Insert Form')

        self.primaryColor = '#987D9A'
        self.secondaryColor = '#B1BFD7'
        self.txtColor = '#FEFBD8'

        self.mainMenu = tkinter.Menu(self.root)
        self.root.configure(menu=self.mainMenu)



        self.fileMenu = tkinter.Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label='Manage Criminal', menu=self.fileMenu)
        self.fileMenu.add_command(label='Add Criminal', command=criminal.Main)
        self.fileMenu.add_command(label='View Criminal',command=viewcriminal.Main)

        self.fileMenu = tkinter.Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label='Manage Admin', menu=self.fileMenu)
        self.fileMenu.add_command(label='Add Admin', command=admin.Main)
        self.fileMenu.add_command(label='View Admin', command=viewAdmin.Main)

        self.fileMenu = tkinter.Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label='Manage Center', menu=self.fileMenu)
        self.fileMenu.add_command(label='Add Center', command=center.Main)
        self.fileMenu.add_command(label='View Center', command=viewcenter.Main)

        self.fileMenu = tkinter.Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label='Manage Profile', menu=self.fileMenu)
        self.fileMenu.add_command(label='Change Password',command=changepassword.Main)
        self.fileMenu.add_command(label='Exit', command=self.exitWindow)

        self.root.configure(bg=self.primaryColor)

        self.root.mainloop()

    def exitWindow(self):
        self.root.destroy()


#obj = admindashboard()
#
if __name__ == "__main__":
    obj = centerdashboard()