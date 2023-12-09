from Prototype_Database.DB import tempDatabase

from tkinter import *
import tkinter.messagebox as mb

class AccountManager:
    def __init__(self, app, master):
        self.App = app
        self.master = master

    def signOut(self):
        self.buildLogin()

    def AttemptLogin(self):
        usr, pswrd = self.userVar.get(), self.passVar.get()
        find = tempDatabase.get(usr, -1)
        if find == -1:
            mb.showinfo("Fail", "Incorrect Username or Password!")
        elif pswrd == find[0]:
            self.App.User.buildUser(usr); print("Login")
        else:
            mb.showinfo("Fail", "Incorrect Username or Password!")

    def buildLogin(self):
        self.App.clearWindow()
        self.master.geometry("400x250")
        self.master.title("Login")
        self.lb = Label(self.master, text="GYMTHETICS", font="Times 40")
        self.lb.pack()
        Label(self.master, text="Username: ").pack()
        self.userVar = StringVar()
        self.tx = Entry(self.master, textvariable=self.userVar)
        self.tx.pack()
        Label(self.master, text="Password: ").pack()
        self.passVar = StringVar()
        self.tx = Entry(self.master, textvariable=self.passVar, show="*")
        self.tx.pack()
        self.btn = Button(self.master, text="Login", command=self.AttemptLogin)
        self.btn.pack()
        Label(self.master, text="OR").pack()
        self.btn2 = Button(self.master, text="Register", command=lambda x: x)
        self.btn2.pack()

    def viewAccount(self, u):
        print("viewing: ", u)
        newLvl = Toplevel(self.master)
        newLvl.title("Account Info.")
        newLvl.geometry("300x210")
        newLvl.grab_set()
        Label(newLvl, text="Account", font="Times 25", fg="dark green").pack()
        Label(newLvl, text="User: {}".format(u), font=("Times", 18), fg="dark green").pack()
        sttngs = Button(newLvl, text="..Privacy/Security..", font=("Times", 14))
        sttngs.pack()
        gyminf = Button(newLvl, text="..Gym Info..", font=("Times", 14))
        gyminf.pack()
        pymnt = Button(newLvl, text="..Payment..", font=("Times", 14))
        pymnt.pack()
        cntct = Button(newLvl, text="..Contact..", font=("Times", 14))
        cntct.pack()
        l = Label(newLvl, text="Terms and Services", font=("Times Italic", 14), fg="blue")
        l.pack()
        l.bind("<Button-1>", self.App.Features.TnS)

        def ent(e): l["fg"] = "red"

        def lev(e): l["fg"] = "blue"

        l.bind("<Enter>", ent)
        l.bind("<Leave>", lev)