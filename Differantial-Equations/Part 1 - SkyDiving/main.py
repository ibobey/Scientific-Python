from matplotlib.widgets import Button, Slider
import matplotlib.pyplot as plt
import seaborn as sns
from SETUP.SetSeabornTheme import *
from ENTITIY.Elements import Elements
from MODELS_FUNCTIONS.Model import model
from MODELS_FUNCTIONS.TerminalVelocity import calculate_terminal_velocity
import numpy as np
from numpy import ndarray
from scipy.integrate import odeint

# Define Variables and Constants
test_elements: Elements = Elements(
    m=80,
    p=1.225,
    A=0.75,
    C_D=0.47,
    v0=0,
    g=9.81,
    t=np.linspace(0, 25, 500)
)

solution: ndarray = odeint(model,
                           y0=test_elements.v0,
                           t=test_elements.t,
                           args=(test_elements.g,
                                 test_elements.A,
                                 test_elements.C_D,
                                 test_elements.m,
                                 test_elements.p,))

terminal_velocity: float = calculate_terminal_velocity(m=test_elements.m,
                            g=test_elements.g,
                            C_D=test_elements.C_D,
                            p=test_elements.p,
                            A=test_elements.A)

figure, axes = plt.subplots(figsize=(10, 6))
figure.subplots_adjust(left=0.25, bottom=0.25)

line, = axes.plot(test_elements.t,
                  solution,
                  lw=2.25,
                  label="f(x)",
                  color="k",
                  alpha=0.75
                  )

line2 = axes.axhline(terminal_velocity,
            alpha=0.45,
            ls="-.",
            label="v-terminal",
            color="#FF00FF",
            lw=1)


# Make a horizontal slider to control the frequency.
ax_C_D = figure.add_axes([0.25, 0.1, 0.65, 0.03])
slider_C_D = Slider(
    ax=ax_C_D,
    label='Drag Coefficient [C_D]',
    valmin=0.01,
    valmax=1,
    valinit=test_elements.C_D,
)

ax_A = figure.add_axes([0.1, 0.25, 0.0225, 0.63])
slider_Area = Slider(
    ax=ax_A,
    label="Area[m2]",
    valmin=0.1,
    valmax=5,
    valinit=test_elements.A,
    orientation="vertical"
)


def update_chart(val):
    test_elements.C_D = slider_C_D.val
    test_elements.A = slider_Area.val

    terminal_velocity: float = calculate_terminal_velocity(m=test_elements.m,
                                                           g=test_elements.g,
                                                           C_D=test_elements.C_D,
                                                           p=test_elements.p,
                                                           A=test_elements.A)

    terminal_velocity_x = test_elements.t
    terminal_velocity_y = np.ones(len(test_elements.t)) * terminal_velocity
    solution: ndarray = odeint(model,
                               y0=test_elements.v0,
                               t=test_elements.t,
                               args=(test_elements.g,
                                     test_elements.A,
                                     test_elements.C_D,
                                     test_elements.m,
                                     test_elements.p,))
    line.set_ydata(solution)
    line2.set_data(terminal_velocity_x, terminal_velocity_y)

    axes.set_ylim(-5, terminal_velocity + 5)
    axes.set_xlim(-1, np.max(test_elements.t) + 2)


    figure.canvas.draw_idle()



slider_Area.on_changed(update_chart)
slider_C_D.on_changed(update_chart)

reset_axes = figure.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(reset_axes, 'Reset', hovercolor='0.975')


def reset_chart(event):
    slider_Area.reset()
    slider_C_D.reset()


button.on_clicked(reset_chart)

axes.grid(True, alpha=0.45, ls="-.")
axes.legend(loc="best")
axes.set_title("Sky Diving Simulation")
axes.set_xlabel("time [s]")
axes.set_ylabel("Velocity [m/s]")
axes.set_ylim(-5, terminal_velocity + 5)
axes.set_xlim(-1, np.max(test_elements.t) + 2)
sns.despine()
plt.show()

print(line)
print(type(line))