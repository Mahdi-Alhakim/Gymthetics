from Src.acc_manager import AccountManager
from Src.user import User
from Src.schedule import Schedule
from Src.proto_features import Features

from tkinter import *


class App:
    def __init__(self, master):
        self.master = master
        self.master.resizable(0, 0)
        self.lock = Label(self.master, text="")
        self.lock.grid(row=2, column=1, sticky=E)

        self.setup()
        self.AccountManager.buildLogin()

    def setup(self):
        self.AccountManager = AccountManager(self, self.master)
        self.User = User(self, self.master)
        self.Schedule = Schedule(self, self.master)
        self.Features = Features(self.master)

    def clearWindow(self):
        for widget in self.master.winfo_children():
            widget.destroy()
