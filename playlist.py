import tkinter as tk
from tkinter import messagebox 
from tkinter import ttk
import pickle
import os.path
import operator


class Playlist:
    def __init__(self, nome):
        self.__nome=nome
        self.__musicas=[]
        
    
    def getNome(self):
        return self.__nome
    
    def addMusica(self, mus):
        self.__musicas.append(mus)
    
    def getMusicas(self):
        return self.__musicas

class LimiteInserePlaylist(tk.Toplevel):
    def __init__(self, controle, listaArtista):
        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title('Playlist')
        self.controle=controle

        self.frameNome=tk.Frame(self)
        self.frameArtista=tk.Frame(self)
        self.frameMusica=tk.Frame(self)
        self.frameButton=tk.Frame(self)
        self.frameNome.pack()
        self.frameArtista.pack()
        self.frameMusica.pack()
        self.frameButton.pack()

        self.labelNome=tk.Label(self.frameNome, text='Nome')
        self.labelNome.pack(side='left')
        self.inputNome=tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side='left')

        self.labelArtista = tk.Label(self.frameArtista,text="Escolha Artista: ")
        self.labelArtista.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.escolhaCombo.set('All')
        self.combobox = ttk.Combobox(self.frameArtista, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaArtista
       
        self.labelMusica=tk.Label(self.frameMusica, text='Escolha as Musicas:')
        self.labelMusica.pack(side='left')
        self.listbox=tk.Listbox(self.frameMusica)
        self.listbox.pack(side='left')

        

        self.buttonInsere = tk.Button(self.frameButton ,text="Insere Musica")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereMusica)
        
        self.buttonCria = tk.Button(self.frameButton ,text="Cria Playlist")           
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaPlaylist) 
    
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaPlaylist(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Consultar Playlist")
        self.controle=controle

        self.frameNome=tk.Frame(self)
        self.frameButton=tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()

        self.labelNome=tk.Label(self.frameNome, text='Nome:')
        self.labelNome.pack(side='left')
        self.inputNome=tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side='left')

        self.buttonConsulta=tk.Button(self.frameButton, text='Consulta')
        self.buttonConsulta.pack(side='left')
        self.buttonConsulta.bind('<Button>', controle.consultaPlaylistHandler)

        self.buttonFecha=tk.Button(self.frameButton, text='Concluído')
        self.buttonFecha.pack(side='left')
        self.buttonFecha.bind("<Button>", controle.fechaPlaylist)

        
    
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg) 
class limiteTop():
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteTocaPlaylist(tk.Toplevel):
    def __init__(self,controle, listaPlaylist):
        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Tocar Playlist")
        self.controle=controle

        self.framePlaylist=tk.Frame(self)
        self.frameMusica=tk.Frame(self)
        self.frameButton=tk.Frame(self)
        self.framePlaylist.pack()
        self.frameMusica.pack()
        self.frameButton.pack()

        self.labelPlaylist = tk.Label(self.framePlaylist,text="Escolha a Playlist: ")
        self.labelPlaylist.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.escolhaCombo.set('All')
        self.combobox = ttk.Combobox(self.framePlaylist, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaPlaylist

        self.labelMusica=tk.Label(self.frameMusica, text='Escolha as Musicas:')
        self.labelMusica.pack(side='left')
        self.listbox=tk.Listbox(self.frameMusica)
        self.listbox.pack(side='left')

        self.buttonConsulta=tk.Button(self.frameButton, text='Tocar')
        self.buttonConsulta.pack(side='left')
        self.buttonConsulta.bind('<Button>', controle.tocaPlaylistHandler)

        self.buttonFecha=tk.Button(self.frameButton, text='Concluído')
        self.buttonFecha.pack(side='left')
        self.buttonFecha.bind("<Button>", controle.fechaTocaPlaylist)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg) 


