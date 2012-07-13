'''
Created on Jul 5, 2012

@author: Meire Vasconcelos
'''

class Requisito(object):
    '''
    classdocs
    '''
    index = -1        #Identificador unico do requisito
    custo = -1        #Valores entre 1 a 5 --> Eh levado em consideracao para nao estourar o orcamento
    tempo = -1        #Valores entre 1 a 10 --> Eh levado em consideracao para nao estourar o tempo de projeto
    prior = -1        #Prioridade do requisito (varia de 5 a 9) (Classificado pelo cliente)
    valor = -1        #Calculo da prioridade - custo do requisito (varia de 4 a 8 dependendo dos outros parametros)
     
    def __init__(self, index, custo, tempo, prior):
        
        '''
        Constructor
        '''
        self.index = index
        self.custo = custo
        self.tempo = tempo
        self.prior = prior
        
        self.valor = prior-custo
        
        
        
        
        