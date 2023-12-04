from numpy import sqrt


def calculate_terminal_velocity(m: float, g: float, C_D: float, p: float, A: float) -> float:
    terminal_velocity: float = sqrt(
        (2 * m * g) / (p * A * C_D)
    )
    return terminal_velocity
