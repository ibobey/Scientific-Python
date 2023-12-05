from numpy import ndarray
import numpy as np


class LinReg:
    x: ndarray
    y: ndarray

    __E_x: float
    __E_y: float
    __E_xy: float
    __E_x_square: float
    __n: int

    __m: float
    __b: float

    def __init__(self, x: ndarray, y: ndarray) -> None:
        self.x = x
        self.y = y
        self.__setup()
    def __setup(self) -> None:
        if len(self.x) != len(self.y):
            raise Exception("Same Length")
        self.__n = len(self.x)

    def __calc_vars(self) -> None:
        self.__E_x = np.sum(self.x)
        self.__E_y = np.sum(self.y)
        self.__E_xy = np.sum(self.x * self.y)
        self.__E_x_square = np.sum(self.x ** 2)

    def __calc_slope(self) -> float:
        m = (self.__n * self.__E_xy - self.__E_x * self.__E_y) / (self.__n * self.__E_x_square - (self.__E_x) ** 2)
        return m

    def __calc_y_intercept(self) -> None:
        self.__m = self.__calc_slope()
        self.__b = (self.__E_y - self.__m * self.__E_x) / (self.__n)

    def calculate_model(self) -> None:
        self.__calc_vars()
        self.__calc_slope()
        self.__calc_y_intercept()

    def show_model(self) -> None:
        print(f"y = {self.__m}x + {self.__b}")
