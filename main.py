from tkinter import *
from tkinter import ttk
from customtkinter import *
from func_banco import Funcs
from tkcalendar import DateEntry

from PIL import Image, ImageTk

color0 = '#000'
color1 = '#fff'
color2 = '#111'
color3 = '#cecece'
color_text_toplevel = 'purple'
color_bg_toplevel = 'yellow'
color_bg_entry_toplevel = 'blue'
color_border_entry_top = 'white'
color_text_button_toplevel = 'pink'
color_bg_button_toplevel = 'red'
color_border_button_toplevel = 'green'
color_hover_button_toplevel = 'black'

class Aplication(Funcs):
    def __init__(self, janela):
        self.janela = janela
        #self.imagens_base64()
        self.tela()
        self.frames_da_tela()
        self.widgets_frame_menu()
        self.init_pg_inicial()
        self.frame = self.frame_pg_inicial
        #self.screen_add()
        #self.Menus()
        self.janela.mainloop()
    
        
    def screen_add(self):
        self.window = CTkToplevel(self.janela)
        self.window.title('clear')
        self.window.geometry('270x450')
        self.window.maxsize(width=300, height=500)
        self.window.minsize(width=270, height=400)
        self.window.config(background=color_bg_toplevel)


        self.img = Image.open('logo2.png')
        self.img = ImageTk.PhotoImage(self.img)
        self.lb_img = CTkLabel(self.window, image=self.img)
        self.lb_img.place(relx=.15, rely=0.1)

        self.specie_entry = CTkEntry(self.window, placeholder_text='Espécie',  text_color=color_text_toplevel,
                                        fg_color=color_bg_entry_toplevel, border_color=color_border_entry_top,
                                        text_font='Arial 15')
        self.specie_entry.place(relx=0.05, rely=0.4, relwidth=0.9)


        self.order_entry = CTkEntry(self.window, placeholder_text='Order',  text_color=color_text_toplevel,
                                        fg_color=color_bg_entry_toplevel, border_color=color_border_entry_top,
                                        text_font='Arial 15')
        self.order_entry.place(relx=0.05, rely=0.5, relwidth=0.9)


        self.location_entry = CTkEntry(self.window, placeholder_text='Local da coleta', text_color=color_text_toplevel,
                                        fg_color=color_bg_entry_toplevel, border_color=color_border_entry_top,
                                        text_font='Arial 15')
        self.location_entry.place(relx=0.05, rely=0.6, relwidth=0.9)
        
        self.date_entry = DateEntry(self.window, font='Arial 15')
        self.date_entry.place(relx=0.05, rely=0.7, relwidth=0.9)

        self.btn_add = CTkButton(self.window, text='Salvar', text_font='Arial 15', cursor='hand2',
                            text_color=color_text_button_toplevel, fg_color=color_bg_button_toplevel,
                            border_color=color_border_button_toplevel, hover_color=color_hover_button_toplevel,
                            command=self.add_cliente)
        self.btn_add.place(relx=0.05, rely=0.85, relwidth=0.45, height=35)

        self.btn_clear = CTkButton(self.window, text='Limpar', text_font='Arial 15', cursor='hand2',
                            text_color=color_text_button_toplevel, fg_color=color_bg_button_toplevel,
                            border_color=color_border_button_toplevel, hover_color=color_hover_button_toplevel)
        self.btn_clear.place(relx=0.5, rely=0.85, relwidth=0.45, height=35)

        
        self.window.grab_set()
        self.window.mainloop()
        

    def screen_edit(self, id):
        self.window_edit = CTkToplevel(self.janela)
        self.window_edit.title('clear')
        self.window_edit.geometry('270x450')
        self.window_edit.maxsize(width=300, height=500)
        self.window_edit.minsize(width=270, height=400)
        self.window_edit.config(background=color_bg_toplevel)


        self.img = Image.open('logo2.png')
        self.img = ImageTk.PhotoImage(self.img)
        self.lb_img = CTkLabel(self.window_edit, image=self.img)
        self.lb_img.place(relx=.15, rely=0.1)

        self.specie_entry_edit = CTkEntry(self.window_edit, placeholder_text='Espécie',  text_color=color_text_toplevel,
                                        fg_color=color_bg_entry_toplevel, border_color=color_border_entry_top,
                                        text_font='Arial 15')
        self.specie_entry_edit.place(relx=0.05, rely=0.4, relwidth=0.9)


        self.order_entry_edit = CTkEntry(self.window_edit, placeholder_text='Order',  text_color=color_text_toplevel,
                                        fg_color=color_bg_entry_toplevel, border_color=color_border_entry_top,
                                        text_font='Arial 15')
        self.order_entry_edit.place(relx=0.05, rely=0.5, relwidth=0.9)


        self.location_entry_edit = CTkEntry(self.window_edit, placeholder_text='Local da coleta', text_color=color_text_toplevel,
                                        fg_color=color_bg_entry_toplevel, border_color=color_border_entry_top,
                                        text_font='Arial 15')
        self.location_entry_edit.place(relx=0.05, rely=0.6, relwidth=0.9)

        self.date_entry_edit = DateEntry(self.window_edit, font='Arial 15')
        self.date_entry_edit.place(relx=0.05, rely=0.7, relwidth=0.9)

        
        dados = self.search_registry(id)
        self.specie_entry_edit.insert(0, dados[1])
        self.order_entry_edit.insert(0, dados[2])
        self.location_entry_edit.insert(0, dados[3])
        self.date_entry_edit.set_date(dados[4])
        
        self.btn_edit = CTkButton(self.window_edit, text='Editar', text_font='Arial 15', cursor='hand2',
                            text_color=color_text_button_toplevel, fg_color=color_bg_button_toplevel,
                            border_color=color_border_button_toplevel, hover_color=color_hover_button_toplevel, 
                            command=lambda: self.alterar_cliente(dados[0]))
        self.btn_edit.place(relx=0.25, rely=0.85, relwidth=0.50, height=35)
        
        self.window_edit.grab_set()
        self.window_edit.mainloop()
    # Criando a janela inicial
    def tela(self):
        self.janela.title('Cadastro de Clientes')
        self.janela.configure(background='#1e3743')
        self.janela.geometry('700x500')
        self.janela.resizable(width=True,height=True)
        self.janela.maxsize(width=900, height=700)
        self.janela.minsize(width=500, height=400)
    
    # Criando os frames da janela inicial
    def frames_da_tela(self):
        
        self.frame_1 = Frame(self.janela, bd=4, bg='#dfe3ee', 
                            highlightbackground='#759fe6', highlightthickness=3)
        self.frame_1.place(relx=0, rely=0, relwidth=1, relheight=0.46)
        
        #Frame da página inicial
        self.frame_menu_internal = CTkFrame(self.janela, bg=color0)
        self.frame_menu_internal.place(x=0, y=0, relwidth=1, relheight=0.08)
        
        self.frame_2 = Frame(self.janela, bd=4, bg='#dfe3ee',
                            highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
        

    def reset_frames(self, func):
        self.frame.destroy()
        func()
        #func()
    #Frame com os botões no topo
    def widgets_frame_menu(self):
        self.btn_pg_inicial = CTkButton(self.frame_menu_internal, text='PÁGINA INICIAL',   
                                         fg_color=color0, bg_color=color0, corner_radius=0,
                                         cursor='hand2', hover_color=color2, text_color=color1,
                                         command=lambda: self.reset_frames(self.init_pg_inicial))
        
        self.btn_pg_inicial.place(relx=0, y=0, relheight=1, relwidth=0.25)
        self.btn_modificacao = CTkButton(self.frame_menu_internal, text='MODIFICAÇÃO',   
                                         fg_color=color0, bg_color=color0, corner_radius=0,
                                         cursor='hand2', hover_color=color2, text_color=color1,
                                         command=lambda: self.reset_frames(self.init_modi))
        self.btn_modificacao.place(relx=0.25, y=0, relheight=1, relwidth=0.25)
        self.btn_inventario = CTkButton(self.frame_menu_internal, text='INVENTARIO',   
                                         fg_color=color0, bg_color=color0, corner_radius=0,
                                         cursor='hand2', hover_color=color2, text_color=color1,
                                         command=lambda: self.reset_frames(self.init_inventory))
        self.btn_inventario.place(relx=0.50, y=0, relheight=1, relwidth=0.25)
        self.btn_backup = CTkButton(self.frame_menu_internal, text='BACKUP',   
                                         fg_color=color0, bg_color=color0, corner_radius=0,
                                         cursor='hand2', hover_color=color2, text_color=color1,
                                         command= self.init_backup)
        self.btn_backup.place(relx=0.75, y=0, relheight=1, relwidth=0.25)
 
    def init_modi(self):
        self.frame_modi = CTkFrame(self.janela, fg_color=color3)
        self.frame_modi.place(x=0, rely=0.08, relheight=1, relwidth=1)
        self.frame = self.frame_modi
    def init_inventory(self):
        self.frame_inventory = CTkFrame(self.janela, fg_color='red')
        self.frame_inventory.place(x=0, rely=0.08, relheight=1, relwidth=1)
        self.frame = self.frame_inventory
    def init_backup(self):
        self.backup()
    def init_pg_inicial(self):
        self.frame_pg_inicial = CTkFrame(self.janela, fg_color=color3)
        self.frame_pg_inicial.place(x=0, rely=0.08, relheight=1, relwidth=1)
        self.widgets_frame_pg_inicial()
        self.frame = self.frame_pg_inicial
    
    def widgets_frame_pg_inicial(self):
        
        self.btn_screen_add = CTkButton(self.frame_pg_inicial, text='ADD', text_font='Arial 20 bold', text_color=color1,
                                 fg_color=color0, cursor='hand2', hover_color=color2,
                                 command=lambda: self.screen_add())
        self.btn_screen_add.place(relx=0.015, rely=0.02)
        
        
        #self.lista_frame2()
        self.select_lista()
        
    

Aplication(CTk())