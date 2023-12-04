from numpy import ndarray


def model(v, t, g, A, C_D, m, p) -> float | ndarray:
    dvdt: float = g - ((p * A * C_D * v ** 2) / (2 * m))
    return dvdt

