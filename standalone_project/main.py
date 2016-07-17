import csv

# Define and Instantiate Solver
class Solver(object):
  def solve(self, x, y):
    solution = x + y
    return solution

solver = Solver()

def read_data():
  data_file = '/data/75821d9915567987edd0ff3271e276c922218c638e05efb2955a32c4526abdd9'
  def to_ints_tuple(row):
    return tuple(map(int, row))
  return map(to_ints_tuple, csv.reader(open(data_file, 'rb'), delimiter=','))

def read_answers():
   answer_file = '/data/3d7219dab4803e82ad97ece9a49fc25c6fd3762a369236d131cb729f32946ff2'
   ans = list(csv.reader(open(answer_file, 'rb'), delimiter=','))
   return map(lambda x: int(x[0]), ans)

# Send problems to solvers
dataset = read_data()
solutions = []
for problem in dataset:
    solutions.append(solver.solve(*problem))

# Evaluate solutions against ground truth
answers = read_answers()
correct_count = 0
for i in xrange(len(dataset)):
    if solutions[i] == answers[i]:
        correct_count = correct_count + 1

accuracy = correct_count / len(dataset)

# Save overall
results = {
    'metric': 'Accuracy',
    'value': accuracy
}

import json
with open('/workspace/overall.json', 'w') as output:
    json.dump(results, output)
