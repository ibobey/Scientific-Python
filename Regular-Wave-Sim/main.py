from regular_wave.RegularWave import RegularWave
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import seaborn as sns

sns.set_theme(context='notebook',
              style='white',
              palette='bright')

sim_data = {
    'd': 40,
    'H': 2,
    'lambda_': 100,
    't_initial': 0,
    'phi': 0
}

STEP = 2

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

fig, ax = plt.subplots(figsize=(16, 9))

Q = ax.quiver(vectors[0][::STEP],
              vectors[1][::STEP],
              vectors[2][::STEP],
              vectors[3][::STEP],
              vectors[4][::STEP],
              cmap='viridis')
ax.set_ylim(-reg.d - 2, reg.H + 5)
sine_line, = ax.plot(vectors[0][:100], vectors[1][:100], label='wave', lw=3.5, alpha=0.75)


def update(t, Q, sine_line):
    vectors = calculate_all_vectors(reg_=reg, t=t)
    Q.set_offsets(np.column_stack([vectors[0][::STEP].flatten(), vectors[1][::STEP].flatten()]))
    Q.set_UVC(vectors[2][::STEP], vectors[3][::STEP])
    sine_line.set_data(vectors[0][:100], vectors[1][:100])

    return Q, sine_line


ani = animation.FuncAnimation(fig, update, frames=range(500), fargs=(Q, sine_line), interval=30)


ax.axhline(0, c='k', alpha=0.45, ls='--', lw=.75,
            label='Sea Level', color='dodgerblue')

ax.axhline(-reg.d, c='k', alpha=0.45, ls='--', lw=.75,
            label='Sea Bed', color='k')
ax.set_xlabel('Distance of Propagation [m]')
ax.set_ylabel('Water Deepth [m]')
ax.set_title('Airy Wave Velocity')

ax.legend(loc='best', ncols=3)
ax.grid(True, alpha=0.65, ls="-.", lw=0.5)
cbar = fig.colorbar(Q)
sns.despine(bottom=True)
plt.tight_layout()


writergif = animation.PillowWriter(fps=30)
ani.save("test3.gif", writer=writergif)