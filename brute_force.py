import math
import time


def tsp_brute(edges, starting_point):
    # Creates a list with all the nodes except for the starting point
    nodes = []
    n = len(edges[0])
    fact = math.factorial(n - 1)
    start_time = time.time()
    for i in range(n):
        if i != starting_point:
            nodes.append(i)

    best_path = []
    best_cost = float('inf')
    i = 1
    for path in perms(nodes, n - 1):
        path_cost = 0
        u = starting_point
        for node in path:
            v = node
            path_cost += edges[u][v]
            u = v
        path_cost += edges[u][starting_point]

        if path_cost < best_cost:
            best_cost = path_cost
            best_path = path
        print_schedule = 7877
        if i == print_schedule:
            stop_time = time.time()
            time_passed = stop_time - start_time
            expected_time = fact * time_passed / print_schedule
            print(f'The expected time to completion is: {expected_time / (3600 * 24* 365 * 1000)} millennia')
        if i % print_schedule == 0:
            print(f'\rProgress: {i} of {fact}', end='')
        i += 1

    best_path.append(starting_point)
    best_path.insert(0, starting_point)
    return best_path, best_cost


def print_list(list):
    for ele in list:
        print(f'{ele:.0f},', end=' ')
    print()


def perms(num_list: list[int], size):
    def swap(u, v):
        temp = num_list[v]
        num_list[v] = num_list[u]
        num_list[u] = temp

    if size == 1:
        yield num_list
    for i in range(size):
        yield from perms(num_list, size - 1)
        if size % 2 == 1:
            swap(0, size - 1)
        else:
            swap(i, size - 1)


def get_adj_matrix(file_name):
    file = open(file_name, 'r')
    for line in file:
        if line[0] == 'D':
            n = int(line.split()[2])
            break
    adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
    cords = []
    for line in file:
        if line[0].isdigit():
            _, x, y = line.split()
            cords.append((float(x), float(y)))

    for u in range(n):
        for v in range(n):
            distance_x = math.fabs(cords[u][0] - cords[v][0])
            distance_y = math.fabs(cords[u][1] - cords[v][1])
            adj_matrix[u][v] = \
                math.sqrt(distance_x * distance_x + distance_y + distance_y)
    return adj_matrix


def main():
    matrix = [
        [0, 3, 4, 2, 7],
        [3, 0, 4, 6, 3],
        [4, 4, 0, 5, 8],
        [2, 6, 5, 0, 6],
        [7, 3, 8, 6, 0]
    ]

    best_path, best_cost = tsp_brute(matrix, 0)
    print(f'The best cost is: {best_cost:.2f}')
    print('The best path is: ', end=' ')
    print_list(best_path)


main()
