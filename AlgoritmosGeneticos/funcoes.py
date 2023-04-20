import random

###############################################################################
#                                   Suporte                                   #
###############################################################################


def distancia_entre_dois_pontos(a, b):
    """Computa a distância Euclidiana entre dois pontos em R^2
    Args:
      a: lista contendo as coordenadas x e y de um ponto.
      b: lista contendo as coordenadas x e y de um ponto.
    Returns:
      Distância entre as coordenadas dos pontos `a` e `b`.
    """

    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]

    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)

    return dist


def cria_cidades(n):
    """Cria um dicionário aleatório de cidades com suas posições (x,y).
    Args:
      n: inteiro positivo
        Número de cidades que serão visitadas pelo caixeiro.
    Returns:
      Dicionário contendo o nome das cidades como chaves e a coordenada no plano
      cartesiano das cidades como valores.
    """

    cidades = {}

    for i in range(n):
        cidades[f"Cidade {i}"] = (random.random(), random.random()) #criamos por tuplas, para nao mudar onde estão as cidades durante o provblema

    return cidades


# NOVIDADE
def computa_mochila(individuo, objetos, ordem_dos_nomes):
    """Computa o valor total e peso total de uma mochila
    Args:
      individiuo:
        Lista binária contendo a informação de quais objetos serão selecionados.
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
    Returns:
      valor_total: valor total dos itens da mochila em unidades de dinheiros.
      peso_total: peso total dos itens da mochila em unidades de massa.
    """

    valor_total = 0
    peso_total = 0 
        
    for pegou_o_item_ou_nao, nome_do_item in zip(individuo, ordem_dos_nomes):
        if pegou_o_item_ou_nao == 1:
            valor_do_item = objetos[nome_do_item]["valor"]
            peso_do_item = objetos[nome_do_item]["peso"]
            
            valor_total += valor_do_item
            peso_total += peso_do_item
            

    return valor_total, peso_total



#################################################################
#                           genes
#################################################################

def gene_cb():
    """ Gera um gene válido para o problema das caixas binárias
    
    Return:
        Um valos de zeros ou um
    """
    lista = [0, 1]
    gene = random.choice(lista)
    return gene


def gene_cnb(valor_max_caixa):
    ''' gera um gene válido para o problema das caixas não binárias.
    
    Args: 
         valor_max_caixa: valor máximo que a caixa pode assumir
    Return: 
         Um valor de 0 a 'valor_max_caixa' (incluso - vamos incluir o último valor)
    '''
    gene = random.randint(0, valor_max_caixa)
    return gene


def gene_letra(letras):
    """Sorteia uma letra.
    Args:
      letras: letras possíveis de serem sorteadas.
    Return:
      Retorna uma letra dentro das possíveis de serem sorteadas.
    """
    letra = random.choice(letras)
    return letra



#################################################################
#                        indivíduo
#################################################################

def individuo_cb (n):
    ''' Gera um individuo para o problema da caixa binaria
    
    Args:
       n: numero de genes do individuo
    
    Return:
        Uma lista com n genes. Cada gene é um valor zero ou um
    '''
    individuo = []
    for i in range(n):
        gene = gene_cb()
        individuo.append(gene)
    return individuo


def individuo_cnb(numero_genes, valor_max_caixa):
    ''' Gera um individuo para o problema da caixa não binária
    
    Args:
       numero_genes: número de genes do individuo (lista)
       valor_max_caixa: valor máximo que a caixa pode assumir

    Return:
        Uma lista que representa um indivpiduo válido para o problema das CNB
    '''
    individuo = []
    for _ in range (numero_genes):
        gene= gene_cnb(valor_max_caixa)
        individuo.append(gene)
    return individuo

    
def individuo_senha(tamanho_senha, letras):
    """Cria um candidato para o problema da senha
    Args:
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.
    Return:
      Lista com n letras
    """

    candidato = []

    for n in range(tamanho_senha):
        candidato.append(gene_letra(letras))

    return candidato


    
