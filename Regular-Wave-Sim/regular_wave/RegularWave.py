import numpy as np
from numpy import pi, cos, sin, tanh, sinh, cosh
from numpy import deg2rad
from numpy import sqrt, power
from numpy import linspace
from numpy import ndarray


class RegularWave:
    d: float
    H: float
    A: float
    lambda_: float
    k: float
    omega: float
    T: float
    phi: float

    t_initial: float

    __x: ndarray

    @property
    def x(self) -> ndarray | None:
        if self.__x is not None:
            return self.__x
        else:
            print('x cannot be None')
            return None

    @x.setter
    def x(self, value: ndarray):
        self.__x = value

    def __init__(self, data: dict) -> None:
        self.d: float = data.get('d')
        self.H: float = data.get('H')
        self.lambda_: float = data.get('lambda_')
        self.t_initial: float = data.get('t_initial')
        self.phi: float = data.get('phi')

        self._setup()

    def _setup(self) -> None:
        try:
            self.k = (2 * pi) / self.lambda_
            self.omega = self.__dispersion()
            self.__x = linspace(0, self.lambda_, 100, endpoint=True)
            self.A = self.H / 2
            self.T = (2 * pi) / self.omega

        except Exception:
            print('Error initializing regular wave')
            raise Exception('A')

    def __dispersion(self, g=9.81) -> float:
        return deg2rad(sqrt(g * self.k * tanh(self.k * self.d)))

    def create_regular_wave(self, t: float = 0) -> ndarray:
        return self.A * cos(self.omega * t - self.k * self.__x + self.phi)

    def __calculate_u_w(self, z: ndarray, t: float) -> tuple[ndarray, ndarray]:
        u: ndarray = ((self.omega * self.A) / sinh(self.k * self.d)) * cosh(self.k * (self.d + z)) * cos(
            self.omega * t - self.k * self.__x)
        w: ndarray = ((self.omega * self.A) / sinh(self.k * self.d)) * sinh(self.k * (self.d + z)) * sin(
            self.omega * t - self.k * self.__x)

        return u, w

    def calculate_vectors(self, t: float, delta: float) -> ndarray:
        wave: ndarray = self.create_regular_wave(t=t)
        z: ndarray = wave + delta
        u_, w_ = self.__calculate_u_w(z=z,
                                      t=t)
        speed: ndarray = sqrt(power(u_, 2) + power(w_, 2))
        array_: ndarray = np.vstack((self.x, wave + delta, u_, w_, speed)).T
        return array_
