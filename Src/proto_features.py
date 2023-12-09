from tkinter import *

class Features:
    def __init__(self, master):
        self.master = master

    def membershipOffers(self, win):
        c = Canvas(win, width=400, height=300, bg="gold")
        c.grid(row=1, column=1, sticky=N + W + S + E)
        c.create_text(200, 40, text="GYMTHETICS MEMBERSHIP", justify=CENTER, font=("System", 27), fill="dark blue")
        c.create_rectangle(20, 80, 116, 180, outline="Black", width=2, fill="light blue")
        c.create_text(68, 130, text="PLAN 1")
        c.create_rectangle(151, 80, 247, 180, outline="Black", width=2, fill="light blue")
        c.create_text(199, 130, text="PLAN 2")
        c.create_rectangle(282, 80, 378, 180, outline="Black", width=2, fill="light blue")
        c.create_text(330, 130, text="PLAN 3")
        c.create_text(200, 240,
                      text="Receive Your Membership Today!\nGain access to multiple exclusive features and services\nthat will pave your way to outstanding results!",
                      justify=CENTER, font=("Times Bold", 13))

    def QR(self, e):
        t = Toplevel(self.master)
        t.geometry("200x230")
        t.grab_set()
        t.grid_rowconfigure(0, weight=1)
        t.grid_columnconfigure(0, weight=1)
        c = Canvas(t, width=200, height=200)
        c.grid(row=0, column=0, sticky=N + S + W + E)
        c.create_rectangle(55, 55, 145, 145, dash=(30, 30))
        c.create_text(100, 100, text="QR", font=("System", 40))
        Label(t, text="(Scan the QR_codes of used)\n(machines to record activity)", font=("Arial Bold", 13),
              fg="red").grid(row=1, column=0, sticky=W + E)

    def dealWithStat(self, usr, cnv):
        cnv.create_line(10, 10, 10, 195, width=2)
        cnv.create_line(10, 195, 190, 195, width=2)
        cnv.create_line(10, 195, 60, 100, fill="red")
        cnv.create_oval(58, 98, 62, 102, fill="red")
        cnv.create_line(60, 100, 100, 130, fill="red")
        cnv.create_oval(98, 128, 102, 132, fill="red")
        cnv.create_line(100, 130, 190, 70, fill="red")
        cnv.create_oval(188, 68, 192, 72, fill="red")

        cnv.create_line(10, 195, 85, 140, fill="blue")
        cnv.create_oval(83, 138, 87, 142, fill="blue")
        cnv.create_line(85, 140, 130, 160, fill="blue")
        cnv.create_oval(128, 158, 132, 162, fill="blue")
        cnv.create_line(130, 160, 190, 80, fill="blue")
        cnv.create_oval(188, 78, 192, 82, fill="blue")
        cnv.create_text(85, 50, text="Activity / Time")
        cnv.bind()

    def TnS(self, e):
        n = Toplevel(self.master)
        n.title("Terms and Services")
        n.grab_set()
        Label(n, text="Terms and Services\n\n" + "".join(
            ["......................................................................................................\n"
             for i in range(12)])).pack()