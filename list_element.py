from tkinter import *

class MyList(Frame):
    def __init__(self, master, func):
        super().__init__(master)
        self.func = func
        
        self.place(x=0, y=0, relwidth=1, relheight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_propagate(False)

        self.canvas = Canvas(self)
        self.canvas.grid(row=0, column=0, sticky="news")

        self.scroll_bar = Scrollbar(self, orient=VERTICAL, command = self.canvas.yview)
        self.scroll_bar.grid(row=0, column=1, sticky='ns')
        self.canvas.config(yscrollcommand = self.scroll_bar.set)
        
        self.internal_frame = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.internal_frame, anchor='nw')

        self.__build()
        self.internal_frame.update_idletasks()

        #self.config(width=300,height=300)
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def __build(self):
        self.func(self.internal_frame)

window = Tk()

def tra(a):
    for i in range(300): 
        frame = Frame(a, bg='purple', width=500)
        #Button(a, text="teste %i" % i, command= lambda *a: print(i)).pack()
                
my_list = MyList(window, tra)
window.geometry('700x500')
window.resizable(width=True,height=True)
window.maxsize(width=900, height=700)
window.minsize(width=500, height=400)
window.mainloop()