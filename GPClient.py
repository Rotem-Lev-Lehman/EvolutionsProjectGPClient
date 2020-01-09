import copy
import urllib.request
import json

optimal_instance = {
	"t0":"bp.registerBThread(\"AddThirdO(<\" + f[p[0]].x + \",\" + f[p[0]].y + \">,\" + \"<\" + f[p[1]].x + \",\" + f[p[1]].y + \">,\" + \"<\" + f[p[2]].x + \",\" + f[p[2]].y + \">)\", function() {\n\t\twhile (true) {\n\t\t\tbp.sync({ waitFor:[ O(f[p[0]].x, f[p[0]].y) ] });\n\n\t\t\tbp.sync({ waitFor:[ O(f[p[1]].x, f[p[1]].y) ] });\n\n\t\t\tbp.sync({ request:[ O(f[p[2]].x, f[p[2]].y) ] }, 50);\n\t\t}\n\t});",
    "t1":"bp.registerBThread(\"PreventThirdX(<\" + f[p[0]].x + \",\" + f[p[0]].y + \">,\" + \"<\" + f[p[1]].x + \",\" + f[p[1]].y + \">,\" + \"<\" + f[p[2]].x + \",\" + f[p[2]].y + \">)\", function() {\n\t\twhile (true) {\n\t\t\tbp.sync({ waitFor:[ X(f[p[0]].x, f[p[0]].y) ] });\n\n\t\t\tbp.sync({ waitFor:[ X(f[p[1]].x, f[p[1]].y) ] });\n\n\t\t\tbp.sync({ request:[ O(f[p[2]].x, f[p[2]].y) ] }, 40);\n\t\t}\n\t});",
    "t2":"bp.registerBThread(\"PreventFork22X(<\" + f[p[0]].x + \",\" + f[p[0]].y + \">,\" + \"<\" + f[p[1]].x + \",\" + f[p[1]].y + \">)\", function() {\n\t\twhile (true) {\n\t\t\tbp.sync({ waitFor:[ X(f[p[0]].x, f[p[0]].y) ] });\n\n\t\t\tbp.sync({ waitFor:[ X(f[p[1]].x, f[p[1]].y) ] });\n\n\t\t\tbp.sync({ request:[ O(2, 2), O(0,2), O(2,0) ] }, 30);\n\t\t}\n\t});",
    "t3":"bp.registerBThread(\"PreventFork02X(<\" + f[p[0]].x + \",\" + f[p[0]].y + \">,\" + \"<\" + f[p[1]].x + \",\" + f[p[1]].y + \">)\", function() {\n\t\twhile (true) {\n\t\t\tbp.sync({ waitFor:[ X(f[p[0]].x, f[p[0]].y) ] });\n\n\t\t\tbp.sync({ waitFor:[ X(f[p[1]].x, f[p[1]].y) ] });\n\n\t\t\tbp.sync({ request:[ O(0, 2), O(0,0), O(2,2) ] }, 30);\n\t\t}\n\t});",
    "t4":"bp.registerBThread(\"PreventFork20X(<\" + f[p[0]].x + \",\" + f[p[0]].y + \">,\" + \"<\" + f[p[1]].x + \",\" + f[p[1]].y + \">)\", function() {\n\t\twhile (true) {\n\t\t\tbp.sync({ waitFor:[ X(f[p[0]].x, f[p[0]].y) ] });\n\n\t\t\tbp.sync({ waitFor:[ X(f[p[1]].x, f[p[1]].y) ] });\n\n\t\t\tbp.sync({ request:[ O(2, 0), O(0,0), O(2,2) ] }, 30);\n\t\t}\n\t});",
    "t5":"bp.registerBThread(\"PreventFork00X(<\" + f[p[0]].x + \",\" + f[p[0]].y + \">,\" + \"<\" + f[p[1]].x + \",\" + f[p[1]].y + \">)\", function() {\n\t\twhile (true) {\n\t\t\tbp.sync({ waitFor:[ X(f[p[0]].x, f[p[0]].y) ] });\n\n\t\t\tbp.sync({ waitFor:[ X(f[p[1]].x, f[p[1]].y) ] });\n\n\t\t\tbp.sync({ request:[ O(0, 0), O(0,2), O(2,0) ] }, 30);\n\t\t}\n\t});",
    "t6":"bp.registerBThread(\"PreventForkdiagX(<\" + f[p[0]].x + \",\" + f[p[0]].y + \">,\" + \"<\" + f[p[1]].x + \",\" + f[p[1]].y + \">)\", function() {\n\t\twhile (true) {\n\t\t\tbp.sync({ waitFor:[ X(f[p[0]].x, f[p[0]].y) ] });\n\n\t\t\tbp.sync({ waitFor:[ X(f[p[1]].x, f[p[1]].y) ] });\n\n\t\t\tbp.sync({ request:[ O(0, 1), O(1, 0), O(1, 2), O(2, 1) ] }, 30);\n\t\t}\n\t});",
    "t7":"bp.registerBThread(\"Center\", function() {\n\twhile (true) {\n\t\tbp.sync({ request:[ O(1, 1) ] }, 35);\n\t}\n});",
    "t8":"bp.registerBThread(\"Corners\", function() {\n\twhile (true) {\n\t\tbp.sync({ request:[ O(0, 0), O(0, 2), O(2, 0), O(2, 2) ] }, 20);\n\n\t}\n});",
    "t9":"bp.registerBThread(\"Sides\", function() {\n\twhile (true) {\n\t\tbp.sync({ request:[ O(0, 1), O(1, 0), O(1, 2), O(2, 1) ] }, 10);\n\t}\n});"
}

# api-endpoint
URL = "http://localhost:8000/TicTacToe"


def send_request(message):
    app_json = json.dumps(message).encode('utf8')

    req = urllib.request.Request(URL, data=app_json, headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(req)

    return response.read().decode('utf8')


def calculate_fitness(instance, playing_against_random_player):
    instance['rand'] = 1 if playing_against_random_player else 0
    return float(send_request(instance))


def calculate_fitness_for_population(population, playing_against_random_player):
    population['rand'] = 1 if playing_against_random_player else 0
    return send_request(population)


optimal_population = []
for i in range(0, 5):
    copy_of_instance = copy.deepcopy(optimal_instance)
    copy_of_instance['id'] = i
    optimal_population.append(copy_of_instance)

data_to_send = {
    "population": optimal_population
}


print(calculate_fitness_for_population(data_to_send, True))
