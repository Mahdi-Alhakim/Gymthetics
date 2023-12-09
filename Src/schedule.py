from Prototype_Database.DB import tempDatabase, GymDatabase
from Src.gym_session import GymSession

from tkinter import *

class Schedule:
    def __init__(self, app, master):
        self.app = app
        self.master = master

    def setupSchedule(self, cnvs, u, mode=0):
        cnvs.delete("all")
        w, h = int(cnvs["width"]), int(cnvs["height"])
        timestep = (w - 10) // 11 + 5
        w_step = (w - timestep - 5) // 7
        cnvs.create_rectangle(5, 5, w - 5, h - 5, fill="white")
        cnvs.create_line(timestep, 15, timestep, h - 15)
        days = {0: "MON", 1: "TUE", 2: "WED", 3: "THUR", 4: "FRI", 5: "SAT", 6: "SUN"}
        for i in range(1, 7):
            cnvs.create_line(timestep + i * w_step, 15, timestep + i * w_step, h - 15, width=1)
        for i in range(0, 7):
            cnvs.create_text(timestep + (i + 0.5) * w_step, 35, text=days[i], fill="dark green")

        GYM = tempDatabase[u][3]
        o, c = min(GymDatabase[GYM][1], key=lambda x: x[0])[0], max(GymDatabase[GYM][1], key=lambda x: x[1])[1]
        Tsteps = 2 * (c - o);
        h_step = round((h - 55) / Tsteps)
        cnvs.create_line(15, 55, w - 15, 55, width=1.5)
        for i in range(Tsteps):
            cnvs.create_line(15, 55 + i * h_step, w - 15, 55 + i * h_step)
            cnvs.create_text((timestep - 5) // 2 + 10, 63 + i * h_step,
                             text="{}:{}".format(o + (i // 2), ("30" if i % 2 else "00")), fill="dark blue",
                             font=("Times", 10))
        sessions = []
        for i in tempDatabase[u][2]:
            print(i)
            Etag = cnvs.create_rectangle(timestep + i[0] * w_step, 55 + 2 * (i[1] - o) * h_step,
                                         timestep + (i[0] + 1) * w_step, 55 + 2 * (i[2] - o) * h_step)
            sessions += [GymSession(self.master, cnvs, u, i[0:3], i[3], (
                timestep + i[0] * w_step, 55 + 2 * (i[1] - o) * h_step, timestep + (i[0] + 1) * w_step,
                55 + 2 * (i[2] - o) * h_step), Etag, mode)]
        for i in GymDatabase[tempDatabase[u][3]][3]:
            print(i, " <GYM")
            cnvs.create_rectangle(timestep + i[0] * w_step, 55 + 2 * (i[1] - o) * h_step,
                                  timestep + (i[0] + 1) * w_step, 55 + 2 * (i[2] - o) * h_step, fill="gray")
            cnvs.create_text(timestep + (i[0] + 0.5) * w_step, 55 + (i[1] + i[2] - 2 * o) * h_step,
                             text="Closed/\nUnavailable", justify=CENTER, font=("System Bold", 11), fill="white")
        return sessions

    def requestSchUpdate(self, t):
        for i in t.winfo_children():
            i.destroy()
        Label(t, text="Your request has been sent succcessfully!\nPlease await your Gym's Approval..",
              font="Arial 24",
              fg="brown").grid(row=0, column=0, sticky=N + W + S + E)