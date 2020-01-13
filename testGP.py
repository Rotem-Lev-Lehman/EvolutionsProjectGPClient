import operator
import numpy
import json

from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from deap import gp
from deap.gp import PrimitiveSetTyped
import obj

btNames = ["bp.registerBThread(\"AddThirdO(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">,\"+\"<\"+f[p[2]].x+\",\"+f[p[2]].y+\">)\",function(){",
           "bp.registerBThread(\"PreventThirdX(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">,\"+\"<\"+f[p[2]].x+\",\"+f[p[2]].y+\">)\",function(){",
           "bp.registerBThread(\"PreventFork22X(<\" + f[p[0]].x + \",\" + f[p[0]].y + \">,\" + \"<\" + f[p[1]].x + \",\" + f[p[1]].y + \">)\", function() {",
           "bp.registerBThread(\"PreventFork02X(<\" + f[p[0]].x + \",\" + f[p[0]].y + \">,\" + \"<\" + f[p[1]].x + \",\" + f[p[1]].y + \">)\", function() {",
           "bp.registerBThread(\"PreventFork20X(<\" + f[p[0]].x + \",\" + f[p[0]].y + \">,\" + \"<\" + f[p[1]].x + \",\" + f[p[1]].y + \">)\", function() {",
           "bp.registerBThread(\"PreventFork00X(<\" + f[p[0]].x + \",\" + f[p[0]].y + \">,\" + \"<\" + f[p[1]].x + \",\" + f[p[1]].y + \">)\", function() {",
           "bp.registerBThread(\"PreventForkdiagX(<\" + f[p[0]].x + \",\" + f[p[0]].y + \">,\" + \"<\" + f[p[1]].x + \",\" + f[p[1]].y + \">)\", function() {",
           "bp.registerBThread(\"Center\", function() {",
           "bp.registerBThread(\"Corners\", function() {",
           "bp.registerBThread(\"Sides\", function() {"
           ]

currentBtNameIndex = 0

weights = [50, 40, 30, 30, 30, 30, 30, 35, 20, 10]

currentWeightIndex = 0


class root_wrapper:
    def __init__(self, root):
        self.root = root

    def __str__(self):
        return str(root)

    __repr__ = __str__


class root:

    def __init__(self, btf1,btf2,btf3,btf4,btf5,btf6,btf7,bt1,bt2,bt3):
        self.btf1 = btf1
        self.btf2 = btf2
        self.btf3 = btf3
        self.btf4 = btf4
        self.btf5 = btf5
        self.btf6 = btf6
        self.btf7 = btf7
        self.bt1 = bt1
        self.bt2 = bt2
        self.bt3 = bt3

    def __str__(self):
        curr_instance = {
            "t0": str(self.btf1),
            "t1": str(self.btf2),
            "t2": str(self.btf3),
            "t3": str(self.btf4),
            "t4": str(self.btf5),
            "t5": str(self.btf6),
            "t6": str(self.btf7),
            "t7": str(self.bt1),
            "t8": str(self.bt2),
            "t9": str(self.bt3)
        }
        return json.dumps(curr_instance)

    __repr__ = __str__


class btf:
    def __init__(self, whiletruef):
        self.whiletruef = whiletruef

    def __str__(self):
        global currentBtNameIndex, btNames
        currName = btNames[currentBtNameIndex]
        currentBtNameIndex = (currentBtNameIndex + 1) % 10
        return currName + str(self.whiletruef) + "});"

    __repr__ = __str__


class bt:
    def __init__(self, whiletrue):
        self.whiletrue = whiletrue

    def __str__(self):
        global currentBtNameIndex, btNames
        currName = btNames[currentBtNameIndex]
        currentBtNameIndex = (currentBtNameIndex + 1) % 10
        return currName + str(self.whiletrue) + "});"

    __repr__ = __str__


class while_truef1:
    def __init__(self, requestf):
        self.requestf = requestf
    def __str__(self):
        return "while(true){" + str(self.requestf)+ "}"
    __repr__ = __str__


class while_truef2:
    def __init__(self, wait_forf, requestf):
        self.requestf = requestf
        self.wait_forf = wait_forf
    def __str__(self):
        return "while(true){" + str(self.wait_forf) + str(self.requestf)+ "}"
    __repr__ = __str__


