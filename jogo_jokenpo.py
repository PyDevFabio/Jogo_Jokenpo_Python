
# Jogo de Jokenpô

from ast import Not
from tkinter import *
from random import choice
from time import sleep
from tkinter.tix import X_REGION

# 1 - Pedra, 2 - Papel, 3 - Tesoura.
escolha_jogador = 0
escolha_computador = 0


class game:

    def __init__(self):
        self.window = Tk()
        self.window.title('Jogo Jokenpô')
        self.window.minsize(800, 620)
        self.window.maxsize(1000, 700)
        self.window.resizable(True, True)
        self.window.configure(bg='#2a5082')

        self.escolha_pc = [1, 2, 3]

        self.p_jogador = '0'
        self.p_computador = '0'

        self.img_papel = PhotoImage(file='asset/papel.png')
        self.img_pedra = PhotoImage(file='asset/pedra.png')
        self.img_tesoura = PhotoImage(file='asset/tesoura.png')

        # Widget Frame do Placar do Game
        self.frame_placar = Frame(self.window, bg='#2a5082')
        self.frame_placar.pack()

        self.placar_jogador = Label(self.frame_placar, text='  0  ',
                                    font='arial 14', bg='#2a5082', fg='white')
        self.placar_jogador.grid(row=0, column=0)

        self.lbl_x = Label(self.frame_placar, text='X',
                           bg='#2a5082', fg='white')
        self.lbl_x.grid(row=0, column=1)

        self.placar_computador = Label(self.frame_placar, text=0,
                                       font='arial 14', bg='#2a5082', fg='white')
        self.placar_computador.grid(row=0, column=2)

        # Nome do Placar - Jogador e Computador

        self.id_jogador = Label(self.frame_placar, text='Jogador',
                                font='arial 12', bg='#2a5082', fg='white')
        self.id_jogador.grid(row=1, column=0)

        self.id_computador = Label(self.frame_placar, text='Computador',
                                   font='arial 12', bg='#2a5082', fg='white')
        self.id_computador.grid(row=1, column=2)

        # Frame do Computador - Botão do Computador.
        self.frame_pc = Frame(self.window, width=350, bg='#2a5082')
        self.frame_pc.pack(padx=50, pady=50)

        # Botão de Escolha do Computador.
        self.btn_pc = Button(self.frame_pc, text='Computador',
                             bd=0, bg='#2a5082', fg='white',
                             font='arial 16')
        self.btn_pc.pack()

        # Frame do Jogador - Onde ficam os Botões.
        self.frame_jogador = Frame(self.window, width=350, bg='#2a5082')
        self.frame_jogador.pack()

        # Botão de Escolha dos Jogadores.
        self.btn_jogador_1 = Button(self.frame_jogador, image=self.img_pedra,
                                    padx=20)
        self.btn_jogador_1.grid(row=0, column=0)

        self.btn_jogador_1.bind('<Button>', self.escolha_computador)

        self.btn_jogador_2 = Button(self.frame_jogador, image=self.img_papel,
                                    padx=20)
        self.btn_jogador_2.grid(row=0, column=1)

        self.btn_jogador_2.bind('<Button>', self.escolha_2)

        self.btn_jogador_3 = Button(self.frame_jogador, image=self.img_tesoura,
                                    padx=20)
        self.btn_jogador_3.grid(row=0, column=2)

        self.btn_jogador_3.bind('<Button>', self.escolha_3)

        self.lbl_status = Label(self.window, text='0', bg='#2a5082', fg='white',
                                font='arial 16')
        self.lbl_status.pack(side='bottom')

        self.window.mainloop()

    def escolha_computador(self, event):
        """
        Quando o Jogador escolhe uma opção, gera 
        uma escolha pro computador.
        """
        # Escolha Jogador - Pedra
        if self.btn_jogador_1:
            pc = choice(self.escolha_pc)
            # Escolha pc: Pedra
            if pc == 1:
                self.btn_pc['image'] = self.img_pedra
                self.lbl_status['text'] = 'Empate'
            # Escolha pc: Papel
            elif pc == 2:
                self.btn_pc['image'] = self.img_papel
                self.lbl_status['text'] = 'Computador Venceu'
            # Escolha pc: Tesoura
            elif pc == 3:
                self.btn_pc['image'] = self.img_tesoura
                self.lbl_status['text'] = 'Jogador Venceu'

    def escolha_2(self, event):
        # Escolha Jogador: Papel
        if self.btn_jogador_2:
            pc = choice(self.escolha_pc)
            # Escolha pc: Pedra
            if pc == 1:
                self.btn_pc['image'] = self.img_pedra
                self.lbl_status['text'] = 'Jogador Venceu'
            # Escolha pc: Papel
            elif pc == 2:
                self.btn_pc['image'] = self.img_papel
                self.lbl_status['text'] = 'Empate'
            # Escolha pc: Tesoura
            elif pc == 3:
                self.btn_pc['image'] = self.img_tesoura
                self.lbl_status['text'] = 'Computador Venceu'

    def escolha_3(self, event):
        # Escolha Jogador: Tesoura
        if self.btn_jogador_3:
            pc = choice(self.escolha_pc)
            # Escolha pc: Pedra
            if pc == 1:
                self.btn_pc['image'] = self.img_pedra
                self.lbl_status['text'] = 'Computador Venceu'
            # Escolha pc: Papel
            elif pc == 2:
                self.btn_pc['image'] = self.img_papel
                self.lbl_status['text'] = 'Jogador Venceu'
            # Escolha pc: Tesoura
            elif pc == 3:
                self.btn_pc['image'] = self.img_tesoura
                self.lbl_status['text'] = 'Empate'


objeto = game()
