from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


class TicTacToe(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.config(background='black')
        self.geometry(f'230x280+'
                      f'{int(self.winfo_screenwidth()/2 - 400/2)}+{int(self.winfo_screenheight()/2 - 500/2)}')
        self.iconphoto(True, PhotoImage(file='Da.png'))
        self.title('TicTacToe')
        # Set player 1 to None, value is going to change once X or O button is clicked
        self.lp1_choice = []
        # Check if position has been taken, using letter N to mark if position is NOT taken
        self.checkposition = ['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]
        # Frame linha 1
        self.button_frame1 = Frame(self, background='black')
        self.button_frame1.pack()

        # Abre e redefine o tamanho da imagem
        i_tuple = (56, 63)

        self.opened_img_x = Image.open('x.png')  # Abre a imagem
        self.resized_x = self.opened_img_x.resize(i_tuple, Image.ANTIALIAS)  # Redefine o tamanho da imagem
        self.img_x = ImageTk.PhotoImage(self.resized_x)  # Cria a imagem para ser exibida

        self.opened_img_o = Image.open('o.png')  # Abre a imagem
        self.resized_o = self.opened_img_o.resize(i_tuple, Image.ANTIALIAS)  # Redefine o tamanho da imagem
        self.img_o = ImageTk.PhotoImage(self.resized_o)  # Cria a imagem para ser exibida

        # Buttons
        self.b1 = Button(self.button_frame1, border=1, width=4, height=2, font=('Verdana', 15),
                         command=lambda: self.change_x_o('b1'))
        self.b1.grid(row=0, column=0, padx=2, pady=2)
        self.b2 = Button(self.button_frame1, width=4, height=2, border=1, font=('Verdana', 15),
                         command=lambda: self.change_x_o('b2'))
        self.b2.grid(row=0, column=1, padx=2, pady=2)
        self.b3 = Button(self.button_frame1, width=4, height=2, border=1, font=('Verdana', 15),
                         command=lambda: self.change_x_o('b3'))
        self.b3.grid(row=0, column=2, padx=2, pady=2)

        # Frame linha 2
        self.button_frame2 = Frame(self, background='black')
        self.button_frame2.pack()

        # Buttons
        self.b4 = Button(self.button_frame2, width=4, height=2, border=1, font=('Verdana', 15),
                         command=lambda: self.change_x_o('b4'))
        self.b4.grid(row=1, column=0, padx=2, pady=2)
        self.b5 = Button(self.button_frame2, width=4, height=2, border=1, font=('Verdana', 15),
                         command=lambda: self.change_x_o('b5'))
        self.b5.grid(row=1, column=1, padx=2, pady=2)
        self.b6 = Button(self.button_frame2, width=4, height=2, border=1, font=('Verdana', 15),
                         command=lambda: self.change_x_o('b6'))
        self.b6.grid(row=1, column=2, padx=2, pady=2)

        # Frame linha 3
        self.button_frame3 = Frame(self, background='black')
        self.button_frame3.pack()

        # Buttons
        self.b7 = Button(self.button_frame2, width=4, height=2, border=1, font=('Verdana', 15),
                         command=lambda: self.change_x_o('b7'))
        self.b7.grid(row=2, column=0, padx=2, pady=2)
        self.b8 = Button(self.button_frame2, width=4, height=2, border=1, font=('Verdana', 15),
                         command=lambda: self.change_x_o('b8'))
        self.b8.grid(row=2, column=1, padx=2, pady=2)
        self.b9 = Button(self.button_frame2, width=4, height=2, border=1, font=('Verdana', 15),
                         command=lambda: self.change_x_o('b9'))
        self.b9.grid(row=2, column=2, padx=2, pady=2)

        # Set all buttons to DISABLED state
        for but in (self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9):
            but.config(state=DISABLED, background='white')

        self.choose_x_o_frame = Frame(self, background='black')
        self.choose_x_o_frame.pack()

        self.bchoose_f = Frame(self, background='black')
        self.bchoose_f.pack()
        self.ltxt = Label(self.choose_x_o_frame, text='Você quer ser X ou O?', font=('Verdana', 10),
                          bg='black', fg='white')
        self.ltxt.pack(anchor=N)
        self.b_x = Button(self.bchoose_f, text='X', width=5, font=('Verdana', 10), command=lambda: self.choice('X'))
        self.b_x.pack(side=LEFT, padx=5)
        self.b_o = Button(self.bchoose_f, text='O', width=5, font=('Verdana', 10), command=lambda: self.choice('O'))
        self.b_o.pack(side=LEFT)

        self.turn = 0

    # Function to change button x and o to a restart and exit
    def confinew(self):
        self.b_x.destroy()
        self.b_o.destroy()
        reiniciar = Button(self.bchoose_f, text='Reiniciar', width=10, command=self.reiniciar)
        reiniciar.pack(side=LEFT, padx=5)
        sair = Button(self.bchoose_f, text='Sair', width=10, command=self.destroy)
        sair.pack(side=LEFT)

    # Gets the x or o value for player 1
    def choice(self, c):
        if c == 'X':
            self.lp1_choice = [[self.img_x, c], [self.img_o, 'O']]
            self.ltxt.config(text='')  # Remove texto de escolha X ou O
            self.confinew()  # Remove os botões X e O e adiciona o reiniciar e sair
        else:
            self.lp1_choice = [[self.img_o, c], [self.img_x, 'X']]
            self.ltxt.config(text='')  # Remove texto de escolha X ou O
            self.confinew()  # Remove os botões X e O e adiciona o reiniciar e sair

        # Habilita todos os botões
        for but in (self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9):
            but.config(state=NORMAL)

    # Starts the game again, reset all variables to its original values
    def reiniciar(self):
        self.destroy()
        TicTacToe()

    def change_x_o(self, button):
        # print(self.lp1_choice[0][1])
        if button == 'b1':
            if self.checkposition[0] in 'XO':
                messagebox.showwarning('Warning', 'Position already taken!')
            else:
                if self. turn == 0:
                    self.b1.config(image=self.lp1_choice[0][0], width=0, height=0)
                    self.checkposition[0] = self.lp1_choice[0][1]
                    self.turn = 1
                else:
                    self.b1.config(image=self.lp1_choice[1][0], width=0, height=0)
                    self.checkposition[0] = self.lp1_choice[1][1]
                    self.turn = 0
        if button == 'b2':
            if self.checkposition[1] in 'XO':
                messagebox.showwarning('Warning', 'Position already taken!')
            else:
                if self.turn == 0:
                    self.b2.config(image=self.lp1_choice[0][0], width=0, height=0)
                    self.checkposition[1] = self.lp1_choice[0][1]
                    self.turn = 1
                else:
                    self.b2.config(image=self.lp1_choice[1][0], width=0, height=0)
                    self.checkposition[1] = self.lp1_choice[1][1]
                    self.turn = 0
        if button == 'b3':
            if self.checkposition[2] in 'XO':
                messagebox.showwarning('Warning', 'Position already taken!')
            else:
                if self.turn == 0:
                    self.b3.config(image=self.lp1_choice[0][0], width=0, height=0)
                    self.checkposition[2] = self.lp1_choice[0][1]
                    self.turn = 1
                else:
                    self.b3.config(image=self.lp1_choice[1][0], width=0, height=0)
                    self.checkposition[2] = self.lp1_choice[1][1]
                    self.turn = 0
        # Not checked yet
        if button == 'b4':
            if self.checkposition[3] in 'XO':
                messagebox.showwarning('Warning', 'Position already taken!')
            else:
                if self.turn == 0:
                    self.b4.config(image=self.lp1_choice[0][0], width=0, height=0)
                    self.checkposition[3] = self.lp1_choice[0][1]
                    self.turn = 1
                else:
                    self.b4.config(image=self.lp1_choice[1][0], width=0, height=0)
                    self.checkposition[3] = self.lp1_choice[1][1]
                    self.turn = 0
        if button == 'b5':
            if self.checkposition[4] in 'XO':
                messagebox.showwarning('Warning', 'Position already taken!')
            else:
                if self.turn == 0:
                    self.b5.config(image=self.lp1_choice[0][0], width=0, height=0)
                    self.checkposition[4] = self.lp1_choice[0][1]
                    self.turn = 1
                else:
                    self.b5.config(image=self.lp1_choice[1][0], width=0, height=0)
                    self.checkposition[4] = self.lp1_choice[1][1]
                    self.turn = 0
        if button == 'b6':
            if self.checkposition[5] in 'XO':
                messagebox.showwarning('Warning', 'Position already taken!')
            else:
                if self.turn == 0:
                    self.b6.config(image=self.lp1_choice[0][0], width=0, height=0)
                    self.checkposition[5] = self.lp1_choice[0][1]
                    self.turn = 1
                else:
                    self.b6.config(image=self.lp1_choice[1][0], width=0, height=0)
                    self.checkposition[5] = self.lp1_choice[1][1]
                    self.turn = 0
        if button == 'b7':
            if self.checkposition[6] in 'XO':
                messagebox.showwarning('Warning', 'Position already taken!')
            else:
                if self.turn == 0:
                    self.b7.config(image=self.lp1_choice[0][0], width=0, height=0)
                    self.checkposition[6] = self.lp1_choice[0][1]
                    self.turn = 1
                else:
                    self.b7.config(image=self.lp1_choice[1][0], width=0, height=0)
                    self.checkposition[6] = self.lp1_choice[1][1]
                    self.turn = 0
        if button == 'b8':
            if self.checkposition[7] in 'XO':
                messagebox.showwarning('Warning', 'Position already taken!')
            else:
                if self.turn == 0:
                    self.b8.config(image=self.lp1_choice[0][0], width=0, height=0)
                    self.checkposition[7] = self.lp1_choice[0][1]
                    self.turn = 1
                else:
                    self.b8.config(image=self.lp1_choice[1][0], width=0, height=0)
                    self.checkposition[7] = self.lp1_choice[1][1]
                    self.turn = 0
        if button == 'b9':
            if self.checkposition[8] in 'XO':
                messagebox.showwarning('Warning', 'Position already taken!')
            else:
                if self.turn == 0:
                    self.b9.config(image=self.lp1_choice[0][0], width=0, height=0)
                    self.checkposition[8] = self.lp1_choice[0][1]
                    self.turn = 1
                else:
                    self.b9.config(image=self.lp1_choice[1][0], width=0, height=0)
                    self.checkposition[8] = self.lp1_choice[1][1]
                    self.turn = 0

        self.check_winner()

    def check_winner(self):
        # Top horizontal
        if ''.join(self.checkposition[:3]) == 'XXX' or ''.join(self.checkposition[:3]) == 'OOO':
            # messagebox.showinfo('teste', 'ok?')
            if self.turn == 0:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[1][1]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()
            else:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[0][1]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()
        # Middle horizontal
        elif ''.join(self.checkposition[3:6]) == 'XXX' or ''.join(self.checkposition[3:6]) == 'OOO':
            if self.turn == 0:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[1][1]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()
            else:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[0][1]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()
        # Bottom horizontal
        elif ''.join(self.checkposition[6:]) == 'XXX' or ''.join(self.checkposition[6:]) == 'OOO':
            if self.turn == 0:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[1][1]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()
            else:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[0][1]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()

        # Diagonal 1
        elif ''.join(self.checkposition[::4]) == 'XXX' or ''.join(self.checkposition[::4]) == 'OOO':
            if self.turn == 0:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[1][1]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()
            else:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[0][1]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()

        # Diagonal 2
        elif ''.join(self.checkposition[2:7:2]) == 'XXX' or ''.join(self.checkposition[2:7:2]) == 'OOO':
            if self.turn == 0:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[1][1]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()
            else:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[0][1]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()

        # Top Vertical
        elif ''.join(self.checkposition[:7:3]) == 'XXX' or ''.join(self.checkposition[:7:3]) == 'OOO':
            if self.turn == 0:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[1][1]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()
            else:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[0][1]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()
        # Middle vertical
        elif ''.join(self.checkposition[1:8:3]) == 'XXX' or ''.join(self.checkposition[1:8:3]) == 'OOO':
            if self.turn == 0:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[1][1]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()
            else:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[0][1]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()
        # Bottom vertical
        elif ''.join(self.checkposition[2::3]) == 'XXX' or ''.join(self.checkposition[2::3]) == 'OOO':
            if self.turn == 0:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[1][1]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()
            else:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[0][1]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()
        # Otherwise
        elif 'N' not in self.checkposition:
            if messagebox.askquestion('Draw', 'Nobody won. Play again?') == 'yes':
                self.reiniciar()
            else:
                self.destroy()


if __name__ == '__main__':
    app = TicTacToe()

    app.mainloop()
