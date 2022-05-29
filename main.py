from tkinter import Tk, Button, Entry, Label, messagebox, PhotoImage
from tkinter import StringVar, Frame
import random


class NumberGuessing(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.fila = 0
        self.verde = '#19C065'
        self.naranjado = '#E3B30E'
        self.gris = '#8F8E8C'
        self.texto = StringVar()
        self.texto.trace("w", lambda *args: self.limitar(self.texto))
        self.create_widgets()
        self.numero_aleatoria()

    def create_widgets(self):
        self.frame_titulo = Frame(
            self.master, bg='black', width=400, height=100)
        self.frame_titulo.grid_propagate(0)
        self.frame_titulo.grid(column=0, row=0, sticky='snew')
        self.frame_cuadros = Frame(
            self.master, bg='black', width=400, height=350)
        self.frame_cuadros.grid_propagate(0)
        self.frame_cuadros.grid(column=0, row=1, sticky='snew')
        self.frame_control = Frame(
            self.master, bg='black', width=400, height=100)
        self.frame_control.grid_propagate(0)
        self.frame_control.grid(column=0, row=2, sticky='snew')

        Label(self.frame_titulo,  bg='black', fg='white', text='Number Guessing',
              font=('Arial', 25, 'bold')).pack(side='top')

        self.signal = Label(self.frame_control,  bg='black', fg='white', text='Numero:',
                            font=('Arial', 12))
        self.signal.pack(side='left', expand=True)

        self.numero = Entry(self.frame_control, font=('Arial', 15), justify='center',
                             textvariable=self.texto, fg='black', highlightcolor="green2", highlightthickness=2, width=7)
        self.numero.pack(side='left', expand=True)

        self.enviar = Button(self.frame_control, text='Enviar', bg='gray50', activebackground='green2',
                             fg='white', font=('Arial', 12, 'bold'), command=self.verificar_numero)
        self.enviar.pack(side='left', expand=True)

        self.limpiar = Button(self.frame_control, text='⌫', bg='gray50', activebackground='green2',
                              fg='white', font=('Arial', 12, 'bold'), width=4, command=lambda: self.texto.set(''))
        self.limpiar.pack(side='left', expand=True)

    def limitar(self, texto):
        if len(texto.get()) > 0:
            texto.set(texto.get()[:5])

    def numero_aleatoria(self):
        archivo = open('data.txt', 'r', encoding="utf-8")
        self.lista = archivo.readlines()
        self.p_a = random.choice(self.lista).rstrip('\n')

    def verificar_numero(self):
        numero = self.texto.get().upper()
        if True:
            self.signal['text'] = ''
            print(self.p_a, numero)
            if self.fila <= 6:
                for i, letra in enumerate(numero):
                    self.cuadros = Label(self.frame_cuadros, width=4,  fg='white',
                                         bg=self.gris, text=letra, font=('Geometr706 BlkCn BT', 18, 'bold'))
                    self.cuadros.grid(column=i, row=self.fila, padx=8, pady=5)
                    if letra == self.p_a[i]:
                        self.cuadros['bg'] = self.verde

                    if letra in self.p_a and not letra == self.p_a[i]:
                        self.cuadros['bg'] = self.naranjado

                    if letra not in self.p_a:
                        self.cuadros['bg'] = self.gris

            self.fila = self.fila + 1
            if self.fila <= 6 and self.p_a == numero:
                messagebox.showinfo('GANASTE', 'FELICIDADES')
                self.master.destroy()
                self.master.quit()
            if self.fila == 6 and self.p_a != numero:
                messagebox.showinfo('PERDISTE', 'INTENTALO DE NUEVO')
                self.master.destroy()
                self.master.quit()
        else:
            self.signal['text'] = 'No esta en BBDD'


if __name__ == "__main__":
    ventana = Tk()
    ventana.config(bg='black')
    ventana.geometry('410x440+500+50')
    ventana.resizable(0, 0)
    ventana.title("Python's Team")
    app = NumberGuessing(ventana)
    app.mainloop()
