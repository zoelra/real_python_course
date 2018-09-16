from random import random

candidate_a = 0
candidate_b = 0

for elections in range(0, 10000):
    result = random()
    print(result)
    candidate_a = 0
    candidate_b = 0

    if result + .87 >= 1:
        candidate_a += 1
    else:
        candidate_b += 1

    if result + .65 >= 1:
        candidate_a += 1
    else:
        candidate_b += 1

    if result + .17 >= 1:
        candidate_a += 1
    else:
        candidate_b += 1

print("Candidate A won {} elections and Candidate B won {} elections".format(candidate_a, candidate_b))
