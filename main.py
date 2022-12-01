from tkinter import *
from tkinter import ttk
from customtkinter import *
""" from module import* """
from func_banco import Funcs
from tkcalendar import DateEntry

from PIL import Image, ImageTk

color0 = '#000'
color1 = '#fff'
color2 = '#008080'
color3 = '#008080'
color_text_toplevel = 'purple'
color_bg_toplevel = '#008080'
color_bg_entry_toplevel = 'blue'
color_border_entry_top = 'white'
color_text_button_toplevel = 'pink'
color_bg_button_toplevel = 'red'
color_border_button_toplevel = 'green'
color_hover_button_toplevel = 'black'

class Aplication(Funcs):
    def __init__(self, janela):
        self.janela = janela
        self.create_tbl_lab()
        self.create_tbl_inventory()
        self.tela()
        self.frames_da_tela()
        self.widgets_frame_menu()
        self.init_pg_inicial()
        self.frame = self.frame_pg_inicial
        #self.screen_add()
        #self.Menus()
        self.janela.mainloop()
    
    # Função para cria a janela de add da tabela tbl_laboratorio   
    def screen_add(self):
        # Configurações da janela
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

        # Definindo entrys para entradas de dados
        self.specie_entry = CTkEntry(self.window, placeholder_text='Espécie',  text_color=color1,
                                        fg_color=color_bg_entry_toplevel, border_color=color_border_entry_top,
                                        text_font='Arial 15')
        self.specie_entry.place(relx=0.05, rely=0.4, relwidth=0.9)


        self.order_entry = CTkEntry(self.window, placeholder_text='Order',  text_color=color1,
                                        fg_color=color_bg_entry_toplevel, border_color=color_border_entry_top,
                                        text_font='Arial 15')
        self.order_entry.place(relx=0.05, rely=0.5, relwidth=0.9)


        self.location_entry = CTkEntry(self.window, placeholder_text='Local da coleta', text_color=color1,
                                        fg_color=color_bg_entry_toplevel, border_color=color_border_entry_top,
                                        text_font='Arial 15')
        self.location_entry.place(relx=0.05, rely=0.6, relwidth=0.9)
        
        self.date_entry = DateEntry(self.window, font='Arial 15')
        self.date_entry.place(relx=0.05, rely=0.7, relwidth=0.9)

        # Definindo botão para add do novo registro
        self.btn_add = CTkButton(self.window, text='Salvar', text_font='Arial 15', cursor='hand2',
                            text_color=color1, fg_color=color_bg_button_toplevel,
                            border_color=color_border_button_toplevel, hover_color=color2,
                            command=self.add_cliente)
        self.btn_add.place(relx=0.05, rely=0.85, relwidth=0.45, height=35)

        # Definindo botão para limpar as entradas de dados
        self.btn_clear = CTkButton(self.window, text='Limpar', text_font='Arial 15', cursor='hand2',
                            text_color=color_text_button_toplevel, fg_color=color_bg_button_toplevel,
                            border_color=color_border_button_toplevel, hover_color=color_hover_button_toplevel)
        self.btn_clear.place(relx=0.5, rely=0.85, relwidth=0.45, height=35)

        
        self.date_entry = DateEntry(self.window, font='Arial 15')
        self.date_entry.place(relx=0.05, rely=0.7, relwidth=0.9)

        self.btn_add = CTkButton(self.window, text='Salvar', text_font='Arial 15', cursor='hand2', text_color=color_text_button_toplevel, fg_color=color_bg_button_toplevel,
                            border_color=color_border_button_toplevel, hover_color=color_hover_button_toplevel,  command=self.add_cliente)
        self.btn_add.place(relx=0.05, rely=0.85, relwidth=0.45, height=35)

        self.btn_clear = CTkButton(self.window, text='Limpar', text_font='Arial 15', cursor='hand2', text_color=color_text_button_toplevel, fg_color=color_bg_button_toplevel,
                            border_color=color_border_button_toplevel, hover_color=color_hover_button_toplevel,
                            command=self.clean_screen)
        self.btn_clear.place(relx=0.5, rely=0.85, relwidth=0.45, height=35)

        self.window.grab_set()
        self.window.mainloop()
        
    # Função para cria a janela de edição da tabela tbl_laboratorio
    def screen_edit(self, id):
        # Configurações da janela
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

        # Definindo entry para entradas de dados
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

        # Pre-carregando informações para edição
        dados = self.search_registry('tbl_laboratorio', id)
        self.specie_entry_edit.insert(0, dados[1])
        self.order_entry_edit.insert(0, dados[2])
        self.location_entry_edit.insert(0, dados[3])
        self.date_entry_edit.set_date(dados[4])
        
        # Definindo butão para edição
        self.btn_edit = CTkButton(self.window_edit, text='Editar', text_font='Arial 15', cursor='hand2',
                            text_color=color_text_button_toplevel, fg_color=color_bg_button_toplevel,
                            border_color=color_border_button_toplevel, hover_color=color_hover_button_toplevel, 
                            command=lambda: self.alterar_cliente(dados[0]))
        self.btn_edit.place(relx=0.25, rely=0.85, relwidth=0.50, height=35)
        
        self.window_edit.grab_set()
        self.window_edit.mainloop()
    
    # Função com as configurações da tela
    def tela(self):
        self.janela.title('Cadastro de Clientes')
        self.janela.configure(background='#1e3743')
        self.janela.geometry('700x500')
        self.janela.resizable(width=True,height=True)
        self.janela.maxsize(width=900, height=700)
        self.janela.minsize(width=500, height=400)
    
    # Criando os frames da janela inicial
    def frames_da_tela(self):
        
        self.frame_1 = Frame(self.janela, bd=4, bg='#008080', 
                            highlightbackground='#759fe6', highlightthickness=3)
        self.frame_1.place(relx=0, rely=0, relwidth=1, relheight=0.46)
        
        #Frame da página inicial
        self.frame_menu_internal = CTkFrame(self.janela, bg=color0)
        self.frame_menu_internal.place(x=0, y=0, relwidth=1, relheight=0.08)
        
        self.frame_2 = Frame(self.janela, bd=4, bg='#008080',
                            highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
        
    # Função para auxiliar a mudanção de tela
    def reset_frames(self, func):
        self.frame.destroy()
        func()
    
    # Frame com os botões no topo
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
 
    # Função para iniciar a tela de modificações
    def init_modi(self):
         # Frame 1 da tela modify
        self.frame_modi = CTkFrame(self.janela, fg_color=color3)
        self.frame_modi.place(x=0, rely=0.08, relheight=0.95, relwidth=1)
        self.list_modify_frame()
        self.frame = self.frame_modi
        self.select_lista_modify()
        
        # Frame 2 da tela modify
        """ self.frame_modi_2 = CTkFrame(self.janela, fg_color=color3)
        self.frame_modi_2.place(x=0, rely=0.5, relheight=0.75, relwidth=1)
        self.list_modify_frame_2()
        self.frame = self.frame_modi_2 """
        
   
    # Função para iniciar a tela do inventário
    def init_inventory(self):
        self.frame_inventory = CTkFrame(self.janela, fg_color=color3)
        self.frame_inventory.place(x=0, rely=0.08, relheight=1, relwidth=1)
        self.widgets_inventory()
        self.frame = self.frame_inventory
    
    # Função para chamar o backup
    def init_backup(self):
        self.backup()
   
    # Função para iniciar a tela inicial
    def init_pg_inicial(self):
        self.frame_pg_inicial = CTkFrame(self.janela, fg_color=color3)
        self.frame_pg_inicial.place(x=0, rely=0.08, relheight=1, relwidth=1)
        self.widgets_frame_pg_inicial()
        self.frame = self.frame_pg_inicial
    

    def widgets_frame_pg_inicial(self):
        
        # Denifindo butão de add na janela de inventário
        self.btn_screen_add = CTkButton(self.frame_pg_inicial, text='ADD', text_font='Arial 20 bold', text_color=color1,
                                 fg_color='#2c605f', cursor='hand2', hover_color=color2,
                                 command=lambda: self.screen_add())
        self.btn_screen_add.place(relx=0.015, rely=0.02)
        
        
        #self.lista_frame2()
        self.select_lista()
        
    # PARTE DO INVENTORY
    def widgets_inventory(self): # cria os widgets da para o frame dos inventarios
        
        # Denifindo butão de add na janela de inventário
        self.btn_screen_add = CTkButton(self.frame_inventory, text='ADD', text_font='Arial 20 bold', text_color=color1,
                                 fg_color='#2c605f', cursor='hand2', hover_color=color2,
                                 command=lambda: self.screen_add_inventory())
        self.btn_screen_add.place(relx=0.015, rely=0.02)  
        
        # Chamada de função para gerar tabela do banco
        self.select_lista_inventory()
    
    # TFunção para cria a janela de add da tabela tbl_inventory
    def screen_add_inventory(self):
        # Configuração da tela de add do inventário
        self.window = CTkToplevel(self.janela)
        self.window.title('clear')
        self.window.geometry('270x450')
        self.window.maxsize(width=300, height=500)
        self.window.minsize(width=270, height=400)
        self.window.config(background=color_bg_toplevel)

        # Definindo logo
        self.img = Image.open('logo2.png')
        self.img = ImageTk.PhotoImage(self.img)
        self.lb_img = CTkLabel(self.window, image=self.img)
        self.lb_img.place(relx=.15, rely=0.1)

        # Criando entradas
        self.itens_entry = CTkEntry(self.window, placeholder_text='Item',  text_color=color_text_toplevel,
                                        fg_color=color_bg_entry_toplevel, border_color=color_border_entry_top,
                                        text_font='Arial 15')
        self.itens_entry.place(relx=0.05, rely=0.5, relwidth=0.9)


        self.qtd_entry = CTkEntry(self.window, placeholder_text='Quantidade',  text_color=color_text_toplevel,
                                        fg_color=color_bg_entry_toplevel, border_color=color_border_entry_top,
                                        text_font='Arial 15')
        self.qtd_entry.place(relx=0.05, rely=0.6, relwidth=0.9)

        
        self.date_entry_inventory = DateEntry(self.window, font='Arial 15')
        self.date_entry_inventory.place(relx=0.05, rely=0.7, relwidth=0.9)

        # Botões da tela
        self.btn_add = CTkButton(self.window, text='Salvar', text_font='Arial 15', cursor='hand2',
                            text_color=color_text_button_toplevel, fg_color=color_bg_button_toplevel,
                            border_color=color_border_button_toplevel, hover_color=color_hover_button_toplevel,
                            command=self.add_inventory)
        self.btn_add.place(relx=0.05, rely=0.85, relwidth=0.45, height=35)

        self.btn_clear = CTkButton(self.window, text='Limpar', text_font='Arial 15', cursor='hand2',
                            text_color=color_text_button_toplevel, fg_color=color_bg_button_toplevel,
                            border_color=color_border_button_toplevel, hover_color=color_hover_button_toplevel,
                            command=self.clean_screen_inventory)
        self.btn_clear.place(relx=0.5, rely=0.85, relwidth=0.45, height=35)

        
        self.window.grab_set()
        self.window.mainloop()
        
    # Função para cria a janela de edição da tabela tbl_inventory
    def screen_edit_inventroy(self, id):
        # Configurações da janela
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

        # Definindo entry para entradas de dados
        self.itens_entry_edit = CTkEntry(self.window_edit, placeholder_text='Item',  text_color=color_text_toplevel,
                                        fg_color=color_bg_entry_toplevel, border_color=color_border_entry_top,
                                        text_font='Arial 15')
        self.itens_entry_edit.place(relx=0.05, rely=0.4, relwidth=0.9)


        self.qtd_entry_edit = CTkEntry(self.window_edit, placeholder_text='Quantidade',  text_color=color_text_toplevel,
                                        fg_color=color_bg_entry_toplevel, border_color=color_border_entry_top,
                                        text_font='Arial 15')
        self.qtd_entry_edit.place(relx=0.05, rely=0.5, relwidth=0.9)



        self.date_entry_edit_inventory = DateEntry(self.window_edit, font='Arial 15')
        self.date_entry_edit_inventory.place(relx=0.05, rely=0.7, relwidth=0.9)

        # Pre-carregando informações para edição
        dados = self.search_registry('tbl_inventory', id)
        self.itens_entry_edit.insert(0, dados[1])
        self.qtd_entry_edit.insert(0, dados[2])
        self.date_entry_edit_inventory.set_date(dados[3])
        
        # Definindo butão para edição
        self.btn_edit = CTkButton(self.window_edit, text='Editar', text_font='Arial 15', cursor='hand2',
                            text_color=color_text_button_toplevel, fg_color=color_bg_button_toplevel,
                            border_color=color_border_button_toplevel, hover_color=color_hover_button_toplevel, 
                            command=lambda: self.alterar_rigister_inventory(dados[0]))
        self.btn_edit.place(relx=0.25, rely=0.85, relwidth=0.50, height=35)
        
        self.window_edit.grab_set()
        self.window_edit.mainloop()
    
   # Criando a Treeview do frame Modify    
    def list_modify_frame(self):
        self.list_modify = ttk.Treeview(self.frame_modi, height=3, columns=("Col1", "Col2", "Col3","Col4","Col5"))
        self.list_modify.heading("#0", text="")
        self.list_modify.heading("#1", text="ID")
        self.list_modify.heading("#2", text="Espécie")
        self.list_modify.heading("#3", text="Ordem")
        self.list_modify.heading("#4", text="Local da Coleta")
        self.list_modify.heading("#5", text="Data da Modificação")
        
        self.list_modify.column('#0', width=1)
        self.list_modify.column('#1', width=30)
        self.list_modify.column('#2', width=125)
        self.list_modify.column('#3', width=125)
        self.list_modify.column('#4', width=125)
        self.list_modify.column('#5', width=125)
        
        self.list_modify.place(relx=0.01, rely=0.01, relwidth=0.95, relheight=0.92)
        
        self.yscrool_lista = Scrollbar(self.frame_modi, orient='vertical')
        self.xscrool_lista = Scrollbar(self.frame_modi, orient='horizontal')
        self.list_modify.configure(yscrollcommand=self.yscrool_lista.set, xscrollcommand=self.xscrool_lista.set)
        self.yscrool_lista.place(relx=0.96, rely=0.01, relwidth=0.02, relheight=0.92)
        self.xscrool_lista.place(relx=0.01, rely=0.93, relwidth=0.95, relheight=0.03)
    
       
    # Criando a Treeview do frame_2 Modify    
    """ def list_modify_frame_2(self):
        self.list_modify_2 = ttk.Treeview(self.frame_modi_2, height=3, columns=("Col1", "Col2", "Col3","Col4","Col5"))
        self.list_modify_2.heading("#0", text="")
        self.list_modify_2.heading("#1", text="ID")
        self.list_modify_2.heading("#2", text="Espécie")
        self.list_modify_2.heading("#3", text="Ordem")
        self.list_modify_2.heading("#4", text="Local da Coleta")
        self.list_modify_2.heading("#5", text="Data da Modificações")
        
        self.list_modify_2.column('#0', width=1)
        self.list_modify_2.column('#1', width=30)
        self.list_modify_2.column('#2', width=125)
        self.list_modify_2.column('#3', width=125)
        self.list_modify_2.column('#4', width=125)
        self.list_modify_2.column('#5', width=125)
        
        self.list_modify_2.place(relx=0.01, rely=0.01, relwidth=0.95, relheight=0.59)
        
        self.yscrool_lista = Scrollbar(self.frame_modi_2, orient='vertical')
        self.xscrool_lista = Scrollbar(self.frame_modi_2, orient='horizontal')
        self.list_modify_2.configure(yscrollcommand=self.yscrool_lista.set, xscrollcommand=self.xscrool_lista.set)
        self.yscrool_lista.place(relx=0.96, rely=0.01, relwidth=0.02, relheight=0.59)
        self.xscrool_lista.place(relx=0.01, rely=0.6, relwidth=0.95, relheight=0.05) """
    
Aplication(CTk())