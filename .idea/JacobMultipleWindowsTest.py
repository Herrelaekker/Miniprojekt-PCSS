#CREDIT: https://stackoverflow.com/questions/16115378/tkinter-example-code-for-multiple-windows-why-wont-buttons-load-correctly
import tkinter as tk

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
        self.button1.grid(row=0,column=0)
        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo1(self.newWindow)

class Demo2:
    def __init__(self, master):
        self.master = master
        self.quitButton = tk.Button( text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.grid(row=0,column=0)

    def close_windows(self):
        self.master.destroy()

def main():
    root = tk.Tk()

    quitButton = tk.Button(text='Quit', width=25)
    quitButton.grid(row=0, column=0)

    top = tk.Toplevel(root)
    app = Demo1(top)
    app2 = Demo1(top)
    root.mainloop()

if __name__ == '__main__':
    main()