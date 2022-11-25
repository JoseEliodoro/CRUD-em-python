from tkinter import *
from tkinter import ttk
import sqlite3

from reportlab.pdfgen import canvas
""" from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont """
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser
from PIL import ImageTk, Image
import base64
from fadsf import MyList
from adicionar import Relatorios

class Funcs(MyList, Relatorios):
    # Função do Botão LIMPAR
    def limpa_tela(self):
        self.id_entry.delete(0, END)
        self.specie_entry.delete(0, END)
        self.order_entry.delete(0, END)
        self.localtion_entry.delete(0, END)
    
    # Funções do BANCO DE DADOS
    def conectar_bd(self):
        self.conn = sqlite3.connect('crudlab.db')
        self.cursor = self.conn.cursor()
        
    def desconectar_bd(self):
        self.conn.close(); print("Desconectando o Banco de Dados")
        
    def montaTabelas(self):
        self.conectar_bd(); print("Conectando ao Banco de Dados")
        # Criando a tabela
        self.cursor.execute("Create table if not exists tbl_laboratorio(id integer primary key autoincrement, specie text, order_v text, location text, date_collect date)")
        self.conn.commit(); print("Banco de dados criado com sucesso")
        self.desconectar_bd()

    def variaveis(self):
        #self.id = self.id_entry.get()
        self.specie = self.specie_entry.get()
        self.order = self.order_entry.get()
        self.location = self.location_entry.get()
        self.date = self.date_entry.get()
        
    # Função do Botão NOVO para cadastrar novos clientes
    def add_cliente(self):
        self.variaveis()
        self.conectar_bd()
        query = "INSERT INTO tbl_laboratorio(specie, order_v, location, date_collect) VALUES (?,?,?,?)"
        self.cursor.execute(query, (self.specie, self.order, self.location, self.date))
        self.conn.commit()
        self.desconectar_bd()
        self.select_lista()
        #self.limpa_tela()
    
    # Função para adicionar a tabela   
    def select_lista(self):
        #self.listaCli.delete(*self.listaCli.get_children())
        
        self.conectar_bd()
        lista = self.cursor.execute("SELECT * FROM tbl_laboratorio ORDER BY id ASC;")
        self.create(self.frame_pg_inicial, lista)
        """ for i in lista:
            print(i)
            self.listaCli.insert("", END, values=i) """
        
        self.desconectar_bd()

    # Função do botão APAGAR para remover clientes do banco de dados
    def deleta_cliente(self, id):
        self.conectar_bd()
        
        self.cursor.execute("DELETE FROM tbl_laboratorio WHERE id = %d"%id)
        self.conn.commit()
        
        self.desconectar_bd()
        #self.limpa_tela()
        #self.select_lista()

    # Função do botão ALTERAR para alterar os dados do cliente
    def variaveis_edit(self):
        self.specie_edit = self.specie_entry_edit.get()
        self.order_edit = self.order_entry_edit.get()
        self.location_edit = self.location_entry_edit.get()
        self.date_edit = self.date_entry_edit.get()
        
    def alterar_cliente(self, id):
        self.variaveis_edit()
        self.conectar_bd()
        print(id)
        self.cursor.execute("UPDATE tbl_laboratorio SET specie = ?, order_v = ?,"
                            "location = ?, date_collect = ?  WHERE id = %d "%id,
                             (self.specie_edit, self.order_edit, self.location_edit, self.date_edit))
        self.conn.commit()
        
        self.desconectar_bd()
        self.select_lista()
        #self.limpa_tela()

    # Função do botão BUSCAR para selecionar os dados do cliente procurado
    def busca_cliente(self):
        self.conectar_bd()
        
        self.listaCli.delete(*self.listaCli.get_children())
        
        self.nome_entry.insert(END, '%')
        nome = self. nome_entry.get()
        self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes
                            WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC """ % nome)
        buscaNomeCliente = self.cursor.fetchall()
        
        for i in buscaNomeCliente:
            
            self.listaCli.insert("", END, values=i)
    
        self.limpa_tela()
        
        self.desconectar_bd()
    def search_registry(self, id):
        self.conectar_bd()
        self.cursor.execute("SELECT * FROM tbl_laboratorio WHERE id=%d"%id)
        datas = self.cursor.fetchall()
        return datas[0]
        
    def imagem(self,caminho, t1,t2):
        self.app_img = Image.open(caminho)
        self.app_img = self.app_img.resize((t1,t2))
        self.app_img = ImageTk.PhotoImage(self.app_img)
        return self.app_img
    
