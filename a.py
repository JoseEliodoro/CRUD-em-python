import sqlite3 as lite
from datetime import datetime


# Criando conexão
con = lite.connect('crudlab.db')

# Inserir inventario
def inserir_form(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO tbl_laboratorio(specie, order_v, location, date_collect) VALUES (?,?,?,?)"
        cur.execute(query, i)


# Deletar inventario
def deletar_form(i):
   
    with con:
        cur = con.cursor()
        query = "DELETE FROM tbl_laboratorio WHERE id=%d"%i
        cur.execute(query)


# Atualizar inventario
def atualizar_form(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Inventario SET nome=?, local=?, descricao=?, marca=?, data_da_compra=?, valor_da_compra=?, serie=?, imagem=? WHERE id=?"
        cur.execute(query, i)


# Ver Inventario
def ver_form():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM tbl_laboratorio")
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens


# Ver Iten no inventario
def ver_iten(id):
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM tbl_laboratorio WHERE id=%d"%id)
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens




print(ver_iten(21))