from customtkinter import *
from tkinter import *
from function import login, image
from main import Aplication

color0 = '#43b9c6'
color1 = '#347e87'
color2 = '#01264e'
class ScreenLogin():
    def __init__(self, root):
        #Atributos da tela
        self.root = root
        
        self.screen_config()
        self.image()
        self.data_input()
        self.root.mainloop()
        
    def press_enter(self, *a):
        if(a[0].keysym == "Return"):
            self.login()
            
    def screen_config(self): #Configuração da tela de login
        self.root.bind("<KeyPress>", self.press_enter)
        self.root.title('Tela de login')
        self.root.geometry('400x600+300+200')
        self.root.resizable(False, False)
        self.root.configure(fg_color=color1)


    def image(self): #Imagem do centro da tela
        self.img = image('img/LogoCRUDLab.png', 130, 130)
        self.img_user = Label(self.root, image=self.img, bg=color1)
        self.img_user.place(relx=0.35, rely=.2)
        
        

    def data_input(self): #Entrada dos dados de login
        
        
        """ Parte do entry de username """
        #Frame de borda inferior do username
        self.frame_border_username = CTkFrame(fg_color=color2)
        self.frame_border_username.place(relx=0.2, rely=.549, relwidth=.6, height=2)
        
        #Imagem lateral carta
        self.img_card = image('img/carta.png', 20, 15)
        self.lb_card = Label(self.root, image=self.img_card, bg=color1)
        self.lb_card.place(relx=.2, rely=.51)
                
        #Definindo o entry para a entrada do username
        self.entry_username = CTkEntry(self.root, placeholder_text='Username'.upper(), 
                                       text_font='Arial 12 bold', placeholder_text_color=color2,
                                       fg_color=color1, border_color=color1)
        self.entry_username.place(relx=0.30, rely=.5, relwidth=.51)
        
        
        """ Parte do entry de senha """
        #Frame de borda inferior do password
        self.frame_border_senha = CTkFrame(fg_color=color2)
        self.frame_border_senha.place(relx=0.2, rely=.649, relwidth=.6, height=2)
        
        #Imagem lateral cadeado
        self.img_key = image('img/senha.png', 20, 15)
        self.lb_key = Label(self.root, image=self.img_key, bg=color1)
        self.lb_key.place(relx=.2, rely=.61)
            
        #Definindo o entry para a entrada do password
        self.entry_password = CTkEntry(self.root, placeholder_text='Password'.upper(), 
                                    text_font='Arial 12 bold', placeholder_text_color=color2,
                                    fg_color=color1, border_color=color1, show='*')
        self.entry_password.place(relx=0.30, rely=.6, relwidth=.51)
        
        
        """ Parte do botão """
        #Botão para realizar o login
        btn_logar = CTkButton(self.root, text='Login'.upper(), text_font='arial 15 bold', 
                              fg_color=color2, cursor='hand2', command=self.login)
        btn_logar.place(relx=0.20, rely=.74, relwidth=.61, height=45)
        
        self.lb_sem_cadastro = Label(self.root, text='Entrar sem cadastro.', fg=color2,
                                bg=color1, cursor='hand2')
        #Entrar sem login
        """ self.lb_sem_cadastro.bind('<Enter>', self.inside_hover)
        self.lb_sem_cadastro.bind('<Leave>', self.outside_hover)
        self.lb_sem_cadastro.place(relx=.35, rely=.9) """
        
    def inside_hover(self, *args):
        self.lb_sem_cadastro['fg'] = '#fff'
    def outside_hover(self, *args):
        self.lb_sem_cadastro['fg'] = color2
            
    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        user = login(username, password)
        if user:
            self.root.destroy()
            Aplication(CTk())
        """ else:
            print(self.frame_border_senha.fg_color)
            self.frame_border_senha.fg_color='#ff0000'
            self.frame_border_senha.destroy()
            #self.frame_border_senha.pack() """
            
            
            
ScreenLogin(CTk())

