import tkinter
from tkinter import *

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
        self.check_position = ['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]
        # Frame linha 1
        self.button_frame1 = Frame(self, background='black')
        self.button_frame1.pack()

        # Buttons
        self.b1 = Button(self.button_frame1, width=4, height=2, border=1, font=('Verdana', 15),
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

        # Set all buttons to DISABLED state and alson change there color at once
        for but in (self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9):
            but.config(state=DISABLED, background='gray')

        self.choose_x_o_frame = Frame(self, background='black')
        self.choose_x_o_frame.pack()

        self.bchoose_f = Frame(self, background='black')
        self.bchoose_f.pack()
        self.ltxt = Label(self.choose_x_o_frame, text='Você quer ser X ou O?', font=('Verdana', 10),
                          bg='black', fg='white')
        self.ltxt.pack(anchor=N)
        self.b_x = Button(self.bchoose_f, text='X', width=5, font=('Verdana', 10), command=lambda: self.choice('X'),
                          background='gray')
        self.b_x.pack(side=LEFT, padx=5)
        self.b_o = Button(self.bchoose_f, text='O', width=5, font=('Verdana', 10), command=lambda: self.choice('O'),
                          background='gray')
        self.b_o.pack(side=LEFT)

        self.turn = 0

    # Function to change Button X and O to Restart and Exit
    def confinew(self):
        self.b_x.destroy()
        self.b_o.destroy()
        reiniciar = Button(self.bchoose_f, text='Reiniciar', width=10, command=self.reiniciar, background='gray')
        reiniciar.pack(side=LEFT, padx=5)
        sair = Button(self.bchoose_f, text='Sair', width=10, command=self.destroy, background='gray')
        sair.pack(side=LEFT)

    # Gets the x or o value for player 1
    def choice(self, c):
        if c == 'X':
            self.lp1_choice = [c, 'O']
            self.ltxt.config(text='')
            self.confinew()
        else:
            self.lp1_choice = [c, 'X']
            self.ltxt.config(text='')
            self.confinew()

        for but in (self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9):
            but.config(state=NORMAL)

    # Starts the game again, reset all variables to its original values
    def reiniciar(self):
        self.destroy()
        TicTacToe()

    # It change the values X and O when a player plays
    def change_x_o(self, button):
        if button == 'b1':
            if self.check_position[0] in 'XO':
                messagebox.showwarning('Warning', 'Position already taken!')
            else:
                if self. turn == 0:
                    self.b1.config(text=f'{self.lp1_choice[0]}')
                    self.check_position[0] = self.lp1_choice[0]
                    print(self.check_position)
                    self.turn = 1
                else:
                    self.b1.config(text=f'{self.lp1_choice[1]}')
                    self.check_position[0] = self.lp1_choice[1]
                    print(self.check_position)
                    self.turn = 0
        if button == 'b2':
            if self.check_position[1] in 'XO':
                messagebox.showwarning('Warning', 'Position already taken!')
            else:
                if self. turn == 0:
                    self.b2.config(text=f'{self.lp1_choice[0]}')
                    self.check_position[1] = self.lp1_choice[0]
                    print(self.check_position)
                    self.turn = 1
                else:
                    self.b2.config(text=f'{self.lp1_choice[1]}')
                    self.check_position[1] = self.lp1_choice[1]
                    print(self.check_position)
                    self.turn = 0

        if button == 'b3':
            if self.check_position[2] in 'XO':
                messagebox.showwarning('Warning', 'Position already taken!')
            else:
                if self. turn == 0:
                    self.b3.config(text=f'{self.lp1_choice[0]}')
                    self.check_position[2] = self.lp1_choice[0]
                    print(self.check_position)
                    self.turn = 1
                else:
                    self.b3.config(text=f'{self.lp1_choice[1]}')
                    self.check_position[2] = self.lp1_choice[1]
                    print(self.check_position)
                    self.turn = 0

        if button == 'b4':
            if self.check_position[3] in 'XO':
                messagebox.showwarning('Warning', 'Position already taken!')
            else:
                if self. turn == 0:
                    self.b4.config(text=f'{self.lp1_choice[0]}')
                    self.check_position[3] = self.lp1_choice[0]
                    print(self.check_position)
                    self.turn = 1
                else:
                    self.b4.config(text=f'{self.lp1_choice[1]}')
                    self.check_position[3] = self.lp1_choice[1]
                    print(self.check_position)
                    self.turn = 0

        if button == 'b5':
            if self.check_position[4] in 'XO':
                messagebox.showwarning('Warning', 'Position already taken!')
            else:
                if self. turn == 0:
                    self.b5.config(text=f'{self.lp1_choice[0]}')
                    self.check_position[4] = self.lp1_choice[0]
                    print(self.check_position)
                    self.turn = 1
                else:
                    self.b5.config(text=f'{self.lp1_choice[1]}')
                    self.check_position[4] = self.lp1_choice[1]
                    print(self.check_position)
                    self.turn = 0

        if button == 'b6':
            if self.check_position[5] in 'XO':
                messagebox.showwarning('Warning', 'Position already taken!')
            else:
                if self. turn == 0:
                    self.b6.config(text=f'{self.lp1_choice[0]}')
                    self.check_position[5] = self.lp1_choice[0]
                    print(self.check_position)
                    self.turn = 1
                else:
                    self.b6.config(text=f'{self.lp1_choice[1]}')
                    self.check_position[5] = self.lp1_choice[1]
                    print(self.check_position)
                    self.turn = 0

        if button == 'b7':
            if self.check_position[6] in 'XO':
                messagebox.showwarning('Warning', 'Position already taken!')
            else:
                if self. turn == 0:
                    self.b7.config(text=f'{self.lp1_choice[0]}')
                    self.check_position[6] = self.lp1_choice[0]
                    print(self.check_position)
                    self.turn = 1
                else:
                    self.b7.config(text=f'{self.lp1_choice[1]}')
                    self.check_position[6] = self.lp1_choice[1]
                    print(self.check_position)
                    self.turn = 0

        if button == 'b8':
            if self.check_position[7] in 'XO':
                messagebox.showwarning('Warning', 'Position already taken!')
            else:
                if self. turn == 0:
                    self.b8.config(text=f'{self.lp1_choice[0]}')
                    self.check_position[7] = self.lp1_choice[0]
                    print(self.check_position)
                    self.turn = 1
                else:
                    self.b8.config(text=f'{self.lp1_choice[1]}')
                    self.check_position[7] = self.lp1_choice[1]
                    print(self.check_position)
                    self.turn = 0

        if button == 'b9':
            if self.check_position[8] in 'XO':
                messagebox.showwarning('Warning', 'Position already taken!')
            else:
                if self. turn == 0:
                    self.b9.config(text=f'{self.lp1_choice[0]}')
                    self.check_position[8] = self.lp1_choice[0]
                    print(self.check_position)
                    self.turn = 1
                else:
                    self.b9.config(text=f'{self.lp1_choice[1]}')
                    self.check_position[8] = self.lp1_choice[1]
                    print(self.check_position)
                    self.turn = 0

        self.check_winner()

    # Check if there's a winner
    def check_winner(self):
        # Top horizontal
        if ''.join(self.check_position[:3]) == 'XXX' or ''.join(self.check_position[:3]) == 'OOO':
            if self.turn == 0:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[1]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()
            else:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[0]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()
        # Middle horizontal
        elif ''.join(self.check_position[3:6]) == 'XXX' or ''.join(self.check_position[3:6]) == 'OOO':
            if self.turn == 0:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[1]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()
            else:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[0]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()
        # Bottom horizontal
        elif ''.join(self.check_position[6:]) == 'XXX' or ''.join(self.check_position[6:]) == 'OOO':
            if self.turn == 0:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[1]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()
            else:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[0]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()

        # Diagonal 1
        elif ''.join(self.check_position[::4]) == 'XXX' or ''.join(self.check_position[::4]) == 'OOO':
            if self.turn == 0:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[1]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()
            else:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[0]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()

        # Diagonal 2
        elif ''.join(self.check_position[2:7:2]) == 'XXX' or ''.join(self.check_position[2:7:2]) == 'OOO':
            if self.turn == 0:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[1]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()
            else:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[0]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()

        # Top Vertical
        elif ''.join(self.check_position[:7:3]) == 'XXX' or ''.join(self.check_position[:7:3]) == 'OOO':
            if self.turn == 0:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[1]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()
            else:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[0]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()
        # Middle vertical
        elif ''.join(self.check_position[1:8:3]) == 'XXX' or ''.join(self.check_position[1:8:3]) == 'OOO':
            if self.turn == 0:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[1]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()
            else:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[0]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()
        # Bottom vertical
        elif ''.join(self.check_position[2::3]) == 'XXX' or ''.join(self.check_position[2::3]) == 'OOO':
            if self.turn == 0:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[1]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()
            else:
                if messagebox.askquestion('Winner', f'{self.lp1_choice[0]} Won the match. Play again?') == 'yes':
                    self.reiniciar()
                else:
                    self.destroy()
        # Otherwise
        elif 'N' not in self.check_position:
            if messagebox.askquestion('Draw', 'Nobody won. Play again?') == 'yes':
                self.reiniciar()
            else:
                self.destroy()


if __name__ == '__main__':
    app = TicTacToe()

    app.mainloop()
