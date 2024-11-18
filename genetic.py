import random

# Dados do problema
pesos = [1.5,1.0,2.0,0.5,0.8,0.4,0.5,0.9,0.6,0.7,1.2,0.5,1.0,0.9,1.1,0.8,0.6]

calorias = [500,300,800,150,600,250,250,400,700,150,300,720,350,330,450,500,240]
peso_maximo = 9

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
for i in range (6):
    melhor_solucao, melhor_fitness = algoritmo_genetico(tamanho_populacao=100, num_geracoes=50, taxa_mutacao=0.05)
    print("Melhor solução:", melhor_solucao)
    print("Fitness (calorias):", melhor_fitness)
    print("\n")