class CtrlPlaylist():
    def __init__(self, controlePrincipal):
        self.controlePrincipal=controlePrincipal
        self.listaMusicas=[]
        if not os.path.isfile('playlist.pickle'):
            self.listaPlaylist=[]
        else:
            with open('playlist.pickle', 'rb') as f:
                self.listaPlaylist=pickle.load(f)
        self.tocadas={}
        self.topart={}
    
    def salvaPlaylist(self):
        if len(self.listaPlaylist)!=0:
            with open('playlist.pickle', 'wb') as f:
                pickle.dump(self.listaPlaylist, f)

    def tocaPlaylistHandler(self, event):
        nomeMusica=self.limiteToca.listbox.get(tk.ACTIVE)
        texto='A musica'+nomeMusica+' foi executada!'
          
        
        if nomeMusica in self.tocadas:
            self.tocadas[nomeMusica]+=1
        else:
            self.tocadas[nomeMusica]=1
        
        
        nomeArtista=self.controlePrincipal.ctrlAlbum.getAlbumByMusica(nomeMusica)

        if nomeArtista in self.topart:
            self.topart[nomeArtista]+=1
        else:
            self.topart[nomeArtista]=1
            
        self.limiteToca.mostraJanela("Sucesso", texto)
          
          
    def tocaPlaylist(self):
        lista=[]
        for i in self.listaPlaylist:
            lista.append(i.getNome())
        self.limiteToca=LimiteTocaPlaylist(self, lista)
        self.limiteToca.escolhaCombo.trace('w', self.update2)
    
    def update2(self, var, indx, mode):
        self.limiteToca.listbox.delete(0,tk.END)
        selecionado=self.limiteToca.escolhaCombo.get()#aqui eu tenho o nome da 
        musicas=[]
        for i in self.listaPlaylist:
            if i.getNome()==selecionado:
                listaMusicas=i.getMusicas()
                for i in listaMusicas:
                    musicas.append(i)#lista de musicas da playlist escolhida
        for i in musicas:
            self.limiteToca.listbox.insert(tk.END, i)

    def fechaTocaPlaylist(self, event):
        self.limiteToca.destroy()

    def update(self, var, indx, mode):
        self.limiteIns.listbox.delete(0, tk.END)
        selecionado=self.limiteIns.escolhaCombo.get()
        albuns=self.controlePrincipal.ctrlAlbum.getListaAlbum()
        lista=[]
        for i in albuns:
            if i.getArtista()==selecionado:
                faixa=i.getFaixa()
                for cont in faixa:
                    lista.append(cont)
        for musica in lista:
            self.limiteIns.listbox.insert(tk.END, musica)

    def cadastraPlaylist(self):
        artistas=self.controlePrincipal.ctrlArtista.getListaArtista()
        art=[]
        for a in artistas:
            art.append(a.getNome())
        self.limiteIns=LimiteInserePlaylist(self, art)
        self.limiteIns.escolhaCombo.trace('w', self.update)
    
    def criaPlaylist(self, event):
        nome=self.limiteIns.inputNome.get()
        playlist=Playlist(nome)
        self.listaPlaylist.append(playlist)
        for i in self.listaMusicas:
            playlist.addMusica(i)
        self.limiteIns.mostraJanela("Sucesso", 'Playlist Cadastrada')
        self.listaMusicas=[]
        self.limiteIns.destroy()
    
    def insereMusica(self, event):
        musica=self.limiteIns.listbox.get(tk.ACTIVE)
        self.listaMusicas.append(musica)
        self.limiteIns.mostraJanela("Sucesso",'Musica Inserida')
        self.limiteIns.listbox.delete(tk.ACTIVE)
    
    def consultaPlaylist(self):
        self.limiteCons=LimiteConsultaPlaylist(self)
    
    def consultaPlaylistHandler(self, event):
        nome=self.limiteCons.inputNome.get()
        texto=''
        for i in self.listaPlaylist:
            if i.getNome()==nome:
                mus=i.getMusicas()
                for cont in mus:
                    texto+=cont+'\n'
            
        if texto =='':
            texto+='Playlist não Encontrada'
        self.limiteCons.mostraJanela('Musicas', texto)

    def zeraPlaylist(self):
        for i in self.tocadas.keys():
            self.tocadas[i]=0

    def fechaPlaylist(self, event):
        self.limiteCons.destroy()

    
        

    def topMusicas(self):
        self.limiteTop=limiteTop()

        
        sorted_x = sorted(self.tocadas.items(), key=operator.itemgetter(1))
        
        sorted_x.sort(reverse=True)
       
        texto=''
        texto+=str(sorted_x[0:5])
        self.limiteTop.mostraJanela('TOP 5 Musicas', texto)

    def topArtistas(self):
        self.limiteTop=limiteTop()
       
        sorted_x=sorted(self.topart.items(), key=operator.itemgetter(1))
        
        #sorted_x.sort(reverse=True)
        
        texto=''
        texto+=str(sorted_x[0:5])
        self.limiteTop.mostraJanela('TOP 5 Artistas', texto)
    


    

    
   
        



    



    