import operator
import numpy
import json
import random
import time
import csv

from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from deap import gp
from deap.gp import PrimitiveSetTyped
from classes import *
from GPClient import calculate_fitness

results_folder_name = "results/"
playingAgainstRandomPlayer = True


def evalTicTacToeGP(individual):
    func = toolbox.compile(expr=individual)
    json_string = str(func(0).root)
    json_obj = json.loads(json_string)
    fitness = calculate_fitness(json_obj, playingAgainstRandomPlayer)
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

pset.addPrimitive(request1Func, [O, priority], request1)
pset.addPrimitive(request2Func, [O, O, priority], request2)
pset.addPrimitive(request3Func, [O, O, O, priority], request3)
pset.addPrimitive(request4Func, [O, O, O, O, priority], request4)

pset.addPrimitive(requestl1Func, [Ol, priority], requestl1)
pset.addPrimitive(requestl2Func, [Ol, Ol, priority], requestl2)
pset.addPrimitive(requestl3Func, [Ol, Ol, Ol, priority], requestl3)
pset.addPrimitive(requestl4Func, [Ol, Ol, Ol, Ol, priority], requestl4)

pset.addPrimitive(xlFunc, [position, position], Xl)
pset.addPrimitive(olFunc, [position, position], Ol)

pset.addPrimitive(xfFunc, [positionf, positionf], Xf)

pset.addPrimitive(oFunc, [position, position], O)

pset.addPrimitive(posFunc, [position], position)
pset.addPrimitive(posfFunc, [positionf], positionf)
pset.addPrimitive(priorityFunc, [priority], priority)

pset.addTerminal(0, position)
pset.addTerminal(1, position)
pset.addTerminal(2, position)

pset.addTerminal(0, positionf)
pset.addTerminal(1, positionf)

pset.addTerminal(1, priority)
pset.addTerminal(2, priority)
pset.addTerminal(3, priority)
pset.addTerminal(4, priority)
pset.addTerminal(5, priority)
pset.addTerminal(6, priority)
pset.addTerminal(7, priority)
pset.addTerminal(8, priority)
pset.addTerminal(9, priority)
pset.addTerminal(10, priority)
pset.addTerminal(11, priority)


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


def save_results(experiment_name, cross_over_p, mut_p, statsRand, stats, best_ind, total_time, num_of_generations):
    global results_folder_name
    file_name = results_folder_name + experiment_name + ".csv"
    with open(file_name, mode='w', newline='') as results_file:
        results_writer = csv.writer(results_file, delimiter=',')

        results_writer.writerow(["cross over p:", str(cross_over_p)])
        results_writer.writerow(["cross over n (num of points for crossover):", str(1)])
        results_writer.writerow(["mutation p:", str(mut_p)])
        results_writer.writerow(["avg time for generation:", str(total_time / num_of_generations)])
        results_writer.writerow(["time for terminating:", str(total_time)])
        results_writer.writerow(["best individual:", best_ind])
        results_writer.writerow(["genID", "max", "average", "median", "min"])
        rand_list = statsRand[1]
        for i, curr in enumerate(rand_list):
            results_writer.writerow([str(i), str(curr["Best"]), str(curr["Avg"]), str(curr["Median"]), str(curr["Worst"])])

        opt_list = stats[1]
        for i, curr in enumerate(opt_list):
            results_writer.writerow([str(i + len(rand_list)), str(curr["Best"]), str(curr["Avg"]), str(curr["Median"]), str(curr["Worst"])])


def runExperiment(cross_over_p, mut_p, experiment_name):
    global playingAgainstRandomPlayer

    num_of_generations_vs_random = 100
    num_of_generations_vs_optimal = 50
    population_size = 100

    print("Now running the " + str(experiment_name) + " experiment on cross_over_p = " + str(cross_over_p) + ", mut_p = " + str(mut_p))
    start_time = time.time()
    playingAgainstRandomPlayer = True
    pop = toolbox.population(n=population_size)
    hofRand = tools.HallOfFame(1)
    statsRand = tools.Statistics(lambda ind: ind.fitness.values)
    statsRand.register("Avg", numpy.mean)
    statsRand.register("Median", numpy.median)
    statsRand.register("Best", numpy.max)
    statsRand.register("Worst", numpy.min)

    print("training against random player:")
    rand_log = algorithms.eaSimple(pop, toolbox, cxpb=cross_over_p, mutpb=mut_p, ngen=num_of_generations_vs_random, stats=statsRand, halloffame=hofRand, verbose=True)

    func = toolbox.compile(expr=hofRand.__getitem__(0))
    print(str(func(0).root))

    print()
    print("training against optimal from now on:")
    for i in range(len(pop)):
        pop[i].fitness.values = ()

    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("Avg", numpy.mean)
    stats.register("Median", numpy.median)
    stats.register("Best", numpy.max)
    stats.register("Worst", numpy.min)
    playingAgainstRandomPlayer = False

    opt_log = algorithms.eaSimple(pop, toolbox, cxpb=cross_over_p, mutpb=mut_p, ngen=num_of_generations_vs_optimal, stats=stats, halloffame=hof, verbose=True)
    print(hof.__getitem__(0))
    func = toolbox.compile(expr=hof.__getitem__(0))

    best_ind = str(func(0).root)
    print(best_ind)

    end_time = time.time()
    total_time = end_time - start_time
    print("Total time = " + str(total_time))

    save_results(experiment_name, cross_over_p, mut_p, rand_log, opt_log, best_ind, total_time, num_of_generations_vs_random + num_of_generations_vs_optimal)


def runExperiment3Times(cross_over_p, mut_p, name):
    for i in range(3):
        curr_name = name + "_" + str(i)
        runExperiment(cross_over_p, mut_p, curr_name)


def main():
    runExperiment3Times(0.7, 0.1, "exp1")
    runExperiment3Times(0.7, 0.01, "exp2")
    runExperiment3Times(0.7, 0.001, "exp3")
    runExperiment3Times(0.4, 0.1, "exp4")
    runExperiment3Times(0.4, 0.01, "exp5")
    runExperiment3Times(0.4, 0.001, "exp6")


if __name__ == "__main__":
    main()

