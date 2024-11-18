import random

# Dados do problema
pesos = [66.7, 33.6, 80.0, 69.0, 9.6, 45.9, 59.9, 36.2, 73.3, 52.1, 86.0, 68.1, 82.5, 21.8, 76.4, 47.8, 11.3, 38.0, 81.4, 50.1, 43.8, 83.7, 69.4, 83.7, 17.2, 75.0, 97.9, 51.3, 94.8, 84.4, 69.3, 50.4, 56.7, 39.3, 68.9, 23.8, 53.1, 87.2, 5.2, 29.5]

calorias = [4.7, 50.0, 38.4, 23.1, 39.8, 2.6, 16.6, 56.2, 53.7, 7.4, 91.1, 22.6, 60.2, 83.5, 61.7, 38.8, 51.5, 67.0, 12.5, 2.3, 53.3, 4.4, 76.3, 42.5, 26.7, 12.5, 79.2, 61.6, 24.5, 64.3, 76.1, 43.4, 81.3, 8.5, 59.0, 75.1, 57.0, 6.3, 90.1, 53.4]

peso_maximo = 80

# Função de fitness
def fitness(individuo):
    peso = sum(individuo[i] * pesos[i] for i in range(len(individuo)))
    calorias_total = sum(individuo[i] * calorias[i] for i in range(len(individuo)))
    if peso > peso_maximo:
        return 0  # Penaliza soluções inválidas
    return calorias_total

# Inicialização da população
def inicializar_populacao(tamanho, num_genes):
    return [[random.randint(0, 1) for _ in range(num_genes)] for _ in range(tamanho)]

# Seleção por torneio
def selecionar(populacao, fitnesses):
    torneio = random.sample(list(zip(populacao, fitnesses)), 3)
    return max(torneio, key=lambda x: x[1])[0]

# Crossover
def crossover(pai1, pai2):
    ponto = random.randint(1, len(pai1) - 1)
    return pai1[:ponto] + pai2[ponto:], pai2[:ponto] + pai1[ponto:]

# Mutação
def mutacao(individuo, taxa_mutacao=0.1):
    for i in range(len(individuo)):
        if random.random() < taxa_mutacao:
            individuo[i] = 1 - individuo[i]  # Alterna entre 0 e 1
    return individuo

# Algoritmo Genético
def algoritmo_genetico(tamanho_populacao, num_geracoes, taxa_mutacao):
    num_genes = len(pesos)
    populacao = inicializar_populacao(tamanho_populacao, num_genes)

    for _ in range(num_geracoes):
        fitnesses = [fitness(ind) for ind in populacao]
        nova_populacao = []

        for _ in range(tamanho_populacao // 2):
            pai1 = selecionar(populacao, fitnesses)
            pai2 = selecionar(populacao, fitnesses)
            filho1, filho2 = crossover(pai1, pai2)
            nova_populacao.append(mutacao(filho1, taxa_mutacao))
            nova_populacao.append(mutacao(filho2, taxa_mutacao))

        populacao = nova_populacao

    # Melhor solução
    fitnesses = [fitness(ind) for ind in populacao]
    melhor_indice = fitnesses.index(max(fitnesses))
    return populacao[melhor_indice], max(fitnesses)

# Executar o algoritmo
melhor_solucao, melhor_fitness = algoritmo_genetico(tamanho_populacao=100, num_geracoes=50, taxa_mutacao=0.05)
print("Melhor solução:", melhor_solucao)
print("Fitness (calorias):", melhor_fitness)

