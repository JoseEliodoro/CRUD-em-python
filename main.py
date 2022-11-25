from tkinter import *
from tkinter import ttk
from customtkinter import *
from func_banco import Funcs
from tkcalendar import DateEntry

color0 = '#000'
color1 = '#fff'
color2 = '#111'
color3 = '#cecece'

class Aplication(Funcs):
    def __init__(self, janela):
        self.janela = janela
        #self.imagens_base64()
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.widgets_frame_menu()
        self.init_pg_inicial()
        self.frame = self.frame_pg_inicial
        #self.screen_add()
        #self.Menus()
        self.janela.mainloop()
    
        
    def screen_add(self):
        self.window = CTkToplevel(self.janela)
        self.window.title('ADD')
        
        self.specie_entry = CTkEntry(self.window, placeholder_text='Espécie')
        self.specie_entry.place(relx=0, rely=0.2, relwidth=0.4)
        
        self.order_entry = CTkEntry(self.window, placeholder_text='Order')
        self.order_entry.place(relx=0, rely=0.4, relwidth=0.9)
        
        self.location_entry = CTkEntry(self.window, placeholder_text='Local da coleta')
        self.location_entry.place(relx=0, rely=0.6, relwidth=0.7)
        
        self.date_entry = DateEntry(self.window)
        self.date_entry.place(relx=0, rely=.8, relwidth=0.7)
        
        self.btn_adda = CTkButton(self.window, text='Criar', command=self.add_cliente)
        self.btn_adda.place(relx=0.5, rely=0, relwidth=.3)
        
        self.window.grab_set()
        self.window.mainloop()
    def screen_edit(self, id):
        self.window_edit = CTkToplevel(self.janela)
        self.window_edit.title('ADD')
        
        self.specie_entry_edit = CTkEntry(self.window_edit, placeholder_text='Espécie')
        self.specie_entry_edit.place(relx=0, rely=0.2, relwidth=0.4)
        
        self.order_entry_edit = CTkEntry(self.window_edit, placeholder_text='Order')
        self.order_entry_edit.place(relx=0, rely=0.4, relwidth=0.9)
        
        self.location_entry_edit = CTkEntry(self.window_edit, placeholder_text='Local da coleta')
        self.location_entry_edit.place(relx=0, rely=0.6, relwidth=0.7)
        
        self.date_entry_edit = DateEntry(self.window_edit, day=31)
        self.date_entry_edit.place(relx=0, rely=.8, relwidth=0.7)
        
        dados = self.search_registry(id)
        self.specie_entry_edit.insert(0, dados[1])
        self.order_entry_edit.insert(0, dados[2])
        self.location_entry_edit.insert(0, dados[3])
        self.date_entry_edit.set_date(dados[4])
        
        self.btn_edit = CTkButton(self.window_edit, text='Editar', command=lambda: self.alterar_cliente(dados[0]))
        self.btn_edit.place(relx=0.5, rely=0, relwidth=.3)
        
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
                                         command=lambda: self.reset_frames(self.init_backup))
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
        self.frame_backup = CTkFrame(self.janela, fg_color='pink')
        self.frame_backup.place(x=0, rely=0.08, relheight=1, relwidth=1)
        self.frame = self.frame_backup
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
        
    # Criando os botões dos frames
    def widgets_frame1(self):
        
        """ 
        # Canvas dos botões a esquerda da janela
        self.canvas1_bt = Canvas(self.frame_1, bd=0, bg='#1e3743', highlightbackground='gray',
                                highlightthickness=5)
        self.canvas1_bt.place(relx=0.19, rely=0.08, relwidth=0.22, relheight=0.19)
        
        # criação do botão limpar
        self.bt_limpar = Button(self.frame_1, text='Limpar', bd=3,
                                bg='#107db2', fg='white', font=('verdana', 8, 'bold'),
                                activebackground='#108ecb', activeforeground='white',
                                command=self.limpa_tela)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        
        # criação do botão buscar
        self.bt_buscar = Button(self.frame_1, text='Buscar', bd=3,
                                bg='#107db2', fg='white', font=('verdana', 8, 'bold'),
                                command= self.busca_cliente)
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        
        
        # Canvas dos botões a direita da janela
        self.canvas2_bt = Canvas(self.frame_1, bd=0, bg='#1e3743', highlightbackground='gray',
                                highlightthickness=5)
        self.canvas2_bt.place(relx=0.59, rely=0.08, relwidth=0.32, relheight=0.19)
        
        # criação do botão novo
        #self.btNovo = PhotoImage(data=base64.b64decode(self.btNovo_base64))
        self.img_novo = self.imagem('adicionar.jpeg', 22, 22)
        self.bt_novo = Button(self.frame_1, image=self.img_novo, text='Novo', bd=3,
                            compound=LEFT, anchor=CENTER,
                                bg='#107db2', fg='white', font=('verdana', 8, 'bold'),
                                command=self.add_cliente)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        
        # criação do botão alterar
        self.bt_alterar = Button(self.frame_1, text='Alterar', bd=3,
                                bg='#107db2', fg='white', font=('verdana', 8, 'bold'),
                                command=self.alterar_cliente)
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        
        # criação do botão apagar
        self.bt_apagar = Button(self.frame_1, text='Apagar', bd=3,
                                bg='#107db2', fg='white', font=('verdana', 8, 'bold'),
                                command=self.deleta_cliente)
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)
    
        # Criando as Labes e Entries
        self.lb_codigo = Label(self.frame_1, text='Código', bg='#dfe3ee', fg='#107db2')
        self.lb_codigo.place(relx=0.05, rely=0.05)
        
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)
    
        self.lb_nome = Label(self.frame_1, text='Nome', bg='#dfe3ee', fg='#107db2')
        self.lb_nome.place(relx=0.05, rely=0.35)
        
        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.9)
        
        self.lb_telefone = Label(self.frame_1, text='Telefone', bg='#dfe3ee', fg='#107db2')
        self.lb_telefone.place(relx=0.05, rely=0.6)
        
        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)
        
        self.lb_cidade = Label(self.frame_1, text='Cidade', bg='#dfe3ee', fg='#107db2')
        self.lb_cidade.place(relx=0.5, rely=0.6)
        
        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)
     """
    def lista_frame2(self): # Parte da tela de login do meu outro crud(empreendedorismo)
        self.listaCli = ttk.Treeview(self.frame_pg_inicial, height=1, columns=("Col1", "Col2", "Col3","Col4"))
        self.listaCli.heading("#0")
        self.listaCli.heading("#1", text="Código")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Cidade")
        
        self.listaCli.column('#0', width=3)
        self.listaCli.column('#1', width=50)
        self.listaCli.column('#2', width=200)
        self.listaCli.column('#3', width=125)
        self.listaCli.column('#4', width=125)
        
        self.listaCli.place(relx=0.015, rely=0.115, relwidth=0.97, relheight=0.8)
        
        self.scrool_lista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scrool_lista.set)
        self.scrool_lista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.listaCli.bind("<Double-1>", self.OnDoubleClick)
        
        
    # Função de um MENU que fica na parte superior da janela
    """ def Menus(self):
        menuBar = Menu(self.janela)
        self.janela.config(menu=menuBar)
        fileMenu = Menu(menuBar)
        fileMenu2 = Menu(menuBar)
        
        menuBar.add_cascade(label="Opções", menu=fileMenu)
        menuBar.add_cascade(label="Relatorios", menu=fileMenu2)
        
        fileMenu.add_command(label="Sair", command= lambda: self.janela.destroy())
        fileMenu.add_command(label="Limpa Cliente", command= self.limpa_tela)
        
        fileMenu2.add_command(label="Ficha do Cliente", command=self.gerarRelatorioClientes)
     """
    

Aplication(CTk())