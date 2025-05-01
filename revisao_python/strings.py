'''
O que são strings?
Começaremos explorando as strings. As strings são sequências de caracteres que utilizamos para representar algum texto. 
Elas podem ser delimitadas por aspas simples ou duplas, a depender da preferência ou do contexto de uso. Além disso, podemos utilizar aspas 
triplas para representar strings maiores, que incluem múltiplas linhas e quebras de linha.

'''
mensagem = 'Olá, mundo!'
mensagem = "Python é incrível!"

texto = """Essa é uma string
que pode ter múltiplas
linhas."""




''' Aplicaçao de uma f string no codigo 
Além desses métodos de manipulação, podemos incluir uma expressão ou variável em uma string. Para isso, usamos as f-strings do Python, que possuem a 
sintaxe da letra f e, entre aspas duplas e chaves, inserimos a variável desejada. Vamos entender isso melhor com um exemplo de código?
'''

estudante = "Pedro"
nota = 10;
mensagem= f'{estudante} tirou {nota} de nota na prova de Matematica!'

print(mensagem)


'''  Indexação de strings
A indexação permite acessar caracteres individuais de uma string atraves de seu indice, começanmdo de 0 paera o primeiro caractere
Para acessar caracteres a partir do final, usase indices negativos, onde -1 é o último caractere.
'''

texto = "Python"

print(texto[5])
print(texto[-1])

''' 
A operação de slicing (fatiamento) permite extrair um pedaço da string.
A sintaxe do slicing envolve uma string seguida de abertura e fechamento de colchetes, que envolvem um valor inicial separado de um valor final por dois pontos (:). 
Também podemos definir um passo, que é o intervalo entre os índices, sendo essa uma informação opcional.
O índice de fim não está incluso na string final.
'''

# string[início:fim:passo]

texto = "Python"

print(texto[1:4])
print(texto[:3])
print(texto[::2])

'''
Conhecendo o operador in
Outro operador interessante é o in, que verifica se uma substring está presente em uma string.

'''

texto = "Python"

print("Py" in texto)

print("Java" in texto)

'''
Conhecendo o método startswith()
O método startswith() verifica se a string começa com uma substring específica, retornando True ou False como resposta.

'''

texto = "Python"

print(texto.startswith("Py"))

print(texto.startswith("py"))

'''
Conhecendo o método endswith()
Por fim, o método endswith() verifica se a string termina com uma substring específica.

No exemplo de código abaixo, verificamos se a string termina com "on", resultando em True. Da mesma forma, verificamos se ela termina com "ton", resultando em False.

'''
texto = "Python"

print(texto.endswith("on"))

print(texto.endswith("ton"))
