from regular_wave.RegularWave import RegularWave
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

sim_data = {
    'd': 40,
    'H': 2,
    'lambda_': 100,
    't_initial': 0,
    'phi': 0
}
reg = RegularWave(sim_data)

vectors = reg.calculate_vectors(t=0, delta=0)

fig, ax = plt.subplots()

Q = ax.quiver(vectors[0], vectors[1], vectors[2], vectors[3], vectors[4])
ax.set_ylim(-reg.d - 2, reg.H + 2)
sine_line, = ax.plot(vectors[0], vectors[1])


def update(t, Q, sine_line):
    vectors = reg.calculate_vectors(t=t, delta=0)
    Q.set_UVC(vectors[2], vectors[3])
    sine_line.set_data(vectors[0], vectors[1])
    Q.set_offsets(np.column_stack([vectors[0].flatten(), vectors[1].flatten()]))
    return Q, sine_line


ani = animation.FuncAnimation(fig, update, frames=range(250), fargs=(Q, sine_line), interval=25)

plt.show()


