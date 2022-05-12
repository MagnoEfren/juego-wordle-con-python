# Juego Wordle
# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren


from tkinter import  Tk, Button, Entry, Label, messagebox, PhotoImage
from tkinter import  StringVar,Frame
import random

class Wordle(Frame):
	def __init__(self, master):
		super().__init__( master)
		self.fila = 0
		self.verde = '#19C065'
		self.naranjado = '#E3B30E'
		self.gris = '#8F8E8C'
		self.texto = StringVar()
		self.texto.trace("w", lambda *args: self.limitar(self.texto))
		self.create_widgets()
		self.palabra_aleatoria()

	def create_widgets(self):
		self.frame_titulo = Frame(self.master, bg='black', width=400, height=100)
		self.frame_titulo.grid_propagate(0)
		self.frame_titulo.grid(column=0, row=0, sticky='snew')
		self.frame_cuadros = Frame(self.master, bg='black', width=400, height=350)
		self.frame_cuadros.grid_propagate(0)
		self.frame_cuadros.grid(column=0, row=1, sticky='snew')
		self.frame_control = Frame(self.master, bg='black', width=400, height=100)
		self.frame_control.grid_propagate(0)
		self.frame_control.grid(column=0, row=2, sticky='snew')

		Label(self.frame_titulo,  bg= 'black',fg='white', text= 'WORDLE', 
			font=('Arial',25,'bold')).pack(side='top')

		self.signal = Label(self.frame_control,  bg= 'black',fg='white', text= 'Señal', 
			font=('Arial',12))
		self.signal.pack(side= 'left', expand=True)

		self.palabra = Entry(self.frame_control, font=('Arial',15), justify = 'center', 
			textvariable = self.texto,fg='black',highlightcolor= "green2", highlightthickness=2, width=7)
		self.palabra.pack(side= 'left', expand=True)

		self.enviar = Button(self.frame_control, text= 'Enviar', bg='gray50',activebackground='green2',
		 fg = 'white', font=('Arial', 12,'bold'), command=self.verificar_palabra)
		self.enviar.pack(side= 'left', expand=True)

		self.limpiar = Button(self.frame_control, text= '⌫', bg='gray50',activebackground='green2',
		 fg = 'white', font=('Arial', 12,'bold'), width=4, command= lambda:self.texto.set(''))
		self.limpiar.pack(side= 'left', expand=True)

	def limitar(self, texto):
	    if len(texto.get()) > 0:
	        texto.set(texto.get()[:5])

	def palabra_aleatoria(self):
		archivo = open('data.txt','r',encoding="utf-8") #leer la Ñ
		self.lista = archivo.readlines()
		self.p_a =  random.choice(self.lista).rstrip('\n')  

	def verificar_palabra(self):
		palabra = self.texto.get().upper()
		x = list(filter(lambda x: palabra in x, self.lista)) #[i for i in lista if palabra in i]
		if len(x)==1 and len(palabra)==5:
			self.signal['text'] = ''
			print(self.p_a, palabra)			
			if self.fila<=6:					
				for i, letra in enumerate(palabra):
					self.cuadros = Label(self.frame_cuadros, width=4,  fg='white' ,
						bg=self.gris, text= letra, font=('Geometr706 BlkCn BT',25, 'bold'))
					self.cuadros.grid(column=i, row = self.fila , padx =5, pady =5)
					if letra == self.p_a[i]:
						self.cuadros['bg']= self.verde

					if letra in self.p_a and not letra== self.p_a[i]:
						self.cuadros['bg']= self.naranjado

					if letra not in self.p_a:
						self.cuadros['bg']= self.gris

			self.fila = self.fila + 1
			if self.fila<=6 and self.p_a == palabra:
				messagebox.showinfo('GANASTE', 'FELICIDADES')
				self.master.destroy()
				self.master.quit()				
			if self.fila==6 and self.p_a != palabra:
				messagebox.showinfo('PERDISTE', 'INTENTALO DE NUEVO')
				self.master.destroy()
				self.master.quit()
		else:
			self.signal['text'] = 'No esta en BBDD'

if __name__ == "__main__":
	ventana = Tk()
	ventana.config(bg='black')
	ventana.call('wm', 'iconphoto', ventana._w, PhotoImage(file='logo.png'))
	ventana.geometry('410x440+500+50')
	ventana.resizable(0,0)
	ventana.title('Wordle')
	app = Wordle(ventana)
	app.mainloop()
