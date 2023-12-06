import tkinter as tk

class MyCalculator:
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("300x500")
        self.root.title("My Calculator")

        self.label = tk.Label(self.root, text="لا، أتوسل إليك.", font=('Arial', 18))
        self.label.pack()
        
        self.button = {}
        self.button = tk.Button(self.root, text="AC", height=4, width=8)
        self.button.place(x = 10, y = 90)
        self.button = tk.Button(self.root, text="+/-", height=4, width=8)
        self.button.place(x = 80, y = 90)
        self.button = tk.Button(self.root, text="%", height=4, width=8)
        self.button.place(x = 150, y = 90)
        self.button = tk.Button(self.root, text="÷", height=4, width=8)
        self.button.place(x = 220, y = 90)
        self.button = tk.Button(self.root, text="7", height=4, width=8)
        self.button.place(x = 10, y = 170)
        self.button = tk.Button(self.root, text="8", height=4, width=8)
        self.button.place(x = 80, y = 170)
        self.button = tk.Button(self.root, text="9", height=4, width=8)
        self.button.place(x = 150, y = 170)
        self.button = tk.Button(self.root, text="×", height=4, width=8)
        self.button.place(x = 220, y = 170)
        self.button = tk.Button(self.root, text="4", height=4, width=8)
        self.button.place(x = 10, y = 250)
        self.button = tk.Button(self.root, text="5", height=4, width=8)
        self.button.place(x = 80, y = 250)
        self.button = tk.Button(self.root, text="6", height=4, width=8)
        self.button.place(x = 150, y = 250)
        self.button = tk.Button(self.root, text="-", height=4, width=8)
        self.button.place(x = 220, y = 250)
        self.button = tk.Button(self.root, text="1", height=4, width=8)
        self.button.place(x = 10, y = 330)
        self.button = tk.Button(self.root, text="2", height=4, width=8)
        self.button.place(x = 80, y = 330)
        self.button = tk.Button(self.root, text="3", height=4, width=8)
        self.button.place(x = 150, y = 330)
        self.button = tk.Button(self.root, text="+", height=4, width=8)
        self.button.place(x = 220, y = 330)
        self.button = tk.Button(self.root, text="0", height=4, width=18)
        self.button.place(x = 10, y = 410)
        self.button = tk.Button(self.root, text="=", height=4, width=8)
        self.button.place(x = 220, y = 410),
        self.button = tk.Button(self.root, text=".", height=4, width=8)
        self.button.place(x = 150, y = 410)
        

        self.root.mainloop()

MyCalculator()
