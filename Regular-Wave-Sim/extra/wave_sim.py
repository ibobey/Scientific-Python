from regular_wave.RegularWave import RegularWave
import matplotlib.pyplot as plt
import matplotlib.animation as animation
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

reg = RegularWave(sim_data)

fig, ax = plt.subplots(figsize=(16, 9))

line, = ax.plot(reg.x, reg.create_regular_wave(t=0))


def animate(i):
    line.set_ydata(reg.create_regular_wave(t=reg.t_initial + i))  # update the data.
    return line,


ax.axhline(0, c='k', alpha=0.45, ls='--', lw=.75,
           label='Sea Level', color='dodgerblue')

ax.axhline(-reg.d, c='k', alpha=0.45, ls='--', lw=.75,
           label='Sea Bed', color='k')

ax.set_ylim(-reg.d - 2, reg.H + 5)

ax.set_xlabel('Distance of Propagation [m]')
ax.set_ylabel('Water Deepth [m]')
ax.set_title('Airy Wave Velocity')

ax.legend(loc='upper left', ncols=3)
ax.grid(True, alpha=0.45, ls="-.", lw=0.5)

plt.tight_layout()
sns.despine(fig=fig, bottom=True)


ani = animation.FuncAnimation(
    fig, animate, interval=25, blit=False, save_count=50)

plt.show()