def individuo_senha_variavel(max_tamanho, letras):
    """Cria um candidato para o problema da senha
    Args:
      letras: letras possíveis de serem sorteadas.
      max_tamanho: tamanho maximo que a senha pode ter.
    Return:
      Lista com um numero aleatório de letras.
    """

    candidato = []
    tamanho_max = random.randint(3, max_tamanho) #para nao ter problema no cruzamento

    for n in range(tamanho_max):
        candidato.append(gene_letra(letras))
    return candidato



def individuo_cv(cidades):
    """Sorteia um caminho possível no problema do caixeiro viajante
    Args:
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Return:
      Retorna uma lista de nomes de cidades formando um caminho onde visitamos
      cada cidade apenas uma vez.
    """
    nomes = list(cidades.keys())
    random.shuffle(nomes) #shuffle muda a ordem da minha lista
    return nomes




#################################################################
#                        população
#################################################################

def populacao_cb(tamanho, n):
    ''' cria uma população no problema das caixas binárias.
    
    Args:
       n: numero de gene de um individuo
       tamanho: tamanho da população
    
    Return:
        Uma lista onde cada item é um individuo. Um individuo é uma lista com n genes.
    '''
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cb(n)) #ele está criando uma pop a partir de uma funcao que ja existe, n vezes
    return populacao


def populacao_cnb(tamanho_populacao, numero_genes,valor_max_caixa):
    ''' cria uma população no problema das caixas binárias
    
    Args:
        tamanho_populacao: numero de individuos da populacao
        numero_genes: numero de genes do individuo
        valor_max_caixa: valor maximo que a caixa pode assumir
        
    Return:
        uma lista onde cada item representa um individuo
    '''
    populacao = []
    for _ in range(tamanho_populacao):
        individuo = individuo_cnb(numero_genes, valor_max_caixa)
        populacao.append(individuo) #ele está criando uma pop a partir de uma funcao que ja existe, n vezes
    return populacao


def populacao_inicial_senha(tamanho, tamanho_senha, letras):
    
    """Cria população inicial no problema da senha
    Args
      tamanho: tamanho da população.
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.
    Returns:
      Lista com todos os indivíduos da população no problema da senha.
    """
    populacao = []
    for n in range(tamanho):
        populacao.append(individuo_senha(tamanho_senha, letras))
    return populacao

def populacao_inicial_senha_variavel(tamanho, max_tamanho, letras):
    
    """Cria população inicial no problema da senha
    Args
      tamanho: tamanho da população.
      max_tamanho: tamanho max que a senha pode ter
      letras: letras possíveis de serem sorteadas.
    Returns:
      Lista com todos os indivíduos da população no problema da senha.
    """
    populacao = []
    for n in range(tamanho):
        populacao.append(individuo_senha_variavel(max_tamanho, letras))
    return populacao


