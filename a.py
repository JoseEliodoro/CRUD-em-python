import sqlite3
from datetime import datetime


def montaTabelas():
    
    conn = sqlite3.connect('crudlab.db')
    cursor = conn.cursor()
    
    cursor.execute("Create table if not exists tbl_laboratorio(id integer primary key autoincrement, specie text, order_v text, location text, date_collect date)")
    conn.commit(); print("Banco de dados criado com sucesso")
    conn.close(); print("Desconectando o Banco de Dados")
    
data_today = datetime.now()
print(data_today.strftime('%d/%m/%y'))