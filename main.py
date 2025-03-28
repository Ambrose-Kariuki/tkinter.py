import tkinter as tk

root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("500x500")
lable = tk.Label(root,text = "Hello world!",font=('arial', 18, 'bold'))
lable.pack(padx = 10, pady = 10)
text = tk.Text(root,height = 3, font=('arial', 16))
text.pack()

root.mainloop()
# This is a simple Tkinter application that creates a window with a title and a button.