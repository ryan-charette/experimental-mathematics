import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from math import comb

def generate_random_graph(n, m):
    G = nx.gnm_random_graph(n, m)
    A = nx.adjacency_matrix(G).todense()
    return A

def center_adjacency_matrix(A, p):
    A_centered = A - (p * (1 - np.eye(A.shape[0])))
    return A_centered

def compute_eigenvalues(A):
    eigenvalues = np.linalg.eigvals(A)
    return eigenvalues

def plot_histogram(eigenvalues, n, m, o):
    plt.hist(eigenvalues, bins=100)
    plt.title(f'Histogram of Eigenvalues of A-Centered G({n}, {m}): p={p}')
    plt.xlabel('Eigenvalue')
    plt.ylabel('Frequency')
    plt.show()

if __name__ == '__main__':
    m_values = [10, 20, 300, 50, 75, 100, 150, 200, 300, 10] # Adjust this list to set the desired number of edges for each graph
    for i, n in enumerate(range(10, 101, 10)):
        m = m_values[i]
        p = m / comb(n, 2)
        A = generate_random_graph(n, m)
        A_centered = center_adjacency_matrix(A, p)
        eigenvalues = compute_eigenvalues(A_centered)
        plot_histogram(eigenvalues, n, m, p)
