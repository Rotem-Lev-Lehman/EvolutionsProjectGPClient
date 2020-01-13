import operator
import numpy
import json
import random

from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from deap import gp
from deap.gp import PrimitiveSetTyped
from classes import *
from GPClient import calculate_fitness


def evalTicTacToeGP(individual):
    func = toolbox.compile(expr=individual)
    json_string = str(func(0).root)
    json_obj = json.loads(json_string)
    fitness = calculate_fitness(json_obj, True)
    return fitness,


# interesting stuff:
pset = PrimitiveSetTyped("main", [root], root_wrapper)
pset.addPrimitive(root_wrapperFunc, [root], root_wrapper)
pset.addPrimitive(rootFunc, [btl,btl,btf,btf,btf,btf,btf,bt,bt,bt], root)

pset.addPrimitive(btlFunc3, [while_truel3], btl)

pset.addPrimitive(btfFunc1, [while_truef1], btf)
pset.addPrimitive(btfFunc2, [while_truef2], btf)
pset.addPrimitive(btfFunc3, [while_truef3], btf)

pset.addPrimitive(btFunc, [whiletrue], bt)

pset.addPrimitive(while_truel3Func1, [wait_forl, wait_forl, requestl1], while_truel3)
pset.addPrimitive(while_truel3Func2, [wait_forl, wait_forl, requestl2], while_truel3)
pset.addPrimitive(while_truel3Func3, [wait_forl, wait_forl, requestl3], while_truel3)
pset.addPrimitive(while_truel3Func4, [wait_forl, wait_forl, requestl4], while_truel3)

pset.addPrimitive(while_truef1Func1, [request1], while_truef1)
pset.addPrimitive(while_truef1Func2, [request2], while_truef1)
pset.addPrimitive(while_truef1Func3, [request3], while_truef1)
pset.addPrimitive(while_truef1Func4, [request4], while_truef1)

pset.addPrimitive(while_truef2Func1, [wait_forf, request1], while_truef2)
pset.addPrimitive(while_truef2Func2, [wait_forf, request2], while_truef2)
pset.addPrimitive(while_truef2Func3, [wait_forf, request3], while_truef2)
pset.addPrimitive(while_truef2Func4, [wait_forf, request4], while_truef2)

pset.addPrimitive(while_truef3Func1, [wait_forf, wait_forf, request1], while_truef3)
pset.addPrimitive(while_truef3Func2, [wait_forf, wait_forf, request2], while_truef3)
pset.addPrimitive(while_truef3Func3, [wait_forf, wait_forf, request3], while_truef3)
pset.addPrimitive(while_truef3Func4, [wait_forf, wait_forf, request4], while_truef3)

pset.addPrimitive(while_trueFunc1, [request1], whiletrue)
pset.addPrimitive(while_trueFunc2, [request2], whiletrue)
pset.addPrimitive(while_trueFunc3, [request3], whiletrue)
pset.addPrimitive(while_trueFunc4, [request4], whiletrue)

pset.addPrimitive(wait_forlFuncX, [Xl], wait_forl)
pset.addPrimitive(wait_forlFuncO, [Ol], wait_forl)

pset.addPrimitive(wait_forfFuncX, [Xf], wait_forf)

pset.addPrimitive(request1Func, [O], request1)
pset.addPrimitive(request2Func, [O, O], request2)
pset.addPrimitive(request3Func, [O, O, O], request3)
pset.addPrimitive(request4Func, [O, O, O, O], request4)

pset.addPrimitive(requestl1Func, [Ol], requestl1)
pset.addPrimitive(requestl2Func, [Ol, Ol], requestl2)
pset.addPrimitive(requestl3Func, [Ol, Ol, Ol], requestl3)
pset.addPrimitive(requestl4Func, [Ol, Ol, Ol, Ol], requestl4)

pset.addPrimitive(xlFunc, [position, position], Xl)
pset.addPrimitive(olFunc, [position, position], Ol)

pset.addPrimitive(xfFunc, [positionf, positionf], Xf)

pset.addPrimitive(oFunc, [position, position], O)

pset.addPrimitive(posFunc, [position], position)
pset.addPrimitive(posfFunc, [positionf], positionf)

pset.addTerminal(0, position)
pset.addTerminal(1, position)
pset.addTerminal(2, position)

pset.addTerminal(0, positionf)
pset.addTerminal(1, positionf)


# stuff to run:
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMax, pset=pset)

toolbox = base.Toolbox()
toolbox.register("expr", gp.genGrow, pset=pset, min_=6, max_=6)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("compile", gp.compile, pset=pset)

toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genGrow, min_=6, max_=6)
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)
toolbox.register("evaluate", evalTicTacToeGP)
toolbox.register("select", tools.selTournament, tournsize=5)


def main():
    '''
    m = 0.01 c= 0.7 n = 100
    m = 0.001 c= 0.7 n = 100
    m = 0.01 c= 0.4 n = 100
    m = 0.001 c= 0.4 n = 100
    m = 0.01 c= 0.7 n = 50
    m = 0.001 c= 0.7 n = 50
    m = 0.01 c= 0.4 n = 50
    m = 0.001 c= 0.4 n = 50
    m = 0.01 c= 0.7 n = 10

    m = 0.001 c= 0.7 n = 10
    m = 0.01 c= 0.4 n = 10
    m = 0.001 c= 0.4 n = 10
    '''

    pop = toolbox.population(n=50)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("Avg", numpy.mean)
    stats.register("Median", numpy.median)
    stats.register("Best", numpy.max)
    stats.register("Worst", numpy.min)

    algorithms.eaSimple(pop, toolbox, cxpb=0.4, mutpb=0.01, ngen=100, stats=stats, halloffame=hof, verbose=True)

    print(hof.__getitem__(0))
    func = toolbox.compile(expr=hof.__getitem__(0))

    print(str(func(0).root))

    return pop, stats, hof


if __name__ == "__main__":
    main()

