from customtkinter import *
from tkinter import *
from PIL import Image, ImageTk
from function import login

color0 = '#43b9c6'
color1 = '#347e87'
color2 = '#01264e'


#Configuração de tela
root = CTk() 
root = root  
def keydown(*a):
    if(a[0].keysym == "Return"):
        logar()
    
root.bind("<KeyPress>", keydown)
root.title('Tela de login')
root.geometry('400x600+300+200')
root.resizable(False, False)
root.configure(fg_color=color1)
        
def image(url, width=12, height=12):
    img = Image.open(url)
    img = img.resize((width, height))
    img = ImageTk.PhotoImage(img)
    return img

img = image('img/biologia.png', 130, 130)
img_user = Label(root, image=img, bg=color1)
img_user.place(relx=0.35, rely=.2)

#Entry do usuário
frame_bottom = CTkFrame(fg_color=color2)
frame_bottom.place(relx=0.2, rely=.549, relwidth=.6, height=2)
img_carta = image('img/carta.png', 20, 15)
lb_carta = Label(root, image=img_carta, bg=color1)
lb_carta.place(relx=.2, rely=.51)
        
        
entry_username = CTkEntry(root, placeholder_text='Username'.upper(), 
                          text_font='Arial 12 bold',placeholder_text_color=color2,
                          fg_color=color1, border_color=color1)
entry_username.place(relx=0.30, rely=.5, relwidth=.51)
        
#Entry da senha
frame_bottom_senha = CTkFrame(fg_color=color2)
frame_bottom_senha.place(relx=0.2, rely=.649, relwidth=.6, height=2)
img_senha = image('img/senha.png', 20, 15)
lb_senha = Label(root, image=img_senha, bg=color1)
lb_senha.place(relx=.2, rely=.61)
    
        
entry_senha = CTkEntry(root, placeholder_text='Password'.upper(), 
                          text_font='Arial 12 bold',placeholder_text_color=color2,
                          fg_color=color1, border_color=color1, show='*')
entry_senha.place(relx=0.30, rely=.6, relwidth=.51)

def logar():
    username = entry_username.get()
    password = entry_senha.get()
    t = login(username, password)
    if t:
        root.destroy()
        Aplication(CTk())
        



btn_logar = CTkButton(root, text='Login'.upper(), text_font='arial 15 bold', fg_color=color2, cursor='hand2', command=logar)
btn_logar.place(relx=0.20, rely=.74, relwidth=.61, height=45)


def entrou(*args):
    lb_sem_cadastro['fg'] = '#fff'
def saiu(*args):
    lb_sem_cadastro['fg'] = color2
    
lb_sem_cadastro = Label(root, text='Entrar sem cadastro.', fg=color2, bg=color1,
                        cursor='hand2')
lb_sem_cadastro.bind('<Enter>', entrou)
lb_sem_cadastro.bind('<Leave>', saiu)
lb_sem_cadastro.place(relx=.35, rely=.9)




root.mainloop()