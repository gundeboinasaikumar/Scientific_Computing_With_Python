import copy
import random
from collections import Counter

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color]*count)

    def draw(self, num):
        draw_result =[]
        for i in range(min(num,len(self.contents))):
            curr = random.choice(self.contents)
            self.contents.remove(curr)
            draw_result.append(curr)
        return draw_result
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M =0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        experiment_result = Counter(hat_copy.draw(num_balls_drawn))
        if all([experiment_result[color]>=count for color, count in expected_balls.items()]) :
            M += 1
    return M/num_experiments

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)