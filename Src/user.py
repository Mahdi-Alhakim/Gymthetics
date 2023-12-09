from Prototype_Database.DB import tempDatabase, ExerciseQuotes

from tkinter import *
import random

class User:
    def __init__(self, app, master):
        self.App = app
        self.master = master

    def clientManage(self, usr):
        t = Toplevel(self.master)
        t.geometry("750x500")
        t.grab_set()
        t.title("Manage Schedule")
        t.resizable = False
        t.grid_rowconfigure(0, weight=1)
        t.grid_columnconfigure(0, weight=1)
        cv = Canvas(t, width=533, height=446)
        cv.grid(row=0, column=0)
        self.App.Schedule.setupSchedule(cv, usr, 1)
        Button(t, text="Request", command=lambda: self.App.Schedule.requestSchUpdate(t)).grid(row=1, column=0, columnspan=2,
                                                                                 sticky=E + W + S + N)

    def clientVrequest(self, usr):
        t = Toplevel(self.master)
        t.grab_set()
        if not tempDatabase[usr][4]:
            t.geometry("406x306")
            t.title("Membership")
            self.App.Features.membershipOffers(t)
        else:
            t.title("Request Virtual Call")
            t.geometry("550x470")
            c = Canvas(t, width=533, height=446, bg="light gray", highlightthickness=1, highlightbackground="black");
            c.pack()
            self.App.Schedule.setupSchedule(c, usr, 2)

    def userInputSection(self, frm, u):
        Label(frm, text="User Status:  {}{}".format(tempDatabase[u][1],
                                                    ("" if not (tempDatabase[u][4]) else "(Membership)")), ).pack()
        status = tempDatabase[u][1]
        print(status)
        btn1 = None
        if status == "Admin":
            btn1 = Button(frm, text="View Users").pack()
            Label(frm, text="temp").pack()
        elif status == "Client":
            Button(frm, text="Manage Schedule", command=lambda: self.clientManage(u)).pack()
            Button(frm, text="Request Virtual Session", command=lambda: self.clientVrequest(u)).pack()
            Label(frm, text="Add Activity \(Click Below)/", font=("System", 14), fg="dark blue").pack()
        elif status == "GYM":
            Button(frm, text="View Clients & Coaches").pack()
            Button(frm, text="Requests Received").pack()
            Button(frm, text="Update Schedule").pack()
            Button(frm, text="Finance").pack()
        elif status == "Coach":
            Button(frm, text="Manage Schedule").pack()
            Button(frm, text="View Available Virtual Requests").pack()
            Button(frm, text="Finance").pack()

    def buildUser(self, u):
        self.App.clearWindow()
        self.master.geometry("800x540")
        self.master.title("Gymthetics")

        secondaryFrame = Frame(self.master)
        secondaryFrame.grid(row=0, column=0, sticky=W + E)
        secondaryFrame.grid_rowconfigure(0, weight=1)
        secondaryFrame.grid_columnconfigure(0, weight=1)
        titleFrame = Frame(secondaryFrame)
        titleFrame.grid(row=0, column=0)
        Label(titleFrame, text="GYMTHETICS", font="Times 20").pack(side=TOP);
        Label(titleFrame, text="Personalized * Effective * Need-based").pack(side=TOP)
        buttonFrame = Frame(secondaryFrame)
        buttonFrame.grid(row=0, column=2, sticky=E)
        btn1 = Button(buttonFrame, text="Account", font="Times 20", command=lambda: self.App.AccountManager.viewAccount(u));
        btn1.pack(side=TOP)
        btn1["bg"] = "blue"
        btn2 = Button(buttonFrame, text="Sign Out", font="Times 15", command=self.App.AccountManager.signOut);
        btn2.pack(side=TOP)
        btn2["bg"] = "blue"

        self.App.mainFrame = Frame(self.master, width=800, height=630)
        self.App.mainFrame.grid(row=1, column=0, sticky=W + E + N + S)
        self.App.cnvs = Canvas(self.App.mainFrame, width=533, height=446, bg="light gray", highlightthickness=1,
                           highlightbackground="black")
        self.App.cnvs.grid(row=0, column=0, sticky=NW)
        Canvas(self.App.mainFrame, width=255, height=5).grid(row=1, column=1, sticky=SE)
        Label(self.master, text="(C) Copyright", font="Times 14", fg="blue").grid(row=2, column=0, sticky=SW)
        self.App.Schedule.setupSchedule(self.App.cnvs, u)

        statFrame = Frame(self.App.mainFrame)
        statFrame.grid(row=0, column=1, sticky=N + S + W + E)
        statFrame.grid_rowconfigure(0, weight=1)
        statFrame.grid_columnconfigure(0, weight=1)
        Frame1 = Frame(statFrame)
        Frame1.grid(row=0, column=0)
        Frame1.grid_rowconfigure(0, weight=1)
        Frame1.grid_columnconfigure(0, weight=1)
        self.App.User.userInputSection(Frame1, u)

        newCanv = Canvas(statFrame, width=200, height=200, bg="light blue", highlightthickness=2,
                         highlightbackground="light gray")
        newCanv.grid(row=1, column=0, pady=1, sticky=N)
        self.App.Features.dealWithStat(u, newCanv)
        newCanv.bind("<Button-1>", self.App.Features.QR)

        c = Canvas(statFrame, width=200, height=60, bg="light gray", highlightthickness=2, highlightbackground="black");
        c.grid(row=2, column=0, pady=1)
        c.create_line(0, 0, 200, 60, dash=(4, 4))
        c.create_line(0, 60, 200, 0, dash=(4, 4))
        c.create_oval(50, 15, 150, 45, fill="light gray", outline="light gray")
        c.create_text(100, 30, text="Advertisement", font=("Persia", 12), fill="red")

        quote = Canvas(statFrame, width=200, height=40, bg="black", highlightthickness=2,
                       highlightbackground="light gray")
        quote.grid(row=4, column=0, sticky=N, pady=1)
        quote.create_text(100, 20, text='"' + random.choice(ExerciseQuotes) + '"', font=("Arial Rounded MT Bold", 9),
                          fill="white", justify=CENTER)