class while_truef3:
    def __init__(self, wait_forf1,wait_forf2, requestf):
        self.requestf = requestf
        self.wait_forf1 = wait_forf1
        self.wait_forf2 = wait_forf2

    def __str__(self):
        return "while(true){" + str(self.wait_forf1) + str(self.wait_forf2) + str(self.requestf) + "}"
    __repr__ = __str__


class whiletrue:
    def __init__(self, request):
        self.request = request
    def __str__(self):
        return "while(true){" + str(self.request) + "}"
    __repr__ = __str__


class wait_forf:
    def __init__(self, eventf):
        self.eventf = eventf

    def __str__(self):
        return "bp.sync({waitFor:[" + str(self.eventf) + "]});"
    __repr__ = __str__


class requestf1:
    def __init__(self, Of):
        self.Of = Of

    def __str__(self):
        global currentWeightIndex, weights
        curr_weight = str(weights[currentWeightIndex])
        currentWeightIndex = (currentWeightIndex + 1) % 10
        return "bp.sync({request:[" + str(self.Of) + "]}," + curr_weight + ");"
    __repr__ = __str__


class requestf2:
    def __init__(self, Of1, Of2):
        self.Of1 = Of1
        self.Of2 = Of2

    def __str__(self):
        global currentWeightIndex, weights
        curr_weight = str(weights[currentWeightIndex])
        currentWeightIndex = (currentWeightIndex + 1) % 10
        return "bp.sync({request:[" + str(self.Of1) + "," + str(self.Of2) + "]}," + curr_weight + ");"

    __repr__ = __str__


class requestf3:
    def __init__(self, Of1, Of2, Of3):
        self.Of1 = Of1
        self.Of2 = Of2
        self.Of3 = Of3

    def __str__(self):
        global currentWeightIndex, weights
        curr_weight = str(weights[currentWeightIndex])
        currentWeightIndex = (currentWeightIndex + 1) % 10
        return "bp.sync({request:[" + str(self.Of1) + "," + str(self.Of2) + "," + str(self.Of3) + "]}," + curr_weight + ");"

    __repr__ = __str__


class requestf4:
    def __init__(self, Of1, Of2, Of3, Of4):
        self.Of1 = Of1
        self.Of2 = Of2
        self.Of3 = Of3
        self.Of4 = Of4

    def __str__(self):
        global currentWeightIndex, weights
        curr_weight = str(weights[currentWeightIndex])
        currentWeightIndex = (currentWeightIndex + 1) % 10
        return "bp.sync({request:[" + str(self.Of1) + "," + str(self.Of2) + "," + str(self.Of3) + "," + str(self.Of4) + "]}," + curr_weight + ");"

    __repr__ = __str__


class Xf:
    def __init__(self, pos1, pos2):
        self.pos1 = pos1
        self.pos2 = pos2

    def __str__(self):
        return "X(f[p[" + str(self.pos1) + "]].x,f[p[" + str(self.pos2) + "]].y)"
    __repr__ = __str__


class Of:
    def __init__(self, pos1, pos2):
        self.pos1 = pos1
        self.pos2 = pos2

    def __str__(self):
        return "O(f[p[" + str(self.pos1) + "]].x,f[p[" + str(self.pos2) + "]].y)"
    __repr__ = __str__


class request1:
    def __init__(self, O):
        self.O = O
    def __str__(self):
        global currentWeightIndex, weights
        curr_weight = str(weights[currentWeightIndex])
        currentWeightIndex = (currentWeightIndex + 1) % 10
        return "bp.sync({request:[" + str(self.O) + "]}," + curr_weight + ");"
    __repr__ = __str__


class request2:
    def __init__(self, O1, O2):
        self.O1 = O1
        self.O2 = O2

    def __str__(self):
        global currentWeightIndex, weights
        curr_weight = str(weights[currentWeightIndex])
        currentWeightIndex = (currentWeightIndex + 1) % 10
        return "bp.sync({request:[" + str(self.O1) + "," + str(self.O2) + "]}," + curr_weight + ");"

    __repr__ = __str__


