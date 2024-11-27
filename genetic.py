import random

"""
População: Conjunto de soluções possíveis para o problema.

Cromossomos: Representação das soluções, geralmente em forma de strings (cadeias) de números ou caracteres.

Função de aptidão: Função que avalia a qualidade de cada solução, determinando sua "aptidão" ou "fitness".

Seleção: Processo de escolher os indivíduos mais aptos para reprodução, de acordo com sua aptidão.

Crossover (cruzamento): Operação que combina partes de dois indivíduos para gerar novos indivíduos (filhos).

Mutação: Alteração aleatória de um ou mais genes em um cromossomo, promovendo diversidade.

Substituição: Substituição da população antiga pela nova, ou parte dela

geração: iteração do algoritmo sobre a população

gene: unidade básica de informação
"""

# Dados do problema
pesos = [1.5,1.0,2.0,0.5,0.8,0.4,0.5,0.9,0.6,0.7,1.2,0.5,1.0,0.9,1.1,0.8,0.6]

calorias = [500,300,800,150,600,250,250,400,700,150,300,720,350,330,450,500,240]
peso_maximo = 9

# se um indivídulo estiver dentro do limite de peso, ele poderá ir para a proxima geração
def fitness(individuo):
    peso = calorias_total = 0
    
    for i in range(len(individuo)):
        if individuo[i] == 1:
            peso += pesos[i]  
            calorias_total += calorias[i]  
    
    if peso > peso_maximo:
        return 0  #individuo inválido
    
    # Caso o peso esteja dentro do limite, retorna o total de calorias
    return calorias_total


# inicializando uma população aleatoria 
def inicializar_populacao(tamanho, num_genes):
    populacao = []

    for _ in range(tamanho):
        individuo =[]
        for _ in range(num_genes):
            gene = random.randint(0, 1)
            individuo.append(gene)
        populacao.append(individuo)
    
    return populacao

def selecionar_torneio(populacao, fitnesses):
    # lista de tuplas dos individuos e calorias, ou seja, [((lista de intens) calorias),...]
    individuos_fitness = list(zip(populacao, fitnesses))
    torneio = random.sample(individuos_fitness, 3)
    
    # Encontrando o indivíduo com maior fitness / mais calorias mas com limite de peso.
    vencedor = torneio[0]
    for individuo_fitness in torneio[1:]:
        individuo = individuo_fitness[0]
        fitness = individuo_fitness[1]
        if fitness > vencedor[1]:
            vencedor = individuo_fitness

    return vencedor[0]


# Cruzando a genetica de dois indivíduos 
def crossover(individuo1, individuo2):
    ponto = random.randint(1, len(individuo1) - 1) 
    
    # pegando metade da genetica de cada individuo
    filho1 = individuo1[:ponto] + individuo2[ponto:]
    filho2 = individuo2[:ponto] + individuo1[ponto:]
    
    return filho1, filho2

# mutando aleatoriamente a genetica de um individuo
def mutacao(individuo, taxa_mutacao=0.1):
    for i in range(len(individuo)):
        if random.random() < taxa_mutacao: 
            individuo[i] = 1 - individuo[i]  # Alterna entre 0 e 1
    return individuo

# Algoritmo Genético
def algoritmo_genetico(tamanho_populacao, num_geracoes, taxa_mutacao):
    num_genes = len(pesos)
    populacao = inicializar_populacao(tamanho_populacao, num_genes) #iniciamos a populacao, o objetivo é ter uma variedade de soluções pré definidas, chamos de diversidade genética

    for _ in range(num_geracoes):
        fitnesses = [fitness(ind) for ind in populacao]
        nova_populacao = []

        for _ in range(tamanho_populacao // 2):
            individuo1 = selecionar_torneio(populacao, fitnesses)
            individuo2 = selecionar_torneio(populacao, fitnesses)
            filho1, filho2 = crossover(individuo1, individuo2)
            nova_populacao.append(mutacao(filho1, taxa_mutacao))
            nova_populacao.append(mutacao(filho2, taxa_mutacao))

        populacao = nova_populacao

    # Melhor solução
    fitnesses = [fitness(ind) for ind in populacao]
    melhor_indice = fitnesses.index(max(fitnesses))
    return populacao[melhor_indice], max(fitnesses)

# Executar o algoritmo
for i in range (3):
    melhor_solucao, melhor_fitness = algoritmo_genetico(tamanho_populacao=100, num_geracoes=50, taxa_mutacao=0.05)
    print("Melhor solução:", melhor_solucao)
    print("Total de calorias:", melhor_fitness)
    print("\n")

