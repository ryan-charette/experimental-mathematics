from pathlib import Path

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def generate_random_graph(n, p):
    G = nx.gnp_random_graph(n, p)
    A = nx.adjacency_matrix(G).todense()
    return A

def center_adjacency_matrix(A, p):
    A_centered = A - (p * (1 - np.eye(A.shape[0])))
    return A_centered

def compute_eigenvalues(A):
    eigenvalues = np.linalg.eigvals(A)
    return eigenvalues

def plot_histogram(eigenvalues, n, p, centered=True):
    p = round(p,1)
    plt.hist(eigenvalues, bins=100)
    plt.xlabel('Eigenvalue')
    plt.ylabel('Frequency')
    output_dir = Path('plots')
    output_dir.mkdir(exist_ok=True)
    if centered is True:
        plt.title(f'Histogram of Eigenvalues of A-Centered for G({n}, {p})')
        filename = output_dir / f'centered_n={n}_p={p}.png'
    else:
        plt.title(f'Histogram of Eigenvalues of A for G({n}, {p})')
        filename = output_dir / f'n={n}_p={p}.png'
    plt.savefig(filename)
    plt.clf()

if __name__ == '__main__':
    p = 0.5
    for n in range(10, 101, 10):
        A = generate_random_graph(n, p)
        eigenvalues = compute_eigenvalues(A)
        plot_histogram(eigenvalues, n, p, centered=False)

    for n in range(10, 101, 10):
        A = generate_random_graph(n, p)
        A_centered = center_adjacency_matrix(A, p)
        eigenvalues = compute_eigenvalues(A_centered)
        plot_histogram(eigenvalues, n, p)

    for q in np.linspace(.1, 0.9, 9):
        for n in range(10, 101, 10):
            A = generate_random_graph(n, q)
            A_centered = center_adjacency_matrix(A, q)
            eigenvalues = compute_eigenvalues(A_centered)
            plot_histogram(eigenvalues, n, q)

''' 
3. As \(n\) increases, a distribution of eigenvalues becomes more evident.
In particular, the eigenvalues appear to be approximately normally distributed around 0, with a single outlier
around \(n/2\).
Conjecture. As \(n\to\infty\), the distribution of eigenvalues becomes approximately normally distributed. 
(Central Limit Theorem!)
'''
'''
4. The eigenvalues tend to fall in the interval \((-\sqrt{n},\sqrt{n})\)
and are centered around 0. The eigenvalues appear to be uniformally distributed.
This behavior does not seem to change as \(n\) increases.
'''
'''
5. 
'''