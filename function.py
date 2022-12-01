import json #Biblioteca para trabalhar com json
import os
from PIL import Image, ImageTk
filename = 'users.json'

def login(username, password):
    try:
        with open(filename) as file:
            users = json.load(file)
    except json.decoder.JSONDecodeError:
        print('Nenhum usuário cadastrado, chame o suporte')
    except FileNotFoundError:
        os.system('type nul > users.json')
    else:
        for user in users:
            if(user['username'].lower() == username.lower() and user['password'] == password):
                return True
            
    return False

def image(url, width=12, height=12):
    img = Image.open(url)
    img = img.resize((width, height))
    img = ImageTk.PhotoImage(img)
    return img