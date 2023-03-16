import random

def gene_cb():
    """ Gera um gene válido para o problema das caixas binárias
    
    Return:
        Um valos de zeros ou um
    """
    lista = [0, 1]
    gene = random.choice(lista)
    return gene


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
    
    

def funcao_objetivo_cb(individuo):
    ''' Computa o problema objetivo no problema das caixas binárias
    
    Args:
        individuo: lista contendo os genes das caixas binárias
    
    Return:
        Um valor representando uma soma dos genes do indivíduo
    '''
    return sum(individuo) + 1 # +1 para nao cair no erro de tudo zero


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
        
    


 
