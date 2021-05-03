#%%
import numpy as np
#%%
gons = []
gons.append([n * (n + 1) // 2 for n in range(200) if 999 < n * (n + 1) // 2 < 10000])
gons.append([n * n for n in range(200) if 999 < n * n < 10000])
gons.append([n * (3 * n - 1) // 2 for n in range(200) if 999 < n * (3 * n - 1) // 2 < 10000])
gons.append([n * (2 * n - 1) for n in range(200) if 999 < n * (2 * n - 1) < 10000])
gons.append([n * (5 * n - 3) // 2 for n in range(200) if 999 < n * (5 * n - 3) // 2 < 10000])
gons.append([n * (3 * n - 2) for n in range(200) if 999 < n * (3 * n - 2) < 10000])


#%%
all_nr = sorted(set([i for j in range(6) for i in gons[j]]))

#%%
def is_adjacent(i,j, nr_i, nr_j):
    if nr_i in gons[i] and nr_j in gons[j] and nr_j != nr_i and str(nr_i)[2:] == str(nr_j)[:2]:
        # str(nr_i)[2:] == str(nr_j)[:2]
        return 1
    return 0
#%%
adjacency_matrix = {}
for i in range(6):
    for j in range(6):
        adjacency_matrix[((i,j))] = np.array([[is_adjacent(i,j, all_nr[b], all_nr[a]) for a in range(len(all_nr))] for b in range(len(all_nr))])
#%%
from itertools import permutations
all_perm = permutations(range(6))

for perm in all_perm:
    matrix = adjacency_matrix[(perm[0], perm[1])]
    for i in range(1,5):
        matrix = np.dot(matrix, adjacency_matrix[(perm[i], perm[i+1])])
        np.fill_diagonal(matrix, 0)
    matrix = np.dot(matrix, adjacency_matrix[(perm[5], perm[0])])

    if np.trace(matrix) != 0:
        print(perm)
        print(np.transpose(matrix.nonzero()))