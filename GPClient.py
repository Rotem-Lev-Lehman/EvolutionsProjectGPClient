import urllib.request
import json
"""
optimal_instance = {
	"t0":"bp.registerBThread(\"AddThirdO(<\" + f[p[0]].x + \",\" + f[p[0]].y + \">,\" + \"<\" + f[p[1]].x + \",\" + f[p[1]].y + \">,\" + \"<\" + f[p[2]].x + \",\" + f[p[2]].y + \">)\", function() {while (true) {bp.sync({ waitFor:[ O(f[p[0]].x, f[p[0]].y) ] });bp.sync({ waitFor:[ O(f[p[1]].x, f[p[1]].y) ] });bp.sync({ request:[ O(f[p[2]].x, f[p[2]].y) ] }, 50);}});",
    "t1":"bp.registerBThread(\"PreventThirdX(<\" + f[p[0]].x + \",\" + f[p[0]].y + \">,\" + \"<\" + f[p[1]].x + \",\" + f[p[1]].y + \">,\" + \"<\" + f[p[2]].x + \",\" + f[p[2]].y + \">)\", function() {while (true) {bp.sync({ waitFor:[ X(f[p[0]].x, f[p[0]].y) ] });bp.sync({ waitFor:[ X(f[p[1]].x, f[p[1]].y) ] });bp.sync({ request:[ O(f[p[2]].x, f[p[2]].y) ] }, 40);}});",
    "t2":"bp.registerBThread(\"PreventFork22X(<\" + f[p[0]].x + \",\" + f[p[0]].y + \">,\" + \"<\" + f[p[1]].x + \",\" + f[p[1]].y + \">)\", function() {while (true) {bp.sync({ waitFor:[ X(f[p[0]].x, f[p[0]].y) ] });bp.sync({ waitFor:[ X(f[p[1]].x, f[p[1]].y) ] });bp.sync({ request:[ O(2, 2), O(0,2), O(2,0) ] }, 30);}});",
    "t3":"bp.registerBThread(\"PreventFork02X(<\" + f[p[0]].x + \",\" + f[p[0]].y + \">,\" + \"<\" + f[p[1]].x + \",\" + f[p[1]].y + \">)\", function() {while (true) {bp.sync({ waitFor:[ X(f[p[0]].x, f[p[0]].y) ] });bp.sync({ waitFor:[ X(f[p[1]].x, f[p[1]].y) ] });bp.sync({ request:[ O(0, 2), O(0,0), O(2,2) ] }, 30);}});",
    "t4":"bp.registerBThread(\"PreventFork20X(<\" + f[p[0]].x + \",\" + f[p[0]].y + \">,\" + \"<\" + f[p[1]].x + \",\" + f[p[1]].y + \">)\", function() {while (true) {bp.sync({ waitFor:[ X(f[p[0]].x, f[p[0]].y) ] });bp.sync({ waitFor:[ X(f[p[1]].x, f[p[1]].y) ] });bp.sync({ request:[ O(2, 0), O(0,0), O(2,2) ] }, 30);}});",
    "t5":"bp.registerBThread(\"PreventFork00X(<\" + f[p[0]].x + \",\" + f[p[0]].y + \">,\" + \"<\" + f[p[1]].x + \",\" + f[p[1]].y + \">)\", function() {while (true) {bp.sync({ waitFor:[ X(f[p[0]].x, f[p[0]].y) ] });bp.sync({ waitFor:[ X(f[p[1]].x, f[p[1]].y) ] });bp.sync({ request:[ O(0, 0), O(0,2), O(2,0) ] }, 30);}});",
    "t6":"bp.registerBThread(\"PreventForkdiagX(<\" + f[p[0]].x + \",\" + f[p[0]].y + \">,\" + \"<\" + f[p[1]].x + \",\" + f[p[1]].y + \">)\", function() {while (true) {bp.sync({ waitFor:[ X(f[p[0]].x, f[p[0]].y) ] });bp.sync({ waitFor:[ X(f[p[1]].x, f[p[1]].y) ] });bp.sync({ request:[ O(0, 1), O(1, 0), O(1, 2), O(2, 1) ] }, 30);}});",
    "t7":"bp.registerBThread(\"Center\", function() {while (true) {bp.sync({ request:[ O(1, 1) ] }, 35);}});",
    "t8":"bp.registerBThread(\"Corners\", function() {while (true) {bp.sync({ request:[ O(0, 0), O(0, 2), O(2, 0), O(2, 2) ] }, 20);}});",
    "t9":"bp.registerBThread(\"Sides\", function() {while (true) {bp.sync({ request:[ O(0, 1), O(1, 0), O(1, 2), O(2, 1) ] }, 10);}});"
}
"""
""" tied about 10 games vs. optimal player.
best_instance_first_iteration_vs_random = {
  "t0": "bp.registerBThread(\"AddThirdO(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">,\"+\"<\"+f[p[2]].x+\",\"+f[p[2]].y+\">)\",function(){while(true){bp.sync({waitFor:[O(f[p[0]].x,f[p[0]].y)]});bp.sync({waitFor:[O(f[p[1]].x,f[p[1]].y)]});bp.sync({request:[O(f[p[1]].x,f[p[1]].y),O(f[p[0]].x,f[p[2]].y),O(f[p[1]].x,f[p[1]].y),O(f[p[2]].x,f[p[2]].y)]},50);}});",
  "t1": "bp.registerBThread(\"PreventThirdX(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">,\"+\"<\"+f[p[2]].x+\",\"+f[p[2]].y+\">)\",function(){while(true){bp.sync({waitFor:[O(f[p[0]].x,f[p[0]].y)]});bp.sync({waitFor:[O(f[p[2]].x,f[p[1]].y)]});bp.sync({request:[O(f[p[1]].x,f[p[1]].y),O(f[p[0]].x,f[p[2]].y),O(f[p[1]].x,f[p[1]].y),O(f[p[2]].x,f[p[2]].y)]},40);}});",
  "t2": "bp.registerBThread(\"PreventFork22X(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">)\",function(){while(true){bp.sync({request:[O(1,2),O(0,0),O(2,1)]},30);}});",
  "t3": "bp.registerBThread(\"PreventFork02X(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">)\",function(){while(true){bp.sync({waitFor:[X(f[p[0]].x,f[p[0]].y)]});bp.sync({request:[O(2,2),O(0,1),O(0,2)]},30);}});",
  "t4": "bp.registerBThread(\"PreventFork20X(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">)\",function(){while(true){bp.sync({request:[O(2,1),O(0,1),O(2,0)]},30);}});",
  "t5": "bp.registerBThread(\"PreventFork00X(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">)\",function(){while(true){bp.sync({request:[O(1,1),O(2,0),O(0,0),O(0,0)]},30);}});",
  "t6": "bp.registerBThread(\"PreventForkdiagX(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">)\",function(){while(true){bp.sync({waitFor:[X(f[p[0]].x,f[p[0]].y)]});bp.sync({waitFor:[X(f[p[0]].x,f[p[0]].y)]});bp.sync({request:[O(0,0)]},30);}});",
  "t7": "bp.registerBThread(\"Center\",function(){while(true){bp.sync({request:[O(0,0),O(0,2),O(2,0),O(2,0)]},35);}});",
  "t8": "bp.registerBThread(\"Corners\",function(){while(true){bp.sync({request:[O(0,2),O(2,2),O(2,2)]},20);}});",
  "t9": "bp.registerBThread(\"Sides\",function(){while(true){bp.sync({request:[O(2,1)]},10);}});"
}
"""
""" better, this time it tied about 20 games vs. optimal player.
best_instance_second_iteration_vs_random = {
  "t0": "bp.registerBThread(\"AddThirdO(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">,\"+\"<\"+f[p[2]].x+\",\"+f[p[2]].y+\">)\",function(){while(true){bp.sync({waitFor:[O(f[p[0]].x,f[p[1]].y)]});bp.sync({waitFor:[X(f[p[1]].x,f[p[1]].y)]});bp.sync({request:[O(f[p[0]].x,f[p[1]].y)]},50);}});",
  "t1": "bp.registerBThread(\"PreventThirdX(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">,\"+\"<\"+f[p[2]].x+\",\"+f[p[2]].y+\">)\",function(){while(true){bp.sync({waitFor:[X(f[p[2]].x,f[p[0]].y)]});bp.sync({waitFor:[X(f[p[1]].x,f[p[1]].y)]});bp.sync({request:[O(f[p[1]].x,f[p[0]].y),O(f[p[2]].x,f[p[0]].y),O(f[p[0]].x,f[p[0]].y),O(f[p[1]].x,f[p[2]].y)]},40);}});",
  "t2": "bp.registerBThread(\"PreventFork22X(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">)\",function(){while(true){bp.sync({waitFor:[X(f[p[0]].x,f[p[0]].y)]});bp.sync({waitFor:[X(f[p[0]].x,f[p[0]].y)]});bp.sync({request:[O(2,0),O(0,2),O(0,2),O(2,0)]},30);}});",
  "t3": "bp.registerBThread(\"PreventFork02X(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">)\",function(){while(true){bp.sync({request:[O(0,1)]},30);}});",
  "t4": "bp.registerBThread(\"PreventFork20X(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">)\",function(){while(true){bp.sync({waitFor:[X(f[p[0]].x,f[p[0]].y)]});bp.sync({waitFor:[X(f[p[1]].x,f[p[1]].y)]});bp.sync({request:[O(1,0)]},30);}});",
  "t5": "bp.registerBThread(\"PreventFork00X(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">)\",function(){while(true){bp.sync({request:[O(0,2),O(2,2),O(0,1)]},30);}});",
  "t6": "bp.registerBThread(\"PreventForkdiagX(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">)\",function(){while(true){bp.sync({request:[O(2,2),O(0,1),O(2,0),O(2,2)]},30);}});",
  "t7": "bp.registerBThread(\"Center\",function(){while(true){bp.sync({request:[O(1,1)]},35);}});",
  "t8": "bp.registerBThread(\"Corners\",function(){while(true){bp.sync({request:[O(0,2),O(2,2),O(0,1)]},20);}});",
  "t9": "bp.registerBThread(\"Sides\",function(){while(true){bp.sync({request:[O(0,1),O(0,0)]},10);}});"
}
"""
""" better, this time it tied about 40 games vs. optimal player. this is the third experiment conducted
best_instance_first_iteration_vs_random_and_optimal = {
  "t0": "bp.registerBThread(\"AddThirdO(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">,\"+\"<\"+f[p[2]].x+\",\"+f[p[2]].y+\">)\",function(){while(true){bp.sync({waitFor:[X(f[p[1]].x,f[p[0]].y)]});bp.sync({waitFor:[X(f[p[2]].x,f[p[1]].y)]});bp.sync({request:[O(f[p[1]].x,f[p[0]].y),O(f[p[0]].x,f[p[1]].y),O(f[p[2]].x,f[p[2]].y)]},50);}});",
  "t1": "bp.registerBThread(\"PreventThirdX(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">,\"+\"<\"+f[p[2]].x+\",\"+f[p[2]].y+\">)\",function(){while(true){bp.sync({waitFor:[X(f[p[1]].x,f[p[0]].y)]});bp.sync({waitFor:[X(f[p[2]].x,f[p[1]].y)]});bp.sync({request:[O(f[p[1]].x,f[p[0]].y),O(f[p[0]].x,f[p[1]].y),O(f[p[2]].x,f[p[2]].y)]},40);}});",
  "t2": "bp.registerBThread(\"PreventFork22X(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">)\",function(){while(true){bp.sync({request:[O(1,0),O(1,1),O(0,0),O(0,2)]},30);}});",
  "t3": "bp.registerBThread(\"PreventFork02X(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">)\",function(){while(true){bp.sync({waitFor:[X(f[p[1]].x,f[p[0]].y)]});bp.sync({waitFor:[X(f[p[1]].x,f[p[1]].y)]});bp.sync({request:[O(0,0),O(1,2),O(2,2),O(1,2)]},30);}});",
  "t4": "bp.registerBThread(\"PreventFork20X(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">)\",function(){while(true){bp.sync({waitFor:[X(f[p[1]].x,f[p[0]].y)]});bp.sync({request:[O(2,1),O(1,2)]},30);}});",
  "t5": "bp.registerBThread(\"PreventFork00X(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">)\",function(){while(true){bp.sync({request:[O(2,2),O(2,1),O(2,2)]},30);}});",
  "t6": "bp.registerBThread(\"PreventForkdiagX(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">)\",function(){while(true){bp.sync({request:[O(1,0),O(2,1),O(0,0),O(0,2)]},30);}});",
  "t7": "bp.registerBThread(\"Center\",function(){while(true){bp.sync({request:[O(0,2),O(2,2),O(1,1)]},35);}});",
  "t8": "bp.registerBThread(\"Corners\",function(){while(true){bp.sync({request:[O(0,0),O(1,2),O(0,1),O(2,1)]},20);}});",
  "t9": "bp.registerBThread(\"Sides\",function(){while(true){bp.sync({request:[O(1,2),O(0,1),O(1,1),O(2,1)]},10);}});"
}
"""
""" better, this time it tied 50 games vs. optimal player (at all trials). this is the fourth experiment conducted
best_instance_second_iteration_vs_random_and_optimal = {
  "t0": "bp.registerBThread(\"AddThirdO(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">,\"+\"<\"+f[p[2]].x+\",\"+f[p[2]].y+\">)\",function(){while(true){bp.sync({waitFor:[O(f[p[2]].x,f[p[2]].y)]});bp.sync({waitFor:[O(f[p[0]].x,f[p[0]].y)]});bp.sync({request:[O(f[p[0]].x,f[p[0]].y),O(f[p[1]].x,f[p[1]].y),O(f[p[0]].x,f[p[0]].y)]},50);}});",
  "t1": "bp.registerBThread(\"PreventThirdX(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">,\"+\"<\"+f[p[2]].x+\",\"+f[p[2]].y+\">)\",function(){while(true){bp.sync({waitFor:[X(f[p[1]].x,f[p[2]].y)]});bp.sync({waitFor:[X(f[p[0]].x,f[p[0]].y)]});bp.sync({request:[O(f[p[0]].x,f[p[1]].y),O(f[p[2]].x,f[p[2]].y),O(f[p[1]].x,f[p[1]].y)]},40);}});",
  "t2": "bp.registerBThread(\"PreventFork22X(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">)\",function(){while(true){bp.sync({waitFor:[X(f[p[1]].x,f[p[1]].y)]});bp.sync({request:[O(1,1)]},30);}});",
  "t3": "bp.registerBThread(\"PreventFork02X(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">)\",function(){while(true){bp.sync({request:[O(0,0),O(2,0),O(2,0)]},30);}});",
  "t4": "bp.registerBThread(\"PreventFork20X(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">)\",function(){while(true){bp.sync({request:[O(0,0),O(2,0),O(2,0)]},30);}});",
  "t5": "bp.registerBThread(\"PreventFork00X(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">)\",function(){while(true){bp.sync({waitFor:[X(f[p[1]].x,f[p[1]].y)]});bp.sync({waitFor:[X(f[p[1]].x,f[p[1]].y)]});bp.sync({request:[O(2,0),O(2,2),O(2,0),O(2,2)]},30);}});",
  "t6": "bp.registerBThread(\"PreventForkdiagX(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">)\",function(){while(true){bp.sync({waitFor:[X(f[p[1]].x,f[p[1]].y)]});bp.sync({waitFor:[X(f[p[1]].x,f[p[1]].y)]});bp.sync({request:[O(2,1),O(1,0)]},30);}});",
  "t7": "bp.registerBThread(\"Center\",function(){while(true){bp.sync({request:[O(1,1)]},35);}});",
  "t8": "bp.registerBThread(\"Corners\",function(){while(true){bp.sync({request:[O(1,1)]},20);}});",
  "t9": "bp.registerBThread(\"Sides\",function(){while(true){bp.sync({request:[O(1,1),O(0,0),O(2,0)]},10);}});"
}
"""
"""
test = {
  "t0": "bp.registerBThread(\"AddThirdO(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">,\"+\"<\"+f[p[2]].x+\",\"+f[p[2]].y+\">)\",function(){while(true){bp.sync({waitFor:[O(f[p[2]].x,f[p[2]].y)]});bp.sync({waitFor:[O(f[p[0]].x,f[p[0]].y)]});bp.sync({request:[O(f[p[1]].x,f[p[1]].y),O(f[p[1]].x,f[p[1]].y),O(f[p[0]].x,f[p[0]].y)]},50);}});",
  "t1": "bp.registerBThread(\"PreventThirdX(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">,\"+\"<\"+f[p[2]].x+\",\"+f[p[2]].y+\">)\",function(){while(true){bp.sync({waitFor:[X(f[p[1]].x,f[p[2]].y)]});bp.sync({waitFor:[X(f[p[0]].x,f[p[0]].y)]});bp.sync({request:[O(f[p[0]].x,f[p[1]].y),O(f[p[2]].x,f[p[1]].y),O(f[p[1]].x,f[p[2]].y)]},40);}});",
  "t2": "bp.registerBThread(\"PreventFork22X(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">)\",function(){while(true){bp.sync({waitFor:[X(f[p[1]].x,f[p[1]].y)]});bp.sync({request:[O(0,0)]},30);}});",
  "t3": "bp.registerBThread(\"PreventFork02X(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">)\",function(){while(true){bp.sync({request:[O(0,0),O(2,0),O(2,0)]},30);}});",
  "t4": "bp.registerBThread(\"PreventFork20X(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">)\",function(){while(true){bp.sync({waitFor:[X(f[p[1]].x,f[p[1]].y)]});bp.sync({waitFor:[X(f[p[0]].x,f[p[1]].y)]});bp.sync({request:[O(1,0),O(0,0),O(2,0)]},30);}});",
  "t5": "bp.registerBThread(\"PreventFork00X(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">)\",function(){while(true){bp.sync({waitFor:[X(f[p[1]].x,f[p[1]].y)]});bp.sync({waitFor:[X(f[p[0]].x,f[p[1]].y)]});bp.sync({request:[O(2,2),O(2,2),O(2,0),O(2,2)]},30);}});",
  "t6": "bp.registerBThread(\"PreventForkdiagX(<\"+f[p[0]].x+\",\"+f[p[0]].y+\">,\"+\"<\"+f[p[1]].x+\",\"+f[p[1]].y+\">)\",function(){while(true){bp.sync({waitFor:[X(f[p[1]].x,f[p[1]].y)]});bp.sync({waitFor:[X(f[p[0]].x,f[p[1]].y)]});bp.sync({request:[O(2,1),O(1,0)]},30);}});",
  "t7": "bp.registerBThread(\"Center\",function(){while(true){bp.sync({request:[O(1,1)]},35);}});",
  "t8": "bp.registerBThread(\"Corners\",function(){while(true){bp.sync({request:[O(1,1),O(2,2),O(1,2)]},20);}});",
  "t9": "bp.registerBThread(\"Sides\",function(){while(true){bp.sync({request:[O(0,1),O(2,2)]},10);}});"
}
"""

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


#print(calculate_fitness(test, False))

"""
import copy
optimal_population = []
for i in range(0, 5):
    copy_of_instance = copy.deepcopy(optimal_instance)
    copy_of_instance['id'] = i
    optimal_population.append(copy_of_instance)

data_to_send = {
    "population": optimal_population
}


print(calculate_fitness_for_population(data_to_send, True))
"""