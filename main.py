import tkinter as tk

class MyCalculator:
    A = "0"
    B = "0"
    op = ""
    Dotpressed = False
    def Button1(self,event):
        self.A = self.A + "1"
        self.label_text.set(self.A)
        self.label.pack()
    def Buttonplus(self,event):
        self.op="+"
        self.B=self.A
        self.A=""
        self.label_text.set(self.A)
        self.label.pack()
    def Buttonsubtract(self,event):
        self.op="-"
        self.B=self.A
        self.A=""
        self.label_text.set(self.A)
        self.label.pack()
    def Buttonmultiply(self,event):
        self.op="×"
        self.B=self.A
        self.A=""
        self.label_text.set(self.A)
        self.label.pack()
    def Buttondivide(self,event):
        self.op="÷"
        self.B=self.A
        self.A=""
        self.label_text.set(self.A)
        self.label.pack()

    def Button2(self,event):
        self.A = self.A + "2"
        self.label_text.set(self.A)
        self.label.pack()

    def Button3(self,event):
        self.A = self.A + "3"
        self.label_text.set(self.A)
        self.label.pack()

    def Button4(self,event):
        self.A = self.A + "4"
        self.label_text.set(self.A)
        self.label.pack()

    def Button5(self,event):
        self.A = self.A + "5"
        self.label_text.set(self.A)
        self.label.pack()

    def Button6(self,event):
        self.A = self.A + "6"
        self.label_text.set(self.A)
        self.label.pack()

    def Button7(self,event):
        self.A = self.A + "7"
        self.label_text.set(self.A)
        self.label.pack()

    def Button8(self,event):
        self.A = self.A + "8"
        self.label_text.set(self.A)
        self.label.pack()

    def Button9(self,event):
        self.A = self.A + "9"
        self.label_text.set(self.A)
        self.label.pack()

    def Button0(self,event):
        if self.A == "0":
            return
        self.A = self.A + "0"
        self.label_text.set(self.A)
        self.label.pack()


    def ButtonDot(self,event):
        
        if self.Dotpressed == True:
            return
        self.Dotpressed = True
        self.A = self.A + "."
        self.label_text.set(self.A)
        self.label.pack()

    def Buttoninvert(self,event):
        self.A = str( -float(self.A))
        self.label_text.set(self.A)
        self.label.pack()
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("300x500")
        self.root.title("My Calculator")
        
        self.label_text = tk.StringVar()
        self.label_text.set(self.A)
        
        self.label = tk.Label(self.root, textvariable=self.label_text, font=('Arial', 18))
        self.label.pack()
        
        self.button = {}
        self.button = tk.Button(self.root, text="AC", height=4, width=8)
        self.button.place(x = 10, y = 90)
        self.button = tk.Button(self.root, text="+/-", height=4, width=8)
        self.button.bind('<Button-1>',self.Buttoninvert)
        self.button.place(x = 80, y = 90)
        self.button = tk.Button(self.root, text="%", height=4, width=8)
        self.button.place(x = 150, y = 90)
        self.button = tk.Button(self.root, text="÷", height=4, width=8)
        self.button.place(x = 220, y = 90)
        self.button = tk.Button(self.root, text="7", height=4, width=8)
        self.button.bind('<Button-1>',self.Button7)
        self.button.place(x = 10, y = 170)
        self.button = tk.Button(self.root, text="8", height=4, width=8)
        self.button.bind('<Button-1>',self.Button8)
        self.button.place(x = 80, y = 170)
        self.button = tk.Button(self.root, text="9", height=4, width=8)
        self.button.bind('<Button-1>',self.Button9)
        self.button.place(x = 150, y = 170)
        self.button = tk.Button(self.root, text="×", height=4, width=8)
        self.button.place(x = 220, y = 170)
        self.button = tk.Button(self.root, text="4", height=4, width=8)
        self.button.bind('<Button-1>',self.Button4)
        self.button.place(x = 10, y = 250)
        self.button = tk.Button(self.root, text="5", height=4, width=8)
        self.button.bind('<Button-1>',self.Button5)
        self.button.place(x = 80, y = 250)
        self.button = tk.Button(self.root, text="6", height=4, width=8)
        self.button.bind('<Button-1>',self.Button6)
        self.button.place(x = 150, y = 250)
        self.button = tk.Button(self.root, text="-", height=4, width=8)
        self.button.place(x = 220, y = 250)
        self.button = tk.Button(self.root, text="1", height=4, width=8)
        self.button.bind('<Button-1>',self.Button1)
        self.button.place(x = 10, y = 330)
        self.button.bind('<Button-1>',self.Button1)
        self.button = tk.Button(self.root, text="2", height=4, width=8)
        self.button.place(x = 80, y = 330)
        self.button.bind('<Button-1>',self.Button2)
        self.button = tk.Button(self.root, text="3", height=4, width=8)
        self.button.bind('<Button-1>',self.Button3)
        self.button.place(x = 150, y = 330)
        self.button = tk.Button(self.root, text="+", height=4, width=8)
        self.button.place(x = 220, y = 330)
        self.button = tk.Button(self.root, text="ENTER", height=4, width=8)
        self.button.place(x = 10, y = 410)
        self.button = tk.Button(self.root, text="0", height=4, width=8)
        self.button.bind('<Button-1>',self.Button0)
        self.button.place(x = 80, y = 410)
        self.button = tk.Button(self.root, text="=", height=4, width=8)
        self.button.place(x = 220, y = 410),
        self.button = tk.Button(self.root, text=".", height=4, width=8)
        self.button.place(x = 150, y = 410)
        
      
        self.button.bind('<Button-1>', self.ButtonDot)

        self.root.mainloop()
        
        #function
    def trigger_event(self,event):
        print(event)
        self.title = "Test"
        self.root.title(self.title)
        self.label_text.set("DIP 02")
        self.label.pack()
        
MyCalculator()
