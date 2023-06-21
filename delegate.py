import main


def native_id():
    return "Group_SS"


def initialize():
    main.num_nests = 5
    main.max_iter = 1000
    main.pa = 0.25
    return


def convert_input(raw_input):
    # this is because in our code we assume that if there is no edge the weight of that edge will be 0
    raw_input[raw_input == -1] = 0
    main.adj_matrix = raw_input
    main.num_cities = raw_input.shape[0]
    return raw_input


def native_process(data):
    permutation, total_distance = main.solve_tsp_dynamic_programming(data)
    return permutation, total_distance
