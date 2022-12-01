from reportlab.pdfgen import canvas
import webbrowser



# Criando a Classe que vai gerar os relatórios com os dados do cliente em PDF
class Relatorios():
    def open_folder(self, name):
        webbrowser.open(name+".pdf")
    
    def gerarRelatorioClientes(self, table, id):
        self.c = canvas.Canvas("animais.pdf")
        dados = self.search_registry(table, id)
        self.idRel = str(dados[0])
        self.specieRel = str(dados[1])
        self.OrderRel = str(dados[2])
        self.locationRel = str(dados[3])
        self.dateRel = str(dados[4])
        #self.descRel = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'''
        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(200, 790, 'Ficha de animais')
        
        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(50, 700, 'Id: ' )
        self.c.drawString(50, 670, 'Especie: ' )
        self.c.drawString(50, 640, 'Ordem: ' )
        self.c.drawString(50, 610, 'local da coleta: ' )
        self.c.drawString(50, 580, 'data da coleta: ' )
        #self.c.drawString(50, 550, 'descrição: ' )
        
        self.c.setFont("Helvetica", 18)
        self.c.drawString(150, 700, self.idRel)
        self.c.drawString(150, 670, self.specieRel)
        self.c.drawString(150, 640, self.OrderRel)
        self.c.drawString(150, 610, self.locationRel)
        self.c.drawString(150, 580, self.dateRel)
        #self.c.drawString(150, 580, self.descRel)
                    #x, y, width, height
        self.c.rect(25, 550, 550, 180, fill=False, stroke=True)
        
        self.c.showPage()
        self.c.save()
        self.open_folder('animais')
        
    def relatorio(self, table, id):
        self.c = canvas.Canvas("inventario.pdf")
        dados = self.search_registry(table, id)
        self.idRel = str(dados[0])
        self.specieRel = str(dados[1])
        self.OrderRel = str(dados[2])
        self.dateRel = str(dados[3])
        #self.descRel = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'''
        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(200, 790, 'Ficha de inventario')
        
        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(50, 700, 'Id: ' )
        self.c.drawString(50, 670, 'Item: ' )
        self.c.drawString(50, 640, 'Quantidade: ' )
        self.c.drawString(50, 580, 'Data: ' )
        #self.c.drawString(50, 550, 'descrição: ' )
        
        self.c.setFont("Helvetica", 18)
        self.c.drawString(150, 700, self.idRel)
        self.c.drawString(150, 670, self.specieRel)
        self.c.drawString(150, 640, self.OrderRel)
        self.c.drawString(150, 580, self.dateRel)
        #self.c.drawString(150, 580, self.descRel)
                    #x, y, width, height
        self.c.rect(25, 550, 550, 180, fill=False, stroke=True)
        
        self.c.showPage()
        self.c.save()
        self.open_folder('inventario')
        