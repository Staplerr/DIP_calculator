import tkinter as tk

class MyCalculator:
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("300x400")
        self.root.title("My Calculator")

        self.label = tk.Label(self.root, text="لا، أتوسل إليك.", font=('Arial', 18))
        self.label.pack()

        self.button = tk.Button(self.root, text="Click here", height=4)
        self.button.place(x = 10, y = 50)
        self.button = tk.Button(self.root, text="Click here", height=4)
        self.button.place(x = 80, y = 50)
        self.button = tk.Button(self.root, text="Click here", height=4)
        self.button.place(x = 150, y = 50)
        self.button = tk.Button(self.root, text="Click here", height=4)
        self.button.place(x = 220, y = 50)
        self.button = tk.Button(self.root, text="Click here", height=4)
        self.button.place(x = 10, y = 130)
        self.button = tk.Button(self.root, text="Click here", height=4)
        self.button.place(x = 80, y = 130)
        self.button = tk.Button(self.root, text="Click here", height=4)
        self.button.place(x = 150, y = 130)
        self.button = tk.Button(self.root, text="Click here", height=4)
        self.button.place(x = 220, y = 130)
        self.button = tk.Button(self.root, text="Click here", height=4)
        self.button.place(x = 10, y = 210)
        self.button = tk.Button(self.root, text="Click here", height=4)
        self.button.place(x = 80, y = 210)
        self.button = tk.Button(self.root, text="Click here", height=4)
        self.button.place(x = 150, y = 210)
        self.button = tk.Button(self.root, text="Click here", height=4)
        self.button.place(x = 220, y = 210)
        self.button = tk.Button(self.root, text="Click here", height=4, width=16)
        self.button.place(x = 10, y = 290)
        self.button = tk.Button(self.root, text="Click here", height=4)
        self.button.place(x = 220, y = 290)
        self.button = tk.Button(self.root, text="Click here", height=4)
        self.button.place(x = 150, y = 290)
        

        self.root.mainloop()

MyCalculator()
