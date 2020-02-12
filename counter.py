from tkinter import *


class Window(Frame):
    def __init__(self, master):
        super(Window, self).__init__(master)
        self.grid()
        self.create_all()

    def create_all(self):

        self.main_txt = Entry(self, width=15)
        self.main_txt.grid(row=0, column=0, columnspan=3, sticky=N)

        self.del_btt = Button(self, text="    DEL    ", command=lambda: self.main_txt.delete(0, END))
        self.del_btt.grid(row=3, column=5, sticky=N)

        self.plus_btt = Button(self, text="  +  ", command=lambda: self.main_txt.insert(END, "+"))
        self.plus_btt.grid(row=4, column=5, sticky=W)

        self.min_btt = Button(self, text="  -  ", command=lambda: self.main_txt.insert(END, "-"))
        self.min_btt.grid(row=5, column=5, sticky=W)

        self.ym_btt = Button(self, text="  *  ", command=lambda: self.main_txt.insert(END, "*"))
        self.ym_btt.grid(row=4, column=5, sticky=E)

        self.dele_btt = Button(self, text="  /  ", command=lambda: self.main_txt.insert(END, "/"))
        self.dele_btt.grid(row=5, column=5, sticky=E)

        self.rav_btt = Button(self, text="   ==   ", command=self.rav_btt_click)
        self.rav_btt.grid(row=6, column=5, sticky=S)

        self.btt1 = Button(self, text="    1    ", command=lambda: self.main_txt.insert(END, "1"))
        self.btt1.grid(row=3, column=0, sticky=S)

        self.btt2 = Button(self, text="    2    ", command=lambda: self.main_txt.insert(END, "2"))
        self.btt2.grid(row=3, column=1, sticky=S)

        self.btt3 = Button(self, text="    3    ", command=lambda: self.main_txt.insert(END, "3"))
        self.btt3.grid(row=3, column=2, sticky=S)

        self.btt4 = Button(self, text="    4    ", command=lambda: self.main_txt.insert(END, "4"))
        self.btt4.grid(row=4, column=0, sticky=S)

        self.btt5 = Button(self, text="    5    ", command=lambda: self.main_txt.insert(END, "5"))
        self.btt5.grid(row=4, column=1, sticky=S)

        self.btt6 = Button(self, text="    6    ", command=lambda: self.main_txt.insert(END, "6"))
        self.btt6.grid(row=4, column=2, sticky=S)

        self.btt7 = Button(self, text="    7    ", command=lambda: self.main_txt.insert(END, "7"))
        self.btt7.grid(row=5, column=0, sticky=S)

        self.btt8 = Button(self, text="    8    ", command=lambda: self.main_txt.insert(END, "8"))
        self.btt8.grid(row=5, column=1, sticky=S)

        self.btt9 = Button(self, text="    9    ", command=lambda: self.main_txt.insert(END, "9"))
        self.btt9.grid(row=5, column=2, sticky=S)

        self.btt0 = Button(self, text="    0    ", command=lambda: self.main_txt.insert(END, "0"))
        self.btt0.grid(row=6, column=1, sticky=S)

    def rav_btt_click(self):

        num = 0
        commands = [
            self.main_txt.get().split(sep="+"),
            self.main_txt.get().split(sep="-"),
            self.main_txt.get().split(sep="/"),
            self.main_txt.get().split(sep="*")]

        for i in range(len(commands)):

            if len(commands[i]) <= 1:
                continue
            else:
                if i == 0:
                    for el in commands[0]:
                        num += int(el)
                elif i == 1:
                    for el in commands[1]:
                        num -= int(el)
                elif i == 2:
                    num = int(commands[2][0])
                    for el in commands[2]:
                        num /= int(el)
                    num *= int(commands[2][0])
                elif i == 3:
                    num = int(commands[3][0])
                    for el in commands[3]:
                        num *= int(el)
                    num /= int(commands[3][0])

        self.main_txt.delete(0, END)
        self.main_txt.insert(0, "=" + str(num))


root = Tk()
root.geometry("190x130")
root.title("Калькуляптор")

window = Window(root)
root.mainloop()
