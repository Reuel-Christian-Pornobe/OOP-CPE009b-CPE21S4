from tkinter import*

class MyWindow:
    def __init__(self, win):
        #common widgets
        win.configure(bg = "pink")

        #Title
        self.Label1 = Label(win, text="Calculator", fg="white", bg="pink", font=("Times New Roman", 24, "bold"))
        self.Label1.place(x=120,y=50)

        #Number 1 text and Entry box
        self.Label2 = Label(win, text="Number 1:", fg="White", bg = "pink", font=("Times New Roman", 12, "bold"))
        self.Label2.place(x=80, y=120)
        self.Entry1 = Entry(win, bd = 2)
        self.Entry1.place(x = 220, y = 120)

        # Number 2 text and Entry box
        self.Label2 = Label(win, text="Number 2:", fg="White", bg = "pink", font=("Times New Roman", 12, "bold"))
        self.Label2.place(x=80, y=140)
        self.Entry2 = Entry(win, bd=2)
        self.Entry2.place(x=220, y=140)

        # Results text and Entry box
        self.Label3 = Label(win, text="Results:", fg="White", bg = "pink", font=("Times New Roman", 12, "bold"))
        self.Label3.place(x=80, y=180)
        self.Entry3 = Entry(win, bd=2)
        self.Entry3.place(x=220, y=180)

        #Buttons for operations
        #Add button
        self.Button1 = Button(win, text="Add", width = 4, height = 1)
        self.Button1.place(x=100, y=220)
        self.Button1.bind('<Button-1>', self.add)

        # Subtract button
        self.Button2 = Button(win, text="Sub", width=4, height=1)
        self.Button2.place(x=160, y=220)
        self.Button2.bind('<Button-1>', self.sub)

        # Multiply button
        self.Button3 = Button(win, text="Multi", width=4, height=1)
        self.Button3.place(x=220, y=220)
        self.Button3.bind('<Button-1>', self.multi)

        #Divide button
        self.Button4 = Button(win, text="Div", width=4, height=1)
        self.Button4.place(x=280, y=220)
        self.Button4.bind('<Button-1>', self.div)

    def add(self,win):
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 + num2
        self.Entry3.insert(0, str(result))

    def sub(self,win):
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 - num2
        self.Entry3.insert(0, str(result))


    def multi(self,win):
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 * num2
        self.Entry3.insert(0, str(result))

    def div(self,win):
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 / num2
        self.Entry3.insert(0, str(result))

window = Tk()
MyWin=MyWindow(window)
window.geometry("400x300+10+10")
window.title("Standard Calculator")
window.mainloop()