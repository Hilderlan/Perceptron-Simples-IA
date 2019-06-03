from tkinter import *
import simplePerceptron
  
class Application:
	def __init__(self, master, perceptron=None):
		master.title("Perceptron Simples")	# Define o titulo da janela
		master.geometry("400x600+100+100")	# Define o tamanho inicial da janela
		self.fontePadrao = ("Arial", "10")	# Define a fonte padrao adotada no sistema

			# Deficao dos conteiners que constituirao a interface
		self.primeiroContainer = Frame(master)
		self.primeiroContainer["pady"] = 10
		self.primeiroContainer.pack()
  
		self.segundoContainer = Frame(master)
		self.segundoContainer["padx"] = 30
		self.segundoContainer.pack()
  
		self.terceiroContainer = Frame(master)
		self.terceiroContainer["padx"] = 20
		self.terceiroContainer.pack()
  
		self.quartoContainer = Frame(master)
		self.quartoContainer["padx"] = 20
		self.quartoContainer.pack()

		self.nonoContainer = Frame(master)
		self.nonoContainer["padx"] = 20
		self.nonoContainer.pack()

		self.quintoContainer = Frame(master)
		self.quintoContainer["padx"] = 20
		self.quintoContainer.pack()

		self.sextoContainer = Frame(master)
		self.sextoContainer["pady"] = 30
		self.sextoContainer.pack()

		self.testeContainer = Frame(master)
		self.testeContainer["pady"] = 10
		self.testeContainer.pack()

		self.classeContainer = Frame(master)
		self.classeContainer["pady"] = 10
		self.classeContainer.pack()

		self.setimoContainer = Frame(master)
		self.setimoContainer["padx"] = 20
		self.setimoContainer.pack()

		self.oitavoContainer = Frame(master)
		self.oitavoContainer["pady"] = 30
		self.oitavoContainer.pack()

		self.jogadorContainer = Frame(master)
		self.jogadorContainer["pady"] = 30
		self.jogadorContainer.pack()

			# Preenchimento dos conteiners com seus atributos  
		self.titulo = Label(self.primeiroContainer, text="Insira as entradas para o treinamento")
		self.titulo["font"] = ("Arial", "14", "bold")
		self.titulo.pack()
  
		self.entrada1 = Label(self.segundoContainer,text="Entrada 1                ", font=self.fontePadrao, width=25)
		self.entrada1.pack(side=LEFT)
  
		self.in1 = Entry(self.segundoContainer)
		self.in1["width"] = 7
		self.in1["font"] = self.fontePadrao
		self.in1.pack(side=LEFT)
		self.in1.focus_force()
  
		self.entrada2 = Label(self.terceiroContainer, text="Entrada 2                ", font=self.fontePadrao, width=25)
		self.entrada2.pack(side=LEFT)
  
		self.in2 = Entry(self.terceiroContainer)
		self.in2["width"] = 7
		self.in2["font"] = self.fontePadrao
		self.in2.pack(side=LEFT)

		self.pesoBias = Label(self.quartoContainer, text="Peso do Bias          ", font=self.fontePadrao, width=25)
		self.pesoBias.pack(side=LEFT)
  
		self.bias = Entry(self.quartoContainer)
		self.bias["width"] = 7
		self.bias["font"] = self.fontePadrao
		self.bias.pack(side=LEFT)

		self.taxaAprendizado = Label(self.nonoContainer, text="Taxa de Aprendizado", font=self.fontePadrao, width=25)
		self.taxaAprendizado.pack(side=LEFT)
  
		self.taxa = Entry(self.nonoContainer)
		self.taxa["width"] = 7
		self.taxa["font"] = self.fontePadrao
		self.taxa.pack(side=LEFT)

		self.limiarAtivacao = Label(self.quintoContainer, text="Limiar de ativacao   ", font=self.fontePadrao, width=25)
		self.limiarAtivacao.pack(side=LEFT)
  
		self.limiar = Entry(self.quintoContainer)
		self.limiar["width"] = 7
		self.limiar["font"] = self.fontePadrao
		self.limiar.pack(side=LEFT)
  		
  			# Botao cuja funcao eh treinar a rede
		self.treinarRede = Button(self.sextoContainer)
		self.treinarRede["text"] = "Treinar rede"
		self.treinarRede["font"] = ("Calibri", "8")
		self.treinarRede["width"] = 12
		self.treinarRede["command"] = self.treinar
		self.treinarRede.pack()

		self.testeC = Label(self.testeContainer, text="Insira as entradas para o teste")
		self.testeC["font"] = ("Arial", "14", "bold")
		self.testeC.pack()

		self.classeC = Label(self.classeContainer, text="00  -  Neymar		\n01  -  Gabriel		\n10  -  Federer		\n11  -  Nadal		")
		self.classeC["width"] = 30
		self.classeC["font"] = ("Arial", "10")
		self.classeC.pack()

		self.testarEntrada = Label(self.setimoContainer, text="Entrada para teste    ", font=self.fontePadrao, width=25)
		self.testarEntrada.pack(side=LEFT)
  
		self.test = Entry(self.setimoContainer)
		self.test["width"] = 7
		self.test["font"] = self.fontePadrao
		self.test.pack(side=LEFT)

			# Botao cuja funcao eh testar a rede
		self.testarRede = Button(self.oitavoContainer)
		self.testarRede["text"] = "Testar rede"
		self.testarRede["font"] = ("Calibri", "8")
		self.testarRede["width"] = 12
		self.testarRede["command"] = self.testar
		self.testarRede.pack()

		self.jogador = Label(self.jogadorContainer, text="", font=("Arial", "12", "bold"), width=40)
		self.jogador.pack(side=LEFT)

	def treinar(self):
		# Amostras que serao treinadas no Simple Perceptron
		amostras = [[1.0, 1.0], # Nadal 	(Tenis)
					[0.0, 1.0], # Gabriel	(Futebol)
					[1.0, 0.0],	# Federer	(Tenis)
					[0.0, 0.0]	# Neymar	(Futebol)
					]

		# Saidas desejadas de cada uma das amostras definidas
		saidas = [1, 0, 1, 0]	# Respectivamente: tenis, futebol, tenis, futebol

		pesos = []

		pesos.append(float(self.in1.get()))

		pesos.append(float(self.in2.get()))
		
		peso_bias = int(float(self.bias.get()))

		taxa_aprendizado = float(self.taxa.get())

		limiar = float(self.limiar.get())

		perceptron = simplePerceptron.Simple_Perceptron(amostras=amostras, saidas=saidas, pesos=pesos, taxa_aprendizado=taxa_aprendizado, epocas=1000, peso_bias=peso_bias, limiar=limiar)

		self.perceptron = perceptron

		print("########################### Simple Perceptron ########################\n\n######################## TREINANDO A REDE ############################\n")

		self.perceptron.treinar()

		self.treinarRede["text"] = "Rede treinada!"

		print("\n\n######################## TREINAMENTO FINALIZADO ############################\n")

	def testar(self):
		dict = {"00": "Neymar", "01": "Gabriel", "10": "Federer", "11": "Nadal"}

		print("\n#################### FASE DE TESTES ####################\n")

		stringTeste = self.test.get()
			
		listInput = [int(stringTeste[0]), int(stringTeste[1])]

		self.jogador["text"] = self.perceptron.testar(listInput, dict[str(stringTeste[0]) + str(stringTeste[1])])

def inicializar():
	root = Tk()
	app = Application(root)
	root.mainloop()