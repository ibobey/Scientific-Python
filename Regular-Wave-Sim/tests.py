import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Function to update the plot for each frame of the animation
def update_quiver(num, Q, sine_line):
    Q.set_UVC(np.cos(num * 0.1), np.sin(num * 0.1))
    sine_line.set_ydata(np.sin(x + num * 0.1))

    return Q, sine_line


# Generate data for quiver plot
X, Y = np.meshgrid(np.arange(-2, 2, 0.2), np.arange(-2, 2, 0.2))
U = np.cos(X)
V = np.sin(Y)

# Generate data for sine wave
x = np.linspace(-2, 2, 100)
y = np.sin(x)

# Create a quiver plot
fig, ax = plt.subplots()
Q = ax.quiver(X, Y, U, V, pivot='mid', scale=10, color='r')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Create a sine line
sine_line, = ax.plot(x, y, 'b-')

# Create the animation
ani = animation.FuncAnimation(fig, update_quiver, frames=range(100), fargs=(Q, sine_line), interval=50)

plt.show()
