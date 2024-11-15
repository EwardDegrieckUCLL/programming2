from itertools import permutations, pairwise

def find_shortest_path(distance, city_count):
    def get_total_distance(path):
        return sum(distance(a, b) for a,b in pairwise(path))

    all_permutations = permutations(range(1, city_count))
    all_possible_paths = ([0] + list(permutation) + [0] for permutation in all_permutations)

    return min(all_possible_paths, key= get_total_distance)