class request3:
    def __init__(self, O1, O2, O3):
        self.O1 = O1
        self.O2 = O2
        self.O3 = O3

    def __str__(self):
        global currentWeightIndex, weights
        curr_weight = str(weights[currentWeightIndex])
        currentWeightIndex = (currentWeightIndex + 1) % 10
        return "bp.sync({request:[" + str(self.O1) + "," + str(self.O2) + "," + str(self.O3) + "]}," + curr_weight + ");"

    __repr__ = __str__


class request4:
    def __init__(self, O1, O2, O3, O4):
        self.O1 = O1
        self.O2 = O2
        self.O3 = O3
        self.O4 = O4

    def __str__(self):
        global currentWeightIndex, weights
        curr_weight = str(weights[currentWeightIndex])
        currentWeightIndex = (currentWeightIndex + 1) % 10
        return "bp.sync({request:[" + str(self.O1) + "," + str(self.O2) + "," + str(self.O3) + "," + str(self.O4) + "]}," + curr_weight + ");"

    __repr__ = __str__


class O:
    def __init__(self, pos1, pos2):
        self.pos1 = pos1
        self.pos2 = pos2

    def __str__(self):
        return "O(" + str(self.pos1) + "," + str(self.pos2) + ")"
    __repr__ = __str__


def root_wrapperFunc(root):
    return root_wrapper(root)


def rootFunc(btf1,btf2,btf3,btf4,btf5,btf6,btf7,bt1,bt2,bt3):
    return root(btf1,btf2,btf3,btf4,btf5,btf6,btf7,bt1,bt2,bt3)


def btfFunc1(while_true_f1):
    return btf(while_true_f1)


def btfFunc2(while_true_f2):
    return btf(while_true_f2)


def btfFunc3(while_true_f3):
    return btf(while_true_f3)


def btFunc(while_true):
    return bt(while_true)

# while_truef1
def while_truef1Func1(requestf):
    return while_truef1(requestf)


def while_truef1Func2(requestf):
    return while_truef1(requestf)


def while_truef1Func3(requestf):
    return while_truef1(requestf)


def while_truef1Func4(requestf):
    return while_truef1(requestf)
# done while_truef1

# while_truef2
def while_truef2Func1(waitforf, requestf):
    return while_truef2(waitforf, requestf)


def while_truef2Func2(waitforf, requestf):
    return while_truef2(waitforf, requestf)


def while_truef2Func3(waitforf, requestf):
    return while_truef2(waitforf, requestf)


def while_truef2Func4(waitforf, requestf):
    return while_truef2(waitforf, requestf)
# done while_truef2

# while_truef3
def while_truef3Func1(waitforf1, waitforf2, requestf):
    return while_truef3(waitforf1, waitforf2, requestf)


def while_truef3Func2(waitforf1, waitforf2, requestf):
    return while_truef3(waitforf1, waitforf2, requestf)


def while_truef3Func3(waitforf1, waitforf2, requestf):
    return while_truef3(waitforf1, waitforf2, requestf)


def while_truef3Func4(waitforf1, waitforf2, requestf):
    return while_truef3(waitforf1, waitforf2, requestf)
# done while_truef2


def while_trueFunc1(request):
    return whiletrue(request)


def while_trueFunc2(request):
    return whiletrue(request)


def while_trueFunc3(request):
    return whiletrue(request)


def while_trueFunc4(request):
    return whiletrue(request)


def wait_forfFuncX(xf):
    return wait_forf(xf)


def wait_forfFuncO(of):
    return wait_forf(of)


# request
def request1Func(o):
    return request1(o)


def request2Func(o1, o2):
    return request2(o1, o2)


def request3Func(o1, o2, o3):
    return request3(o1, o2, o3)


def request4Func(o1, o2, o3, o4):
    return request4(o1, o2, o3, o4)
# done request


# requestf
def requestf1Func(o):
    return requestf1(o)


def requestf2Func(o1, o2):
    return requestf2(o1, o2)


def requestf3Func(o1, o2, o3):
    return requestf3(o1, o2, o3)


def requestf4Func(o1, o2, o3, o4):
    return requestf4(o1, o2, o3, o4)
# done requestf


def xfFunc(pos1, pos2):
    return Xf(pos1, pos2)


def ofFunc(pos1, pos2):
    return Of(pos1, pos2)


def oFunc(pos1, pos2):
    return O(pos1, pos2)


