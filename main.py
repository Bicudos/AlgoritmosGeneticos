import random
                      
from pyevolve import G1DList
from pyevolve import GSimpleGA
from pyevolve import GAllele
from pyevolve import Mutators
from pyevolve import Initializators
from pyevolve import DBAdapters
from pyevolve import Crossovers
from pyevolve import Consts


from requisitos import Requisito

def geraRequisitos(num):
 
    list = []
        
    for i in range(num):
        
        index = i
        custo = random.randint(1, 5)
        tempo = random.randint(1, 10)
        prior = random.randint(5, 9)
            
        list.append(Requisito(index, custo, tempo, prior))
        
    return list

def G1DListTSPInitializator(genome, **args):
   """ The initializator for the TSP """
   genome.clearList()
   lst = [i for i in xrange(genome.listSize)]

   for i in xrange(genome.listSize):
      choice = random.choice(lst)
      lst.remove(choice)
      genome.append(choice)


def calculo_custo(listaComTodosRequisitos, listaParcial):
   
   """ Returna o custo total do projeto."""
   
   custo = 0
   
   num_requisitos=len(listaParcial)
   
   for i in range(num_requisitos):
       
      if custo < 50: 
          custo += listaComTodosRequisitos[listaParcial[i]].custo
         
   return custo

def eval_func(chromosome):
    
   """ The evaluation function """
   global listReq
   return calculo_custo(listReq, chromosome)



listReq = geraRequisitos(50)


def main_run():

    global listReq
   
    # write_random(filename, number of the cities, max width, max_height)
    #escreve_requisitos("requisitos.txt", listReq)
    
    
    # set the alleles to the cities numbers
    setOfAlleles = GAllele.GAlleles(homogeneous=True)
    lst = [ i for i in xrange(len(listReq)) ]
    
    
    a = GAllele.GAlleleList(lst)
    setOfAlleles.add(a)
    
    #import pdb; pdb.set_trace()
    
    genome = G1DList.G1DList(len(listReq))
    genome.setParams(allele=setOfAlleles)
    
    genome.evaluator.set(eval_func)
    genome.mutator.set(Mutators.G1DListMutatorSwap)
    genome.crossover.set(Crossovers.G1DListCrossoverOX)
    genome.initializator.set(G1DListTSPInitializator)
    genome.setParams(rangemin=10, rangemax=40)
    
    ga = GSimpleGA.GSimpleGA(genome)
    ga.setGenerations(100)
    ga.terminationCriteria.set(GSimpleGA.ConvergenceCriteria)
    ga.setMinimax(Consts.minimaxType["minimize"])
    ga.setCrossoverRate(1.0)
    ga.setMutationRate(0.03)
    ga.setPopulationSize(80)
    
    ga.evolve(freq_stats=10)
    best = ga.bestIndividual()
    print best

if __name__ == "__main__":
   main_run()
   
