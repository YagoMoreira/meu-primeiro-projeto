# Projeto de Análise de Dados com Entrada do Usuário e Gráfico
# Autor: Yago Moreira

import matplotlib.pyplot as plt

# Entrada de dados pelo usuário
entrada = input("Digite valores separados por vírgula (ex: 7,8,9,10): ")

# Convertendo para lista de números
dados = [float(x.strip()) for x in entrada.split(",")]

# Cálculos
media = sum(dados) / len(dados)
maior = max(dados)
menor = min(dados)

# Resultados
print("\nAnálise de Dados")
print("----------------")
print(f"Dados: {dados}")
print(f"Média: {media:.2f}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")

# Classificação
if media >= 7:
    print("Resultado: Dados dentro do padrão esperado")
else:
    print("Resultado: Atenção aos dados")

# Gráfico simples
plt.figure()
plt.plot(dados, marker='o')
plt.title("Visualização dos Dados")
plt.xlabel("Índice")
plt.ylabel("Valor")
plt.grid()

# Mostrar gráfico
plt.show()
