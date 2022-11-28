from tkinter import *
from tkinter import ttk
from customtkinter import *
from PIL import ImageTk, Image

bg_color_line = 'yellow'
bg_color_button = 'purple'
bg_hover_color_button = 'black'
fg_color_line = 'blue'


class MyList(CTkFrame):
    
    def create(self, master, datas):
        super().__init__(master)
        self.datas = datas
        #Imagens
        self.img_edit = Image.open('icon-edit.png')
        self.img_edit = self.img_edit.resize((24, 24))
        self.img_edit = ImageTk.PhotoImage(self.img_edit)
        
        self.img_delete = Image.open('icon-delete.png')
        self.img_delete = self.img_delete.resize((24, 24))
        self.img_delete = ImageTk.PhotoImage(self.img_delete)
        
        self.img_descri = Image.open('icon-descri.png')
        self.img_descri = self.img_descri.resize((24, 24))
        self.img_descri = ImageTk.PhotoImage(self.img_descri)
        
        
        self.place(relx=0.015, rely=0.115, relwidth=0.97, relheight=0.8)
        self.grid_rowconfigure(0, weight=1)

        self.canvas = CTkCanvas(self)
        self.canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.scroll_bar = CTkScrollbar(self, orientation=VERTICAL, command = self.canvas.yview)
        self.scroll_bar.place(relx=.98, rely=0, relwidth=.02, relheight=1)
        self.canvas.config(yscrollcommand = self.scroll_bar.set)
        
        self.internal_frame = CTkFrame(self.canvas, fg_color='#000')
        self.canvas.create_window((0, 0), window=self.internal_frame, anchor='nw')
        
        self.__build()
        self.internal_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def __build(self):
        
        for data in self.datas:
            frame = Frame(self.internal_frame, bg=bg_color_line)
            frame.pack(fill = BOTH, expand = True)
            CTkLabel(frame, text=data[0], width=60, fg_color=bg_color_line, text_color=fg_color_line).pack(side=LEFT)
            
            if(len(data[1]) > 30):
                specie = data[1][:27] + "..."
            else:
                specie = data[1]
            CTkLabel(frame, text=specie.title(), fg_color=bg_color_line, text_color=fg_color_line, width=220).pack(side=LEFT)
            
            if(len(data[2]) > 15):
                order = data[2][:13] +"..."
            else:
                order = data[2]
            CTkLabel(frame, text=order, width=100, fg_color=bg_color_line, text_color=fg_color_line).pack(side=LEFT)
            
            if(len(data[3]) > 15):
                location = data[3][:13] +"..."
            else:
                location = data[3]
            CTkLabel(frame, text=location, width=100, fg_color=bg_color_line, text_color=fg_color_line).pack(side=LEFT)
            
            CTkLabel(frame, text=data[4], width=100, fg_color=bg_color_line, text_color=fg_color_line).pack(side=LEFT)
            
            self.new_button_edit(frame, data[0])
            self.new_button_excluir(frame, data[0])
            self.new_button_descricao(frame, data[0])
     
    def new_button_edit(self, master, id):
        return CTkButton(master, text='', image=self.img_edit, width=12, cursor='hand2',
                         fg_color=bg_color_button, hover_color=bg_hover_color_button,
                         command=lambda *a: self.edit_reg(id)).pack(side=LEFT)
    
    def new_button_excluir(self, master, id):
        return CTkButton(master, text='', image=self.img_delete, width=12, cursor='hand2',
                         fg_color=bg_color_button, hover_color=bg_hover_color_button,
                         command=lambda *a: self.excluirasdf(master, id)).pack(side=LEFT)
    
    def new_button_descricao(self, master, id):
        return CTkButton(master, text='', image=self.img_descri, width=12, cursor='hand2',
                         fg_color=bg_color_button, hover_color=bg_hover_color_button,
                         command=lambda *a: self.gerarRelatorioClientes(id)).pack(side=LEFT)
    
    def excluirasdf(self, master, id):
        master.destroy()
        self.deleta_cliente(id)
        
    def edit_reg(self, id):
        self.screen_edit(id)
        