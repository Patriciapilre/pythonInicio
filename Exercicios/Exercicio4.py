#olá, vamos começar

#exercicio 4:

# Define os valores de a e b
a = 3
b = 5

# Calcula a expressão 2a x 3b
resultado = 2 * a * 3 * b

# Escreve a expressão e o resultado
print("2a x 3b é igual a {resultado}")



# pedir ao utilizador que insira a data de nascimento
data_nascimento = input("Por favor, insira a sua data de nascimento (DD/MM/AAAA): ")

# Aqui divide a string da data em dia, mês e ano com a funcao split
dia, mes, ano = data_nascimento.split('/')

# Converte o dia, mes e ano para um número inteiro
dia = int(dia)
mes = int(mes)
ano_inteiro = int(ano)

# Exibe a data como um número inteiro
print(f"a data de nascimento é: {dia} / {mes} / {ano_inteiro}")