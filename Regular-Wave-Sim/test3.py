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


def calculate_all_vectors(reg_: RegularWave, t: float):
    s1 = reg_.calculate_vectors(t=t, delta=0)
    s2 = reg_.calculate_vectors(t=t, delta=-5)
    s3 = reg_.calculate_vectors(t=t, delta=-10)
    s4 = reg_.calculate_vectors(t=t, delta=-15)
    s5 = reg_.calculate_vectors(t=t, delta=-20)
    s6 = reg_.calculate_vectors(t=t, delta=-25)
    s7 = reg_.calculate_vectors(t=t, delta=-30)
    s8 = reg_.calculate_vectors(t=t, delta=-33.5)
    s9 = reg_.calculate_vectors(t=t, delta=-37.5)
    return np.hstack((s1, s2, s3, s4, s5, s6, s7, s8, s9))


vectors = calculate_all_vectors(reg_=reg, t=0)

fig, ax = plt.subplots()

Q = ax.quiver(vectors[0], vectors[1], vectors[2], vectors[3], vectors[4])
ax.set_ylim(-reg.d - 2, reg.H + 2)
sine_line, = ax.plot(vectors[0][:100], vectors[1][:100])


def update(t, Q, sine_line):
    vectors = calculate_all_vectors(reg_=reg, t=t)
    Q.set_offsets(np.column_stack([vectors[0].flatten(), vectors[1].flatten()]))
    Q.set_UVC(vectors[2], vectors[3])
    sine_line.set_data(vectors[0][:100], vectors[1][:100])

    return Q, sine_line


ani = animation.FuncAnimation(fig, update, frames=range(1000), fargs=(Q, sine_line), interval=25)

plt.show()
