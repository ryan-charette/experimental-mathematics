import numpy as np
import matplotlib.pyplot as plt

def g(u, h, c):
    return u * (1 - u) - (h * u) / (1 + c * u)

def g_prime(u, h, c):
    return 1 - 2*u + h*(c-4)/((1+c*u)**2)

h_values = np.linspace(0, 3, 1000)
c = 4

equilibrium_points = []
stable_equilibria = []
unstable_equilibria = []

for h in h_values:
    u_values = np.linspace(0, 1.5, 1000)
    du = u_values[1] - u_values[0]
    
    for i in range(1, len(u_values)):
        if g(u_values[i-1], h, c) * g(u_values[i], h, c) < 0:
            u_eq = u_values[i-1] + (u_values[i] - u_values[i-1]) / (g(u_values[i], h, c) - g(u_values[i-1], h, c)) * (0 - g(u_values[i-1], h, c))
            equilibrium_points.append((h, u_eq))
            
            if g_prime(u_eq, h, c) < 0:
                stable_equilibria.append((h, u_eq))
            else:
                unstable_equilibria.append((h, u_eq))

h_points, u_points = zip(*equilibrium_points)
h_stable, u_stable = zip(*stable_equilibria)
h_unstable, u_unstable = zip(*unstable_equilibria)

plt.figure(figsize=(10, 8))
plt.scatter(h_stable, u_stable, s=2, color='blue', label='Stable Equilibria')
plt.scatter(h_unstable, u_unstable, s=2, color='red', label='Unstable Equilibria')
plt.axhline(y=1/8, color='green', linestyle='--', label='$u_0 = 1/8$')
plt.title("Bifurcation Diagram with $c=4$")
plt.xlabel('h')
plt.ylabel('u')
plt.legend()
plt.grid(True)
plt.show()
