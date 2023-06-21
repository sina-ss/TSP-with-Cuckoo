import numpy as np
import matplotlib.pyplot as plt
import random


num_cities = 5  # Number of cities
num_nests = 100  # Number of nests
max_iter = 10  # Maximum number of iterations
pa = 0.25  # Fraction of worst nests to abandon

# Initialization
nests = [np.random.permutation(num_cities) for _ in range(num_nests)]

# Define adjacency matrix with random distances in the range 1-100
adj_matrix = np.array(
    [
        [0, 20, 30, 10, 50],
        [20, 0, 40, 60, 70],
        [30, 40, 0, 80, 90],
        [10, 60, 80, 0, 100],
        [50, 70, 90, 100, 0],
    ]
)


# Function to calculate total distance
def path_dist(path):
    return sum(adj_matrix[path[i - 1], path[i]] for i in range(num_cities))


# Function to generate a new solution (path)
def get_new_path(path):
    path = path.copy()
    i, j = random.sample(range(num_cities), 2)  # Pick two cities
    path[i], path[j] = path[j], path[i]  # Swap them
    return path


# Function to replace worst nests
def replace_worst_nests(nests, new_nests):
    # Calculate nest qualities
    nest_qualities = [path_dist(nest) for nest in nests]
    # Get indices of worst nests
    worst_nests = np.argsort(nest_qualities)[-int(pa * num_nests) :]
    # Replace worst nests with new ones
    for i in worst_nests:
        nests[i] = new_nests[i]
    return nests


def solve_tsp_dynamic_programming():
    global nests
    for _ in range(max_iter):
        # Generate new solutions
        new_nests = [get_new_path(nest) for nest in nests]
        # Replace nests if new solution is better
        for i in range(num_nests):
            if path_dist(new_nests[i]) < path_dist(nests[i]):
                nests[i] = new_nests[i]
        # Replace worst nests with new, random ones
        nests = replace_worst_nests(
            nests, [np.random.permutation(num_cities) for _ in range(num_nests)]
        )
    # Find the best path
    best_path = min(nests, key=path_dist)

    print("Best path:", best_path)
    print("Total distance:", path_dist(best_path))
    return (best_path, path_dist(best_path))


solve_tsp_dynamic_programming()
