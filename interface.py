from tkinter import *
import simplePerceptron
  
class Application:
	def __init__(self, master, perceptron=None):
		self.fontePadrao = ("Arial", "10")
		self.primeiroContainer = Frame(master)
		self.primeiroContainer["pady"] = 10
		self.primeiroContainer.pack()
  
		self.segundoContainer = Frame(master)
		self.segundoContainer["padx"] = 20
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
		self.sextoContainer["pady"] = 10
		self.sextoContainer.pack()

		self.setimoContainer = Frame(master)
		self.setimoContainer["padx"] = 20
		self.setimoContainer.pack()

		self.oitavoContainer = Frame(master)
		self.oitavoContainer["pady"] = 10
		self.oitavoContainer.pack()
  
		self.titulo = Label(self.primeiroContainer, text="Insira as entradas para o treinamento")
		self.titulo["font"] = ("Arial", "10", "bold")
		self.titulo.pack()
  
		self.entrada1 = Label(self.segundoContainer,text="Entrada 1", font=self.fontePadrao)
		self.entrada1.pack(side=LEFT)
  
		self.in1 = Entry(self.segundoContainer)
		self.in1["width"] = 10
		self.in1["font"] = self.fontePadrao
		self.in1.pack(side=LEFT)
  
		self.entrada2 = Label(self.terceiroContainer, text="Entrada 2", font=self.fontePadrao)
		self.entrada2.pack(side=LEFT)
  
		self.in2 = Entry(self.terceiroContainer)
		self.in2["width"] = 10
		self.in2["font"] = self.fontePadrao
		self.in2.pack(side=LEFT)

		self.pesoBias = Label(self.quartoContainer, text="Peso do Bias", font=self.fontePadrao)
		self.pesoBias.pack(side=LEFT)
  
		self.bias = Entry(self.quartoContainer)
		self.bias["width"] = 10
		self.bias["font"] = self.fontePadrao
		self.bias.pack(side=LEFT)

		self.taxaAprendizado = Label(self.nonoContainer, text="Taxa de Aprendizado", font=self.fontePadrao)
		self.taxaAprendizado.pack(side=LEFT)
  
		self.taxa = Entry(self.nonoContainer)
		self.taxa["width"] = 10
		self.taxa["font"] = self.fontePadrao
		self.taxa.pack(side=LEFT)

		self.limiarAtivacao = Label(self.quintoContainer, text="Limiar de ativacao", font=self.fontePadrao)
		self.limiarAtivacao.pack(side=LEFT)
  
		self.limiar = Entry(self.quintoContainer)
		self.limiar["width"] = 10
		self.limiar["font"] = self.fontePadrao
		self.limiar.pack(side=LEFT)
  
		self.treinarRede = Button(self.sextoContainer)
		self.treinarRede["text"] = "Treinar"
		self.treinarRede["font"] = ("Calibri", "8")
		self.treinarRede["width"] = 12
		self.treinarRede["command"] = self.treinar
		self.treinarRede.pack()

		self.testarEntrada = Label(self.setimoContainer, text="Entrada para teste", font=self.fontePadrao)
		self.testarEntrada.pack(side=LEFT)
  
		self.test = Entry(self.setimoContainer)
		self.test["width"] = 10
		self.test["font"] = self.fontePadrao
		self.test.pack(side=LEFT)

		self.testarRede = Button(self.oitavoContainer)
		self.testarRede["text"] = "Testar rede"
		self.testarRede["font"] = ("Calibri", "8")
		self.testarRede["width"] = 12
		self.testarRede["command"] = self.testar
		self.testarRede.pack()
  
    #Método verificar senha
	def verificaSenha(self):
 		usuario = self.nome.get()
  #      senha = self.senha.get()
   #     if usuario == "usuariodevmedia" and senha == "dev":
    #        self.mensagem["text"] = "Autenticado"
     #   else:
      #      self.mensagem["text"] = "Erro na autenticação"

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

		print(type(pesos[0]))
		
		peso_bias = int(float(self.bias.get()))

		print(peso_bias)

		taxa_aprendizado = float(self.taxa.get())

		limiar = float(self.limiar.get())

		perceptron = simplePerceptron.Simple_Perceptron(amostras=amostras, saidas=saidas, pesos=pesos, taxa_aprendizado=taxa_aprendizado, epocas=1000, peso_bias=peso_bias, limiar=limiar)

		self.perceptron = perceptron

		print("########################### Simple Perceptron ########################\n")
		print("\n######################## TREINANDO A REDE ############################\n")

		self.perceptron.treinar()

		print("\n\n######################## TREINAMENTO FINALIZADO ############################\n")

	def testar(self):
		dict = {"00": "Neymar", "01": "Gabriel", "10": "Federer", "11": "Nadal"}

		print("\n#################### FASE DE TESTES ####################\n")

		for k,v in dict.items():
			print(k, " - ", v)

		stringTeste = self.test.get()

		print(stringTeste)
			
		listInput = [int(stringTeste[0]), int(stringTeste[1])]

		self.perceptron.testar(listInput, dict[str(stringTeste[0]) + str(stringTeste[1])])

def inicializar():
	root = Tk()
	app = Application(root)
	root.mainloop()