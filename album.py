import tkinter as tk 
from tkinter import messagebox
import pickle
import os.path

class Album:
    def __init__(self, titulo, artista, ano):
        self.__titulo=titulo
        self.__artista=artista
        self.__ano=ano
        self.__faixas=[]
    
    def getTitulo(self):
        return self.__titulo
    
    def getArtista(self):
        return self.__artista
    
    def getAno(self):
        return self.__ano
    
    def addFaixas(self, faixa):
        self.__faixas.append(faixa)
    
    def getFaixa(self):
        return self.__faixas
    
class LimiteInsereAlbum(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Album")
        self.controle = controle

        self.frameArtista=tk.Frame(self)
        self.frameTitulo=tk.Frame(self)
        self.frameAno=tk.Frame(self)
        self.frameMusica=tk.Frame(self)
        self.frameButton=tk.Frame(self)
        self.frameArtista.pack()
        self.frameTitulo.pack()
        self.frameAno.pack()
        self.frameMusica.pack()
        self.frameButton.pack()

        self.labelArtista = tk.Label(self.frameArtista,text="Artista: ")
        self.labelArtista.pack(side="left")
        self.inputArtista=tk.Entry(self.frameArtista, width=20)
        self.inputArtista.pack(side='left')

        self.labelTitulo = tk.Label(self.frameTitulo,text="Titulo: ")
        self.labelTitulo.pack(side="left")
        self.inputTitulo=tk.Entry(self.frameTitulo, width=20)
        self.inputTitulo.pack(side='left')

        self.labelAno = tk.Label(self.frameAno,text="Ano: ")
        self.labelAno.pack(side="left")
        self.inputAno=tk.Entry(self.frameAno, width=20)
        self.inputAno.pack(side='left')

        self.labelMusica=tk.Label(self.frameMusica, text='Musica')
        self.labelMusica.pack(side='left')
        self.inputMusica=tk.Entry(self.frameMusica, width=20)
        self.inputMusica.pack(side='left')

        self.buttonSubmit2 = tk.Button(self.frameButton ,text="Inserir Musica")      
        self.buttonSubmit2.pack(side="left")
        self.buttonSubmit2.bind("<Button>", controle.insereMusicaHandler)

        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)
    
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraAlbum():
    def __init__(self, str):
        messagebox.showinfo('Lista de Musicas', str)
class LimiteConsultaAlbum(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Consulta Album")
        self.controle = controle

        self.frameTitulo=tk.Frame(self)
        self.frameButton=tk.Frame(self)
        self.frameTitulo.pack()
        self.frameButton.pack()

        self.labelTitulo = tk.Label(self.frameTitulo,text="Titulo: ")
        self.labelTitulo.pack(side="left")
        self.inputTitulo=tk.Entry(self.frameTitulo, width=20)
        self.inputTitulo.pack(side='left')

        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandlerConsulta)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandlerConsulta)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandlerConsulta)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlAlbum():
    def __init__(self, controlePrincipal):
        self.controlePrincipal=controlePrincipal
        self.listaAlbuns=[]
        if not os.path.isfile('album.pickle'):
            self.listaAlbuns=[]
        else:
            with open('album.pickle', 'rb') as f:
                self.listaAlbuns=pickle.load(f)
    
    def salvaAlbum(self):
        if len(self.listaAlbuns)!=0:
            with open('album.pickle', 'wb') as f:
                pickle.dump(self.listaAlbuns, f)
    
    def getMusicasAlbum(self, nome):
        alb= []
        for procura in self.listaAlbuns:
            if procura.getTitulo()==nome:
                alb=procura.getFaixa()
        return alb

    def getAlbumByMusica(self, musica):
        for i in self.listaAlbuns:
            mus = i.getFaixa()
            for cont in mus:
                if cont==musica:
                    return i.getArtista()
        
    def getAlbum(self, titulo):
        alb = None
        for procura in self.listaAlbuns:
            if procura.getTitulo()==titulo:
                alb=procura
        return alb
    
    def getListaAlbum(self):
        return self.listaAlbuns
    
    def cadastraAlbum(self):
        self.listaMusicas=[]
        self.limiteIns= LimiteInsereAlbum(self)
    
    def consultaAlbum(self):
        self.limiteCons=LimiteConsultaAlbum(self)

    def insereMusicaHandler(self, event):
        mus=self.limiteIns.inputMusica.get()
        self.listaMusicas.append(mus)
        self.limiteIns.mostraJanela("Sucesso", "Musica inserida")
        self.clearMusicaHandler(event)

    def enterHandler(self, event):
        titulo=self.limiteIns.inputTitulo.get()
        artista=self.limiteIns.inputArtista.get()
        ano=self.limiteIns.inputAno.get()

        album=Album(titulo, artista, ano)
        for i in self.listaMusicas:
            album.addFaixas(i)
        
        self.listaMusicas=[]
        self.listaAlbuns.append(album)
        self.limiteIns.mostraJanela("Sucesso", "Album Cadastrado")
        self.clearHandler(event)
    
    def clearHandler(self, event):
        self.limiteIns.inputAno.delete(0, len(self.limiteIns.inputAno.get()))
        self.limiteIns.inputArtista.delete(0, len(self.limiteIns.inputArtista.get()))
        self.limiteIns.inputTitulo.delete(0, len(self.limiteIns.inputTitulo.get()))
    def clearMusicaHandler(self, event):
        self.limiteIns.inputMusica.delete(0, len(self.limiteIns.inputMusica.get()))
    def fechaHandler(self, event):
        self.limiteIns.destroy()
    
    def enterHandlerConsulta(self, event):
        titulo=self.limiteCons.inputTitulo.get()
        texto=''
        for procura in self.listaAlbuns:
            if procura.getTitulo()==titulo:
                texto+="Nome do album:"+procura.getTitulo()+'\n'
                texto+='Musicas:\n'
                for i in procura.getFaixa():
                    texto+= str(i)+'\n'
        if texto == '':
            texto+='Album não encontrado!'
        self.limiteLista = LimiteMostraAlbum(texto)           
        self.clearHandlerConsulta(event)
    
    def clearHandlerConsulta(self, event):
        self.limiteCons.inputTitulo.delete(0, len(self.limiteCons.inputTitulo.get()))
    
    def fechaHandlerConsulta(self, event):
        self.limiteCons.destroy()



        







