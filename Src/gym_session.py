from Prototype_Database.DB import tempDatabase, GymDatabase
from tkinter import *

class GymSession:
    def __init__(self, master, cnvs, user, interval, info, coords, Etag, mode=0):
        self.usr = user
        self.intrvl = interval
        self.info = self.analyzeInfo(info)
        self.master, self.cnvs, self.coords, self.Etag, self.mode = master, cnvs, coords, Etag, mode
        self.Workoutcolors = {"Supervision": "orange", "Full Body": "blue", "Upper Body": "orange",
                              "Lower Body": "dark green", "Cardio": "red"}
        self.days = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
        self.daysI = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}

        self.draw()

    def analyzeInfo(self, info):
        return info.split(",")

    def draw(self):
        day, o, c = self.intrvl
        TI = "{}:{} - {}:{}".format(o // 1, ("30" if (o * 2) % 2 else "00"), c // 1, ("30" if (c * 2) % 2 else "00"))
        txt = """{}\n{}\n{}""".format(tempDatabase[self.usr][3], TI, self.info[0])
        r, c = (self.coords[0] + self.coords[2]) // 2, (self.coords[1] + self.coords[3]) // 2
        self.txtObj = self.cnvs.create_text(r, c, text=txt, font=("Persia", 9), fill="white", justify=CENTER)
        self.cnvs.itemconfig(self.Etag, fill=self.Workoutcolors[self.info[0]])
        if self.info[0] != "Supervision":
            if self.mode == 0:
                self.cnvs.tag_bind(self.Etag, "<Button-1>", lambda e: self.viewInfo(txt, TI, e))
                self.cnvs.tag_bind(self.txtObj, "<Button-1>", lambda e: self.viewInfo(txt, TI, e))
            elif self.mode == 2:
                self.cnvs.tag_bind(self.Etag, "<Button-1>", self.Select)
                self.cnvs.tag_bind(self.txtObj, "<Button-1>", self.Select)
            else:
                self.cnvs.tag_bind(self.Etag, "<Button-2>", lambda e: self.editSession(txt, TI, e))
                self.cnvs.tag_bind(self.txtObj, "<Button-2>", lambda e: self.editSession(txt, TI, e))

    def Select(self, e):
        self.cnvs.delete("all")
        self.cnvs.destroy()
        frm = Frame(self.cnvs.master);
        frm.place(relx=0.5, rely=0.5, anchor=CENTER)
        Label(frm, text="Request Virtual Meeting?", font=("System", 40)).grid(row=0, column=0, columnspan=2, sticky=S)

        def yes():
            frm.destroy()
            Label(self.cnvs.master, text="Your request has been sent succcessfully!\nPlease await approval..",
                  font="Arial 24", fg="brown", justify=CENTER).place(relx=0.5, rely=0.5, anchor=CENTER)

        def no(): self.cnvs.master.destroy()

        Button(frm, text="Yes", font=("Times", 30), command=yes).grid(row=1, column=0, padx=6, pady=6, sticky=NE)
        Button(frm, text="No", font=("Times", 30), command=no).grid(row=1, column=1, padx=6, pady=6, sticky=NW)

    def editSession(self, txt, TI, e):
        print(e.x, e.y)
        newLvl = Toplevel(self.master);
        newLvl.title("{}  {}".format(tempDatabase[self.usr][3], TI))
        newLvl.resizable = False;
        newLvl.grab_set()
        tv1, tv2, dropdown, workout = StringVar(), StringVar(), StringVar(), StringVar();
        tv1.set(self.intrvl[1]);
        tv2.set(self.intrvl[2]);
        dropdown.set(self.days[self.intrvl[0]]);
        workout.set(self.info[0])
        OptionMenu(newLvl, dropdown, *[self.days[i] for i in range(7)]).grid(row=1, column=1, sticky=E + W)
        OptionMenu(newLvl, workout, "Full Body", "Upper Body", "Lower Body", "Cardio").grid(row=3, column=1,
                                                                                            sticky=E + W)

        print(self.intrvl)
        frm = Frame(newLvl);
        frm.grid(row=2, column=1, sticky=E + W);
        Entry(frm, textvariable=tv1, width=4).pack(side=LEFT);
        Label(frm, text=" --> ").pack(side=LEFT, anchor=E);
        Entry(frm, textvariable=tv2, width=4).pack(side=RIGHT)
        Label(newLvl, text=tempDatabase[self.usr][3], fg=self.Workoutcolors[self.info[0]], font="Times 16").grid(row=0,
                                                                                                                 column=1,
                                                                                                                 sticky=N + E + W)

        def update():
            w_step = self.coords[2] - self.coords[0]
            h_step = (self.coords[3] - self.coords[1]) / (self.intrvl[2] - self.intrvl[1]) / 2
            Tstart = self.intrvl[1] - 0.5 * (self.coords[1] - 55) / h_step
            timestep = self.coords[0] % w_step
            T1, T2 = float(tv1.get()), float(tv2.get())
            print("Update:", Tstart, "---", T1, T2)
            self.cnvs.delete(self.Etag)
            self.cnvs.delete(self.txtObj)
            self.Etag = self.cnvs.create_rectangle(timestep + w_step * self.daysI[dropdown.get()],
                                                   55 + 2 * (T1 - Tstart) * h_step,
                                                   timestep + w_step * (1 + self.daysI[dropdown.get()]),
                                                   55 + 2 * (T2 - Tstart) * h_step,
                                                   fill=self.Workoutcolors[workout.get()])
            day, o, c = self.daysI[dropdown.get()], T1, T2

            TI = "{}:{} - {}:{}".format(int(o // 1), ("30" if (o * 2) % 2 else "00"), int(c // 1),
                                        ("30" if (c * 2) % 2 else "00"))
            txt = """{}\n{}\n{}""".format(tempDatabase[self.usr][3], TI, workout.get())
            self.txtObj = self.cnvs.create_text(timestep + w_step * (self.daysI[dropdown.get()] + 0.5),
                                                55 + h_step * (T1 + T2 - 2 * Tstart), text=txt, font=("Persia", 9),
                                                fill="white", justify=CENTER)

            self.cnvs.tag_bind(self.Etag, "<Button-2>", lambda e: self.editSession(txt, TI, e))
            self.cnvs.tag_bind(self.txtObj, "<Button-2>", lambda e: self.editSession(txt, TI, e))
            self.info[0] = workout.get()
            self.intrvl = (self.daysI[dropdown.get()], T1, T2)
            self.coords = (timestep + w_step * self.daysI[dropdown.get()], 55 + 2 * (T1 - Tstart) * h_step,
                           timestep + w_step * (1 + self.daysI[dropdown.get()]), 55 + 2 * (T2 - Tstart) * h_step)
            newLvl.destroy()

        Button(newLvl, text="Update", command=update).grid(row=4, column=1, sticky=E + W)

    def viewInfo(self, txt, TI, e):
        newLvl = Toplevel(self.master);
        newLvl.title("{}  {}".format(tempDatabase[self.usr][3], TI))
        newLvl.geometry("300x300");
        newLvl.grab_set()
        Label(newLvl, text=txt, fg=self.Workoutcolors[self.info[0]], font="Times 16").pack()
        Label(newLvl, text="\nAvailable in {}:".format(tempDatabase[self.usr][3])).pack()

        dct = GymDatabase[tempDatabase[self.usr][3]][5]
        itms = dct[self.info[0]] if self.info[0] != "Full Body" else (
                    dct["Cardio"] + dct["Upper Body"] + dct["Lower Body"])
        l = Listbox(newLvl);
        l.pack();
        l.insert(END, *itms)