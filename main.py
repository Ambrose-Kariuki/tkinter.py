import tkinter as tk

root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("500x500")
lable = tk.Label(root,text = "Hello world!",font=('arial', 18, 'bold'))
lable.pack(padx = 10, pady = 10)
text = tk.Text(root,height = 3, font=('arial', 16))
text.pack()
button  = tk.Button(root,text = "click me",font =('arial',18,'bold'),bg = 'blue',fg = 'white')
button.pack()
buttonframe = tk.Button(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
btn1 = tk.Button(buttonframe, text="Button 1", font=('arial', 18,))
btn1.grid(row=0, column=0,sticky="ew")
btn2 = tk.Button(buttonframe, text="Button 2", font=('arial', 18,))
btn2.grid(row=0, column=1,sticky="ew")
btn3 = tk.Button(buttonframe, text="Button 3", font=('arial', 18,)) 
btn3.grid(row=0, column=2,sticky="ew")
buttonframe.pack(pady = 10)
buttonframe = tk.Frame(root)                 
root.mainloop()
# This is a simple Tkinter application that creates a window with a title and a button.