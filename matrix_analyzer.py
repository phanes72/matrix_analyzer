import numpy as np
import matplotlib.pyplot as plt

def find_groups(matrix):
    rows, cols = matrix.shape
    visited = np.zeros_like(matrix, dtype=bool)
    groups = []

    def dfs(row, col, group):
        if 0 <= row < rows and 0 <= col < cols and not visited[row, col] and matrix[row, col] == current_number:
            visited[row, col] = True
            group.append((row, col))

            # Check above, below, left, and right (exclude diagonal)
            dfs(row - 1, col, group)
            dfs(row + 1, col, group)
            dfs(row, col - 1, group)
            dfs(row, col + 1, group)

    for current_number in range(1, 10):
        for i in range(rows):
            for j in range(cols):
                if matrix[i, j] == current_number and not visited[i, j]:
                    group = []
                    dfs(i, j, group)
                    if len(group) > 1:
                        groups.append(group)

    return groups

def plot_matrix(matrix, groups):
    plt.imshow(matrix, cmap='viridis')

    for group in groups:
        group = np.array(group)
        plt.plot(group[:, 1], group[:, 0], 'ro-')
        plt.text(group[0, 1], group[0, 0], 'Tumor', color='red', fontsize=8, ha='center', va='center')

    plt.title('MiniMRI Machine')
    plt.show()

# Example usage:
matrix = np.array([[1, 2, 2, 1],
                   [2, 1, 1, 2],
                   [1, 3, 2, 2],
                   [2, 2, 1, 3]])

identified_groups = find_groups(matrix)
plot_matrix(matrix, identified_groups)
