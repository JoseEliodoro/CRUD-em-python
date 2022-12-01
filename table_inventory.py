from tkinter import *
from tkinter import ttk
from customtkinter import *
from PIL import ImageTk, Image

bg_color_line = '#d3d3d3'
bg_color_button_descricao = '#2c605f'
bg_color_button_delete = '#d36e6e'
bg_color_button_editar = '#5f8e9f'
bg_hover_color_button = '#008080'
fg_color_line = '#000'

# Classe para a tabela da janela de inventário
class TblInventory(CTkFrame):
    # Função para Criar o esbolço da tabela
    def create_invetory(self, master, datas):
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
        
        self.__build_inventory()
        self.internal_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    # Função que constroi os campos da tabela
    def __build_inventory(self):
        
        # for que criar uma linha para cada registro contido no banco
        for data in self.datas:
            
            frame = Frame(self.internal_frame, bg=bg_color_line)
            frame.pack(fill = BOTH, expand = True)
            CTkLabel(frame, text=data[0], width=60, fg_color=bg_color_line, text_color=fg_color_line).pack(side=LEFT)
            
            if(len(data[1]) > 30):
                specie = data[1][:27] + "..."
            else:
                specie = data[1]
            CTkLabel(frame, text=specie.title(), fg_color=bg_color_line, text_color=fg_color_line, width=300).pack(side=LEFT)
            
            if(len(data[2]) > 15):
                order = data[2][:13] +"..."
            else:
                order = data[2]
            CTkLabel(frame, text=order, width=115, fg_color=bg_color_line, text_color=fg_color_line).pack(side=LEFT)
            
            CTkLabel(frame, text=data[3], width=100, fg_color=bg_color_line, text_color=fg_color_line).pack(side=LEFT)
            
            self.new_button_edit_inventory(frame, data[0])
            self.new_button_excluir_inventory(frame, data[0])
            self.new_button_descricao_inventory(frame, data[0])
    
    # Função para criar novo botão de edição do registro
    def new_button_edit_inventory(self, master, id):
        return CTkButton(master, text='', image=self.img_edit, width=12, cursor='hand2',
                         fg_color=bg_color_button_editar, hover_color=bg_hover_color_button,
                         command=lambda *a: self.edit_register_inventory(id)).pack(side=LEFT)
        
    # Função para criar novo botão de excluir registro
    def new_button_excluir_inventory(self, master, id):
        return CTkButton(master, text='', image=self.img_delete, width=12, cursor='hand2',
                         fg_color=bg_color_button_delete, hover_color=bg_hover_color_button,
                         command=lambda *a: self.put_register_inventory(master, id)).pack(side=LEFT)
    
    # Função para criar novo botão de descrição do registro
    def new_button_descricao_inventory(self, master, id):
        return CTkButton(master, text='', image=self.img_descri, width=12, cursor='hand2',
                         fg_color=bg_color_button_descricao, hover_color=bg_hover_color_button,
                         command=lambda *a: self.relatorio('tbl_inventory', id)).pack(side=LEFT)
    
    def put_register_inventory(self, master, id):
        master.destroy()
        self.deleta_cliente('tbl_inventory', id)
        
    def edit_register_inventory(self, id):
        print(id)
        self.screen_edit_inventroy(id)
        