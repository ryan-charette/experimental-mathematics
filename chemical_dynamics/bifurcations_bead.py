import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Define the system of ODEs
def system(t, y, gamma):
    x, y_ = y
    dxdt = 10 - x - 4 * x * y_ / (1 + x**2)
    dydt = gamma * x - gamma * x * y_ / (1 + x**2)
    return [dxdt, dydt]

# Plot the nullclines and directional field
def plot_directional_field_and_nullclines(gamma):
    x = np.linspace(0, 12, 20)  # Reduced grid density for arrows
    y = np.linspace(0, 12, 20)  # Reduced grid density for arrows
    
    X, Y = np.meshgrid(x, y)
    U, V = np.zeros(X.shape), np.zeros(Y.shape)

    DX = 10 - X - 4 * X * Y / (1 + X**2)
    DY = gamma * X - gamma * X * Y / (1 + X**2)

    # Normalize arrows for better visualization
    N = np.sqrt(DX**2 + DY**2)
    U = DX/N
    V = DY/N

    # Plotting directional field with larger arrows
    plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=2.5, alpha=0.5)  # Reduced scale value
    
    # Plotting nullclines using a denser grid for smoothness
    dense_x = np.linspace(0, 12, 400)
    plt.plot(dense_x, (10-dense_x) * (1+dense_x**2) / (4*dense_x), 'r-', label="dx/dt=0")
    plt.plot(dense_x, gamma * dense_x / (gamma + dense_x), 'b-', label="dy/dt=0")
    
    # Add the rectangle
    rectangle = Rectangle((9, 0), 2, 2, fill=False, edgecolor='green', linewidth=1.5)
    plt.gca().add_patch(rectangle)
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title(f"Trapping Region for γ={gamma}")
    plt.grid(True)
    plt.xlim([0, 12])
    plt.ylim([0, 12])
    plt.show()

gamma_value = 1.0  # You can change the gamma value as needed
plot_directional_field_and_nullclines(gamma_value)
