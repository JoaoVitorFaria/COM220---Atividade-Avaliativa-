import tkinter as tk 
from tkinter import messagebox
import pickle
import os.path

class Artista:
    def __init__(self, nome):
        self.__nome=nome
    
    def getNome(self):
        return self.__nome

class LimiteInsereArtista(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Artista")
        self.controle=controle

        self.frameNome=tk.Frame(self)
        self.frameButton=tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()

        self.labelNome=tk.Label(self.frameNome, text='Nome do Artista: ')
        self.labelNome.pack(side='left')

        self.inputNome=tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side='left')

        self.buttonSubmit=tk.Button(self.frameButton, text='Cadastrar')
        self.buttonSubmit.pack(side='left')
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)
    
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaArtista(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry("250x100")
        self.title("Consulta Artista")
        self.controle = controle

        self.frameNome=tk.Frame(self)
        self.frameButton=tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()

        self.labelNome=tk.Label(self.frameNome, text='Nome do Artista: ')
        self.labelNome.pack(side='left')

        self.inputNome=tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side='left')

        self.buttonSubmit=tk.Button(self.frameButton, text='Consultar')
        self.buttonSubmit.pack(side='left')
        self.buttonSubmit.bind("<Button>", controle.enterHandlerConsulta)

        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandlerConsulta)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandlerConsulta)
    
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlArtista():
    def __init__(self, controlePrincipal):
        self.controlePrincipal=controlePrincipal
        if not os.path.isfile('artista.pickle'):
            self.listaArtista=[]
        else:
            with open('artista.pickle', 'rb') as f:
                self.listaArtista=pickle.load(f)
    
    def salvaArtista(self):
        if len(self.listaArtista)!=0:
            with open('artista.pickle', 'wb') as f:
                pickle.dump(self.listaArtista, f)
    
    def getArtista(self, nome):
        procura=None
        for art in self.listaArtista:
            if art.getNome()==nome:
                procura=art
        return procura
    
    def getListaArtista(self):
        return self.listaArtista
    
    def cadastraArtista(self):
        self.limiteIns=LimiteInsereArtista(self)
    
    def consultaArtista(self):
        self.limiteCons=LimiteConsultaArtista(self)
    
    def enterHandler(self, event):
        nome= self.limiteIns.inputNome.get()
        art= Artista(nome)
        self.listaArtista.append(art)
        self.limiteIns.mostraJanela("Sucesso", "Artista Cadastrado")
        self.clearHandler(event)
    
    def clearHandler(self, event):
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
    
    def fechaHandler(self, event):
        self.limiteIns.destroy()
    
    def enterHandlerConsulta(self, event):
        nome=self.limiteCons.inputNome.get()
        albuns=self.controlePrincipal.ctrlAlbum.getListaAlbum()
        texto=''
        
        for i in albuns:
            if i.getArtista()==nome:
                texto+='Musicas do Album : '+i.getTitulo()+'\n'
                for mus in i.getFaixa():
                    texto+=mus+'\n'
                
        
        if texto =='':
            texto+='Artista Não Encontrado!'

        self.limiteCons.mostraJanela("Albuns", texto)
        self.clearHandlerConsulta(event)
    
    def clearHandlerConsulta(self, event):
        self.limiteCons.inputNome.delete(0, len(self.limiteCons.inputNome.get()))
    
    def fechaHandlerConsulta(self, event):
        self.limiteCons.destroy()