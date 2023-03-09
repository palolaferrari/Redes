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

def funcao_objetivo_cb(individuo):
    ''' Computa o problema objetivo no problema das caixas binárias
    
    Args:
        individuo: lista contendo os genes das caixas binárias
    
    Return:
        Um valor representando uma soma dos genes do indivíduo
    '''
    return sum(individuo)


 
