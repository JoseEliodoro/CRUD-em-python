from tkinter import *
from tkinter import ttk
import sqlite3
import io
from table_inventory import TblInventory
from tabela import MyList
from relatorio import Relatorios

class Funcs(MyList, TblInventory, Relatorios):
    
    # Funções do BANCO DE DADOS
    def conectar_bd(self):
        self.conn = sqlite3.connect('crudlab.db')
        self.cursor = self.conn.cursor()
        
    def desconectar_bd(self):
        self.conn.close(); print("Desconectando o Banco de Dados")
        
    def create_tbl_lab(self):
        self.conectar_bd(); print("Conectando ao Banco de Dados")
        # Criando a tabela
        self.cursor.execute("Create table if not exists tbl_laboratorio(id integer primary key autoincrement, specie text, order_v text, location text, date_collect date)")
        self.conn.commit(); print("Banco de dados criado com sucesso")
        self.desconectar_bd()


    # Função para criar tabela do inventário
    def create_tbl_inventory(self):
        self.conectar_bd(); print("Conectando ao Banco de Dados")
        # Criando a tabela
        self.cursor.execute("Create table if not exists tbl_inventory(id integer primary"
                            " key autoincrement, itens text, qtd text,  date_collect date)")
        self.conn.commit(); print("Banco de dados criado com sucesso")
        self.desconectar_bd()

    
    # Função para obter os dados quando estiver adicionando
    def variaveis(self):
        self.specie = self.specie_entry.get()
        self.order = self.order_entry.get()
        self.location = self.location_entry.get()
        self.date = self.date_entry.get()
      
        
    # Função para obter os dados quando estiver adicionando
    def variaveis_inventory(self):
        self.itens = self.itens_entry.get()
        self.qtd = self.qtd_entry.get()
        self.date_inventory = self.date_entry_inventory.get()
    
    
    # Função do Botão NOVO para cadastrar novos clientes
    def add_cliente(self):
        self.variaveis()
        self.conectar_bd()
        query = "INSERT INTO tbl_laboratorio(specie, order_v, location, date_collect) VALUES (?,?,?,?)"
        self.cursor.execute(query, (self.specie, self.order, self.location, self.date))
        self.conn.commit()
        self.desconectar_bd()
        self.select_lista()
    
    # Função que add na tabela inventário
    def add_inventory(self):
        self.variaveis_inventory()
        self.conectar_bd()
        query = "INSERT INTO tbl_inventory(itens, qtd, date_collect) VALUES (?,?,?)"
        self.cursor.execute(query, (self.itens, self.qtd, self.date_inventory))
        self.conn.commit()
        self.desconectar_bd()
        self.select_lista_inventory()
    
    # Função para adicionar a tabela   
    def select_lista_inventory(self):
        #self.listaCli.delete(*self.listaCli.get_children())
        self.conectar_bd()
        lista = self.cursor.execute("SELECT * FROM tbl_inventory ORDER BY id ASC;")
        self.create_invetory(self.frame_inventory, lista)
        """ for i in lista:
            print(i)
            self.listaCli.insert("", END, values=i) """
        
        self.desconectar_bd()
    
    # Função para pegar os dados quando estiver alterando
    def variaveis_edit_inventory(self):
        self.itens_edit = self.itens_entry_edit.get()
        self.qtd_edit = self.qtd_entry_edit.get()
        self.date_edit_inventory = self.date_entry_edit_inventory.get()

    
    # Função do botão ALTERAR para alterar os dados do cliente  
    def alterar_rigister_inventory(self, id):
        self.variaveis_edit_inventory()
        self.conectar_bd()
        self.cursor.execute("UPDATE tbl_inventory SET itens = ?, qtd = ?,"
                            " date_collect = ?  WHERE id = %d "%id,
                             (self.itens_edit, self.qtd_edit, self.date_edit_inventory))
        self.conn.commit()
        
        self.desconectar_bd()
        self.select_lista_inventory()
        self.window_edit.destroy()
        #self.limpa_tela(
    
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
    def deleta_cliente(self, table, id):
        self.conectar_bd()
        
        self.cursor.execute("DELETE FROM %s WHERE id = %d"%(table, id))
        self.conn.commit()
        
        self.desconectar_bd()

    # Função para pegar os dados quando estiver alterando
    def variaveis_edit(self):
        self.specie_edit = self.specie_entry_edit.get()
        self.order_edit = self.order_entry_edit.get()
        self.location_edit = self.location_entry_edit.get()
        self.date_edit = self.date_entry_edit.get()
   
    # Função do botão ALTERAR para alterar os dados do cliente  
    def alterar_cliente(self, id):
        self.variaveis_edit()
        self.conectar_bd()
        self.cursor.execute("UPDATE tbl_laboratorio SET specie = ?, order_v = ?,"
                            "location = ?, date_collect = ?  WHERE id = %d "%id,
                             (self.specie_edit, self.order_edit, self.location_edit, self.date_edit))
        self.conn.commit()
        
        self.desconectar_bd()
        self.select_lista()
        self.window_edit.destroy()
        #self.limpa_tela()

    # Função que busca pelo id o registro
    def search_registry(self, table, id):
        self.conectar_bd()
        self.cursor.execute("SELECT * FROM %s WHERE id=%d"%(table, id))
        datas = self.cursor.fetchall()
        return datas[0]

    # Função que cria o backup do banco
    def backup(self):
        
        self.conectar_bd()
        
        # Open() function 
        with io.open('backupcrudlab.db', 'w') as p: 
                
            # iterdump() function
            for line in self.conn.iterdump(): 
                
                p.write('%s\n' % line)
            
        print(' Backup performed successfully!')
        print(' Data Saved as backupdatabase_dump.db')
        
        self.desconectar_bd()