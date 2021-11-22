import tkinter as tk 
from tkinter import messagebox 
import artista as art
import album as alb
import playlist as play
#artistas: Kodaline, Skank, Capital Inicial, Of Monsters And Men, The Lumineers

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle=controle
        self.root=root
        self.root.geometry('300x250')
        self.menubar=tk.Menu(self.root)
        self.artistaMenu=tk.Menu(self.menubar)
        self.albumMenu=tk.Menu(self.menubar)
        self.sairMenu=tk.Menu(self.menubar)
        self.playlistMenu=tk.Menu(self.menubar)
        self.topMenu=tk.Menu(self.menubar)

        self.artistaMenu.add_command(label='Cadastrar',\
                    command=self.controle.cadastraArtista)
        self.artistaMenu.add_command(label='Consultar',\
                    command=self.controle.consultaArtista)
        self.menubar.add_cascade(label="Artista",\
                    menu=self.artistaMenu)

        self.albumMenu.add_command(label='Cadastrar',\
                    command=self.controle.cadastraAlbum)
        self.albumMenu.add_command(label='Consultar',\
                    command=self.controle.consultaAlbum)
        self.menubar.add_cascade(label='Album',\
                    menu=self.albumMenu)

        
        self.playlistMenu.add_command(label='Cadastrar',\
                    command=self.controle.cadastraPlaylist)
        self.playlistMenu.add_command(label='Consultar',\
                    command=self.controle.consultaPlaylist)
        self.playlistMenu.add_command(label='Tocar',\
                    command=self.controle.tocaPlaylist)
        self.playlistMenu.add_command(label='Zerar',\
                    command=self.controle.zeraPlaylist)
        self.menubar.add_cascade(label='Playlist',\
                    menu=self.playlistMenu)
        
        

        self.topMenu.add_command(label='Músicas',\
                    command=self.controle.topMusicas)
        self.topMenu.add_command(label='Artistas',\
                    command=self.controle.topArtistas)
        self.menubar.add_cascade(label="Top 5",\
                    menu=self.topMenu)
        
        self.sairMenu.add_command(label='Salvar',\
                    command=self.controle.salvaDados)
        self.menubar.add_cascade(label='Sair',\
                    menu=self.sairMenu)

        self.root.config(menu=self.menubar)

class ControlePrincipal():
    def __init__(self):
        self.root=tk.Tk()
        
        self.ctrlArtista= art.CtrlArtista(self)
        self.ctrlAlbum= alb.CtrlAlbum(self)
        self.ctrlPlaylist= play.CtrlPlaylist(self)
        #self.ctrlTop=top.CtrlTop(self)

        self.limite=LimitePrincipal(self.root, self)

        self.root.title('Spotfou')
        self.root.mainloop()
    
    def cadastraAlbum(self):
        self.ctrlAlbum.cadastraAlbum()

    def consultaAlbum(self):
        self.ctrlAlbum.consultaAlbum()
    
    def cadastraArtista(self):
        self.ctrlArtista.cadastraArtista()
    
    def consultaArtista(self):
        self.ctrlArtista.consultaArtista()
    
    def cadastraPlaylist(self):
        self.ctrlPlaylist.cadastraPlaylist()
    
    def consultaPlaylist(self):
        self.ctrlPlaylist.consultaPlaylist()
    def tocaPlaylist(self):
        self.ctrlPlaylist.tocaPlaylist()
    
    def zeraPlaylist(self):
        self.ctrlPlaylist.zeraPlaylist()

    def topMusicas(self):
        self.ctrlPlaylist.topMusicas()
    
    def topArtistas(self):
        self.ctrlPlaylist.topArtistas()
    def salvaDados(self):
        self.ctrlAlbum.salvaAlbum()
        self.ctrlArtista.salvaArtista()
        self.ctrlPlaylist.salvaPlaylist()
        self.root.destroy()
        

if __name__=='__main__':
    c=ControlePrincipal()


