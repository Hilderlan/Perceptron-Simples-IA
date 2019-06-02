#############################################################################################
#	Universidade Federal do Piaui - UFPI													#
#	Bacharelado em Ciencia da Computacao													#
#	Disciplina: Interligencia Artificial - IA												#
#	Componentes: Hilderlan, Jose Chaves e Lucas Vinicius									#
#																							#
#	Implementacao do Perceptron de camada unica ou Perceptron simples (Simple perceptron)	#
#############################################################################################

import random, copy
import os

class Simple_Perceptron:

	# Construtor da classe, com valores padroes caso nao sejam setados
	def __init__(self, amostras, saidas, pesos, taxa_aprendizado=0.25, epocas=1000, peso_bias=0, limiar=0):

		self.amostras = amostras
		self.saidas = saidas # Saidas desejadas de cada uma das entradas
		self.taxa_aprendizado = taxa_aprendizado # Taxa de aprendizado ou Neta
		self.epocas = epocas
		self.peso_bias = peso_bias # Peso do bias que eh inserido no inicio da lista de entradas
		self.limiar = limiar # Limiar de ativacao utilizado pela funcao de ativacao para definir a classe do jogador
		self.quant_entradas = len(amostras[0]) # Quantidade de elementos presentes em cada entrada
		self.pesos = pesos

	def treinar(self):
		
		# Adiciona 1 para cada uma das amostras, bem no inicio, referente ao valor do bias que eh fixo
		for amostra in self.amostras:
			amostra.insert(0, 1)	# No caso, cada entrada passara a ter 3 valores, (1, v1, v2), onde o 1 eh o valor do Bias

		# Insere o peso do Bias no inicio da lista de pesos
		self.pesos.insert(0, self.peso_bias)

		# Contador de epocas
		num_epocas = 0

		while True:
			
			print(f"########### Epoca {num_epocas} #############\n")

			erro = False # Ja que erro eh uma das condicoes de parada

			# Para cada uma das entradas (amostras de treinamento)
			for i in range(len(amostras)):
    				
				print(f"\n-> Para a entrada {amostras[i]}\n")

				u = 0	# Parametro para a funcao de ativacao

				for j in range(self.quant_entradas + 1):
					u += self.pesos[j] * self.amostras[i][j]	# Somatorio de cada entrada multiplicada pelo seu respectivo peso

				print(f"      Somatorio: {u}")

				y = self.funcao_de_ativacao(u)	# Aplica a funcao de ativacao
				print(f"      Valor esperado: {self.saidas[i]}\n      Funcao de ativacao: {y}")

				# Verifica se a saída da rede (obtida) é diferente da saída desejada
				erro_aux = self.saidas[i] - y	# Saida desejada - saida atual (obtida)

				if(erro_aux == 0):
					print("      Erro inexistente.")
				else:
					print(f"      Existe erro: {erro_aux}, ajustando os pesos...")

				if erro_aux != 0:	# Significa que para os pesos em questao a rede nao acertou a classe, entao, os mesmos devem ser atualizados
					for j in range(self.quant_entradas + 1):
						# O novo peso, sera o peso atual, somado com a multiplicacao entre o neta, a entrada e o erro obtido
						self.pesos[j] = self.pesos[j] + self.taxa_aprendizado*erro_aux*self.amostras[i][j]
					
					print(f"      Novos pesos: {self.pesos}")

					erro = True # Para continuar testando para as outras entradas

			num_epocas += 1 # A quantidade de epocas eh atualizada, ja que todas as entradas foram apresentadas para a rede

			print("\n")

			# O Simple Perceptron para quando nao existir erro, o que significa que a rede foi devidamente treinada, ou quando atingir uma quantidade pre-definida de epocas
			if num_epocas > self.epocas or not erro:
				break

		self.epocas = num_epocas # Seta a quantidade de epocas que foram necessarias para treinar a rede

		print(f"Quantidade de epocas necessarias: {num_epocas}\n\nPesos finais: {self.pesos}")


	def testar(self, amostra, jogador):
    		
		# Insere 0 no inicio de cada entrada novamente
		amostra.insert(0, 1)

		# Faz o uso da lista de pesos que foi obtida por meio do treinamento da rede
		u = 0
		for i in range(self.quant_entradas + 1):
			u += self.pesos[i] * amostra[i]

		y = self.funcao_de_ativacao(u)

		# Verifica a qual classe o jogador pertence
		if y == 0:	 # Futebol
			print(f'\n  -> O jogador {jogador} pertence a classe Futebol!')
		elif y == 1: # Tenis
			print(f'\n  -> O jogador {jogador} pertence a classe Tenis!')


	# Funcao de ativacao: degrau
	def funcao_de_ativacao(self, u):
		return 1 if u >= self.limiar else 0

if __name__ == "__main__":
    	
	# Amostras que serao treinadas no Simple Perceptron
	amostras = [[1.0, 1.0], # Nadal 	(Tenis)
				[0.0, 1.0], # Gabriel	(Futebol)
				[1.0, 0.0],	# Federer	(Tenis)
				[0.0, 0.0]	# Neymar	(Futebol)
				]

	dict = {"00": "Neymar", "01": "Gabriel", "10": "Federer", "11": "Nadal"}

	# Saidas desejadas de cada uma das amostras definidas
	saidas = [1, 0, 1, 0]	# Respectivamente: tenis, futebol, tenis, futebol

	testes = copy.deepcopy(amostras)

	pesos = []

	print("########################### Simple Perceptron ########################\n")

	for i in range(len(amostras[0])):
		pesos.append(float(input(f"\nDigite o peso da entrada {i+1}: ")))
	
	peso_bias = float(input("\nDigite o peso do Bias: "))

	taxa_aprendizado = float(input("\nDigite a taxa de aprendizado (Neta): "))

	limiar = float(input("\nDigite o limiar de ativacao: "))
	
	simplePerceptron = Simple_Perceptron(amostras=amostras, saidas=saidas, pesos=pesos, taxa_aprendizado=taxa_aprendizado, epocas=1000, peso_bias=peso_bias, limiar=limiar)

	print("\n######################## TREINANDO A REDE ############################\n")

	simplePerceptron.treinar()

	print("\n\n######################## TREINAMENTO FINALIZADO ############################\n")
	print("\n\n#################### FASE DE TESTES ####################\n")

	while(True):

		for k,v in dict.items():
			print(k, " - ", v)

		inp = input("\nEscolha a entrada: ")
		
		listInput = [int(inp[0]), int(inp[1])]

		simplePerceptron.testar(listInput, dict[str(inp[0]) + str(inp[1])])

		resp = input("\nDeseja fazer outro teste? < y : n >")

		if(resp == 'n' or resp == 'N'):
			break

		os.system('cls' if os.name == 'nt' else 'clear')
		print("\n\n#################### FASE DE TESTES ####################\n")

	print("\n\n##########################################################")