def populacao_inicial_cv(tamanho, cidades):
    """Cria população inicial no problema do caixeiro viajante.
    Args
      tamanho:
        Tamanho da população.
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
      Lista com todos os indivíduos da população no problema do caixeiro
      viajante.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cv(cidades))
    return populacao


#################################################################
#                        seleção
#################################################################

def selecao_roleta_max (populacao, fitness): #depende dos individuos que vão ser sorteados, o quão bom o individuo é dentro da função
    '''seleciona individuos de uma populacao usando o método de roleta. 
    
    Nota: apenas funciona para problemas de maximizaçao.
    
    Args:
       populacao: lista com todos os individuos da populacao
       fitness: valor da função objetivo dos individuos da população
       
    Returns:
       populações dos individuos selecionados.
    '''
    populacao_selecionada = random.choices(populacao, weights = fitness, k = len(populacao)) 
    return populacao_selecionada 


def selecao_torneio_min(populacao, fitness, tamanho_torneio=3):
    """Faz a seleção de uma população usando torneio.
    Nota: da forma que está implementada, só funciona em problemas de
    minimização.
    Args:
      populacao: população do problema
      fitness: lista com os valores de fitness dos individuos da populacao
      tamanho_torneio: quantidade de invidiuos que batalham entre si
    Returns:
      Individuos selecionados. Lista com os individuos selecionados com mesmo
      tamanho do argumento `populacao`.
    """
    selecionados = []

    # criamos essa variável para associar cada individuo com seu valor de fitness
    par_populacao_fitness = list(zip(populacao, fitness))

    # vamos fazer len(populacao) torneios! Que comecem os jogos!
    for _ in range(len(populacao)):
        combatentes = random.sample(par_populacao_fitness, tamanho_torneio)

        # é assim que se escreve infinito em python
        minimo_fitness = float("inf")

        for par_individuo_fitness in combatentes:
            individuo = par_individuo_fitness[0]
            fit = par_individuo_fitness[1]

            # queremos o individuo de menor fitness
            if fit < minimo_fitness:
                selecionado = individuo
                minimo_fitness = fit

        selecionados.append(selecionado)

    return selecionados



#################################################################
#                       cruzamento
#################################################################
    
def cruzamento_ponto_simples(mae, pai):
    ''' Operador de cruzamento de ponto simples.
    
    Args: 
       mae: uma lista representando um individuo
       pai: uma lista representando um individuo
       
    Return:
       Duas listas, sendo que cada uma das listas representa um filho dos pais que foram os argumentos
    '''
    ponto_de_corte = random.randint(1, len(pai)-1) #seleciona numeros inteiros dentro do intervalo, inclusive ele mesmo (tipo com intervalos usando [] fechados) e tem que ser aleatório (random)
    
    filho1 = pai [:ponto_de_corte] + mae [ponto_de_corte:]
    filho2 = mae [:ponto_de_corte] + pai [ponto_de_corte:]
    
    return filho1, filho2

def cruzamento_ponto_simples_sv(mae, pai):
    ''' Operador de cruzamento de ponto simples para o problema das senha variaveis.
    
    Args: 
       mae: uma lista representando um individuo
       pai: uma lista representando um individuo
       
    Return:
       Duas listas, sendo que cada uma das listas representa um filho dos pais que foram os argumentos, com o crossover setado no menor gene 
    '''
    if len(pai) > len(mae):
        ponto_de_corte = random.randint(1, len(pai)-1) #seleciona numeros inteiros dentro do intervalo, inclusive ele mesmo (tipo com intervalos usando [] fechados) e tem que ser aleatório (random)
    else: 
        ponto_de_corte = random.randint(1, len(mae)-1)
    
    filho1 = pai [:ponto_de_corte] + mae [ponto_de_corte:]
    filho2 = mae [:ponto_de_corte] + pai [ponto_de_corte:]
    
    return filho1, filho2



def cruzamento_ordenado(pai, mae):
    """Operador de cruzamento ordenado.
    Neste cruzamento, os filhos mantém os mesmos genes que seus pais tinham,
    porém em uma outra ordem. Trata-se de um tipo de cruzamento útil para
    problemas onde a ordem dos genes é importante e não podemos alterar os genes
    em si. É um cruzamento que pode ser usado no problema do caixeiro viajante.
    Ver pág. 37 do livro do Wirsansky.
    Args:
      pai: uma lista representando um individuo
      mae : uma lista representando um individuo
    Returns:
      Duas listas, sendo que cada uma representa um filho dos pais que foram os
      argumentos. Estas listas mantém os genes originais dos pais, porém altera
      a ordem deles
    """
    corte1 = random.randint(0, len(pai) - 2)# escolher um ponto aleatorio na lista sem chegar no final
    corte2 = random.randint(corte1 + 1, len(pai) - 1) # escolher um ponto aleatorio na lista a partir do corte 1, para não cair o corte no mesmo lugar
    
    filho1 = pai [corte1:corte2]
    for gene in mae:
        if gene not in filho1:
            filho1.append(gene)
    
    filho2= mae[corte1:corte2]
    for gene in pai:
        if gene not in filho2:
            filho2.append(gene)
    
    return filho1, filho2

#################################################################
#                         mutação 
#################################################################

def mutacao_cb(individuo):
    '''realiza a mutacao de um gene no problema das caixas binárias.
    
    Args:
      individuo: uma lista representando um individuo no problema das caixas binárias.
      
    Return:
       Um individuo com gene mutado
    '''
    gene_a_ser_mutado = random.randint(0, len(individuo)-1)
    individuo[gene_a_ser_mutado] = gene_cb()
    return individuo


def mutacao_cnb(individuo, valor_max_caixa):
    '''realiza a mutacao de um gene no problema das caixas nao binárias.
    
    Args:
      individuo: uma lista representando um individuo no problema das caixas nao binárias.
      valor_max_caixa: valor maximo que a caixa pode assumir
      
    Return:
       Um individuo com gene mutado
    '''    
    gene_a_ser_mutado = random.randint(0, len(individuo)-1)
    individuo[gene_a_ser_mutado] = gene_cnb(valor_max_caixa)
    return individuo

    
def mutacao_senha(individuo, letras):
    """Realiza a mutação de um gene no problema da senha.
    Args:
      individuo: uma lista representado um individuo no problema da senha
      letras: letras possíveis de serem sorteadas.
    Return:
      Um individuo (senha) com um gene mutado.
    """
    gene = random.randint(0, len(individuo) - 1)
    individuo[gene] = gene_letra(letras)
    return individuo

def mutacao_senha_sv(individuo, letras, tamanho_max):
    """Realiza a mutação de um gene no problema da senha.
    Args:
      individuo: uma lista representado um individuo no problema da senha.
      letras: letras possíveis de serem sorteadas.
      tamanho_max: tamanho máximo de letras que meu individuo pode ter.
    Return:
      Um individuo (senha) com um gene mutado.
    """
    
    if random.random () < .5:    #50% de chance mutar uma letra e 50% de mutar o tamanho
        gene = random.randint(0, len(individuo) - 1)
        individuo[gene] = gene_letra(letras)
        return individuo
    else: 
        novo_tamanho = random.randint(3, tamanho_max)
        if novo_tamanho < len(individuo): # se a senha antiga tiver o tamanho maior, corta até até o tamanho novo
            return individuo[:novo_tamanho]
        else:       # se a senha antiga for menor, adiciona tantas letras quanto forem necessárias
            for _ in range (novo_tamanho - len(individuo)):
                individuo.append(gene_letra(letras))
            return individuo



def mutacao_de_troca(individuo):
    """Troca o valor de dois genes.
    Args:
      individuo: uma lista representado um individuo.
    Return:
      O indivíduo recebido como argumento, porém com dois dos seus genes
      trocados de posição.
    """
    
    #sample #amostragem de um conjunto de uma lista
    indices = list(range(len(individuo)))
    lista_sorteada = random.sample(indices, k=2)
    indice1 = lista_sorteada[0]
    indice2 = lista_sorteada[1]
    
    individuo [indice1], individuo [indice2] = individuo [indice2], individuo [indice1]    
    
    return individuo
    

    

#################################################################
#                 Função objetivo - indivíduos
#################################################################

def funcao_objetivo_cb(individuo):
    ''' Computa o problema objetivo no problema das caixas binárias
    
    Args:
        individuo: lista contendo os genes das caixas binárias
    
    Return:
        Um valor representando uma soma dos genes do indivíduo
    '''
    return sum(individuo) + 1 # +1 para nao cair no erro de tudo zero

def funcao_objetivo_cnb(individuo):
    ''' calcula o fitness para o problema das caixas nao binarias
    
    Args:
        individuo: lista que representa um individuo dentro do problema das cnb
        
    Return:
        Um valor que representa a fitness do individuo
    '''
    fitness = sum(individuo)
    return fitness


def funcao_objetivo_senha(individuo, senha_verdadeira): #medir o quanto o que vc tem ta longe do que vc quer
    """Computa a funcao objetivo de um individuo no problema da senha
    Args:
      individiuo: lista contendo as letras da senha
      senha_verdadeira: a senha que você está tentando descobrir
    Returns:
      A "distância" entre a senha proposta e a senha verdadeira. Essa distância
      é medida letra por letra. Quanto mais distante uma letra for da que
      deveria ser, maior é essa distância.
    """
    diferenca = 0

    for letra_candidato, letra_oficial in zip(individuo, senha_verdadeira): #itera as duas listas ao mesmo tempo
        diferenca = diferenca + abs(ord(letra_candidato) - ord(letra_oficial))

    return diferenca

def funcao_objetivo_sv(individuo, senha_verdadeira, peso_penalidade):
    """Computa a funcao objetivo de um individuo no problema da senha
    Args:
      individiuo: lista contendo as letras da senha
      senha_verdadeira: a senha que você está tentando descobrir
      peso_penalidade: peso adicionado para a diferença de tamanho entre a lista teste e a lita certa (o valor do fit para cada erro) - faz o fit ficar maior
    Returns:
      A "distância" entre a senha proposta e a senha verdadeira. Essa distância é medida letra por letra. Quanto mais distante uma letra for da que
      deveria ser, maior é essa distância.
    """
    diferenca = 0

    for letra_candidato, letra_oficial in zip(individuo, senha_verdadeira): #itera as duas listas ao mesmo tempo
        diferenca = diferenca + abs(ord(letra_candidato) - ord(letra_oficial))
    
    diferenca_tamanho = abs(len(individuo) - len(senha_verdadeira))
    diferenca += peso_penalidade * diferenca_tamanho

    return diferenca


def funcao_objetivo_cv(individuo, cidades):
    """Computa a funcao objetivo de um individuo no problema do caixeiro viajante.
    Args:
      individiuo:
        Lista contendo a ordem das cidades que serão visitadas
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
      A distância percorrida pelo caixeiro seguindo o caminho contido no
      `individuo`. Lembrando que após percorrer todas as cidades em ordem, o
      caixeiro retorna para a cidade original de onde começou sua viagem.
    """

    distancia = 0
    for posicao in range(len(individuo)-1):
        partida = cidades [individuo[posicao]]
        chegada = cidades [individuo[posicao+1]]
        
        percurso = distancia_entre_dois_pontos(partida, chegada)
        distancia = distancia + percurso #armazena a distancia
        
    #calculando o caminho de volta para a cidade inicial
    partida = cidades[individuo[-1]] #ultima cidade 
    chegada = cidades[individuo[0]] # até a primeira
    
    percurso = distancia_entre_dois_pontos (partida, chegada)
    distancia = distancia + percurso
    
    return distancia


# NOVIDADE
def funcao_objetivo_mochila(individuo, objetos, limite, ordem_dos_nomes):
    """Computa a funcao objetivo de um candidato no problema da mochila.
    Args:
      individiuo:
        Lista binária contendo a informação de quais objetos serão selecionados.
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      limite:
        Número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
    Returns:
      Valor total dos itens inseridos na mochila considerando a penalidade para
      quando o peso excede o limite.
    """

    valor_mochila, peso_mochila = computa_mochila(individuo, objetos, ordem_dos_nomes)
    
    if peso_mochila > limite:
        valor_mochila = 0.01 #problema de maximizacao, para o algoritmo nao escolher esse item
        
    return valor_mochila



def funcao_objetivo_cv_gasolina(individuo, cidades):
    """Computa a funcao objetivo de um individuo no problema do caixeiro viajante.
    Args:
      individiuo:
        Lista contendo a ordem das cidades que serão visitadas
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
      A distância percorrida pelo caixeiro seguindo o caminho contido no
      `individuo`. Lembrando que após percorrer todas as cidades em ordem, o
      caixeiro retorna para a cidade original de onde começou sua viagem.
    """

    distancia = 0
    for posicao in range(len(individuo)-1):
        partida = cidades [individuo[posicao]]
        chegada = cidades [individuo[posicao+1]]
        
        percurso = distancia_entre_dois_pontos(partida, chegada)
        distancia = distancia + percurso #armazena a distancia
        
    #calculando o caminho de volta para a cidade inicial
    partida = cidades[individuo[-1]] #ultima cidade 
    chegada = cidades[individuo[0]] # até a primeira
    
    percurso = distancia_entre_dois_pontos (partida, chegada)
    distancia = distancia + percurso
    
    return -distancia # por ser um problema de maximizacao



#################################################################
#                 Função objetivo - população              
#################################################################

#possuem sempre a mesma estrutura, calcular a funcao obj para o individuo e colocar em uma lista de resultados

def funcao_objetivo_pop_cb(populacao):
    ''' calcula a funcao objetivo para todos os membros de uma populacao
    
    Args: 
       populacao: lista com todos os individuos da populacao.
    
    Return:
       lista de valores representando a fitness de cada individuo
    '''
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetivo_cb(individuo)
        fitness.append(fobj)
    return fitness
        
    
def funcao_objetivo_pop_cnb(populacao):
    ''' calcula a funcao objetivo para a populacao completa
    
    Args: 
       populacao: lista com todos os individuos da populacao.
    
    Return:
       lista de valores representando a fitness de cada individuo
    '''
    fitness_pop = []
    for individuo in populacao:
        fitness_ind = funcao_objetivo_cnb(individuo)
        fitness_pop.append(fitness_ind)
    return fitness_pop

        
def funcao_objetivo_pop_senha(populacao, senha_verdadeira):
    """Computa a funcao objetivo de uma populaçao no problema da senha.
    Args:
      populacao: lista com todos os individuos da população
      senha_verdadeira: a senha que você está tentando descobrir
    Returns:
      Lista contendo os valores da métrica de distância entre senhas.
    """
    resultado = []

    for individuo in populacao:
        resultado.append(funcao_objetivo_senha(individuo, senha_verdadeira))

    return resultado

def funcao_objetivo_pop_sv (populacao, senha_verdadeira, peso_penalidade):
    """Computa a funcao objetivo de uma populaçao no problema da senha.
    Args:
      populacao: lista com todos os individuos da população
      senha_verdadeira: a senha que você está tentando descobrir
      peso_penalidade: peso adicionado para a diferença de tamanho entre a lista teste e a lita certa (o valor do fit para cada erro) - faz o fit ficar maior
    Returns:
      Lista contendo os valores da métrica de distância entre senhas.
    """
    resultado = []
    for individuo in populacao:
        resultado.append(funcao_objetivo_sv(individuo, senha_verdadeira, peso_penalidade))

    return resultado


def funcao_objetivo_pop_cv(populacao, cidades):
    """Computa a funcao objetivo de uma população no problema do caixeiro viajante.
    Args:
      populacao:
        Lista com todos os inviduos da população
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
      Lista contendo a distância percorrida pelo caixeiro para todos os
      indivíduos da população.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(funcao_objetivo_cv(individuo, cidades))

    return resultado


# NOVIDADE
def funcao_objetivo_pop_mochila(populacao, objetos, limite, ordem_dos_nomes):
    """Computa a fun. objetivo de uma populacao no problema da mochila
    Args:
      populacao:
        Lista com todos os individuos da população
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      limite:
        Número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
    Returns:
      Lista contendo o valor dos itens da mochila de cada indivíduo.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(
            funcao_objetivo_mochila(
                individuo, objetos, limite, ordem_dos_nomes
            )
        )

    return resultado


def funcao_objetivo_pop_cv_gasoliba(populacao, cidades):
    """Computa a funcao objetivo de uma população no problema do caixeiro viajante.
    Args:
      populacao:
        Lista com todos os inviduos da população
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
      Lista contendo a distância percorrida pelo caixeiro para todos os
      indivíduos da população.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(funcao_objetivo_cv_gasolina(individuo, cidades))

    return resultado
 