def posFunc(pos):
    return pos


def evalTestGP(individual):
    # todo complete this func
    func = toolbox.compile(expr=individual)
    return 1,


# interesting stuff:
pset = PrimitiveSetTyped("main", [root], root_wrapper)
pset.addPrimitive(root_wrapperFunc, [root], root_wrapper)
pset.addPrimitive(rootFunc, [btf,btf,btf,btf,btf,btf,btf,bt,bt,bt], root)
pset.addPrimitive(btfFunc1, [while_truef1], btf)
pset.addPrimitive(btfFunc2, [while_truef2], btf)
pset.addPrimitive(btfFunc3, [while_truef3], btf)
pset.addPrimitive(btFunc, [whiletrue], bt)

pset.addPrimitive(while_truef1Func1, [requestf1], while_truef1)
pset.addPrimitive(while_truef1Func2, [requestf2], while_truef1)
pset.addPrimitive(while_truef1Func3, [requestf3], while_truef1)
pset.addPrimitive(while_truef1Func4, [requestf4], while_truef1)

pset.addPrimitive(while_truef2Func1, [wait_forf, requestf1], while_truef2)
pset.addPrimitive(while_truef2Func2, [wait_forf, requestf2], while_truef2)
pset.addPrimitive(while_truef2Func3, [wait_forf, requestf3], while_truef2)
pset.addPrimitive(while_truef2Func4, [wait_forf, requestf4], while_truef2)

pset.addPrimitive(while_truef3Func1, [wait_forf, wait_forf, requestf1], while_truef3)
pset.addPrimitive(while_truef3Func2, [wait_forf, wait_forf, requestf2], while_truef3)
pset.addPrimitive(while_truef3Func3, [wait_forf, wait_forf, requestf3], while_truef3)
pset.addPrimitive(while_truef3Func4, [wait_forf, wait_forf, requestf4], while_truef3)

pset.addPrimitive(while_trueFunc1, [request1], whiletrue)
pset.addPrimitive(while_trueFunc2, [request2], whiletrue)
pset.addPrimitive(while_trueFunc3, [request3], whiletrue)
pset.addPrimitive(while_trueFunc4, [request4], whiletrue)

pset.addPrimitive(wait_forfFuncX, [Xf], wait_forf)
pset.addPrimitive(wait_forfFuncO, [Of], wait_forf)

pset.addPrimitive(request1Func, [O], request1)
pset.addPrimitive(request2Func, [O, O], request2)
pset.addPrimitive(request3Func, [O, O, O], request3)
pset.addPrimitive(request4Func, [O, O, O, O], request4)

pset.addPrimitive(requestf1Func, [Of], requestf1)
pset.addPrimitive(requestf2Func, [Of, Of], requestf2)
pset.addPrimitive(requestf3Func, [Of, Of, Of], requestf3)
pset.addPrimitive(requestf4Func, [Of, Of, Of, Of], requestf4)

pset.addPrimitive(xfFunc, [int, int], Xf)
pset.addPrimitive(ofFunc, [int, int], Of)
pset.addPrimitive(oFunc, [int, int], O)
#pset.addPrimitive(posFunc, [int], int)
pset.addTerminal(0, int)
pset.addTerminal(1, int)
pset.addTerminal(2, int)


# stuff to run:
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin, pset=pset)

toolbox = base.Toolbox()
toolbox.register("expr", gp.genGrow, pset=pset, min_=6, max_=6)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("compile", gp.compile, pset=pset)

toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genGrow, min_=0, max_=2)
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)
toolbox.register("evaluate", evalTestGP)
toolbox.register("select", tools.selTournament, tournsize=3)


def main():
    global n
    n = 50
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
    pop = toolbox.population(n=10)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("Avg", numpy.mean)
    stats.register("Median", numpy.median)
    stats.register("Best", numpy.min)
    stats.register("Worst", numpy.max)

    algorithms.eaSimple(pop, toolbox, cxpb=0.4, mutpb=0.01, ngen=50, stats=stats, halloffame=hof, verbose=True)

    print(hof.__getitem__(0))
    func = toolbox.compile(expr=hof.__getitem__(0))

    print(str(func(0).root))

    return pop, stats, hof


if __name__ == "__main__":
    main()

