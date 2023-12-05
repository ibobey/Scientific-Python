from typing import Any, Callable
from numpy import ndarray
import numpy as np


class LinearRegression:
    x: ndarray
    y: ndarray
    __y_predicted: ndarray

    __E_x: float | Any
    __E_y: float | Any
    __E_xy: float | Any
    __E_x_square: float | Any
    __n: int

    __m: float | Any
    __b: float

    __model_function: Callable[[float | ndarray], float | ndarray]
    __mse: float | Any
    __se: float | Any

    __state: bool

    @property
    def MODEL_FUNCTION(self) -> Callable[[float | ndarray], float | ndarray] | None:
        """
        Returns callable model function depends x-y regression analyse
        :return: Callable
        """
        return self.__model_function

    @property
    def MATH_MODELLED_FUNCTION(self) -> str:
        """
        Math Modelled function
        :return: str
        """
        return f"p(x) = {self.__m}x + ({self.__b})"

    @property
    def PREDICTED_Y_VALUES(self) -> ndarray:
        return self.__y_predicted

    @property
    def MSE(self) -> float | None:
        """
        Mean Square Error
        :return: float
        """
        return self.__mse

    @property
    def SE(self) -> float | None:
        """
        Square Error
        :return: float
        """
        return self.__se

    def __init__(self, x: ndarray, y: ndarray) -> None:
        self.x = x
        self.y = y
        self.__state = False
        self.__setup()

    def __str__(self) -> str:
        return f"p(x) = {self.__m}x + ({self.__b})"

    def __setup(self) -> None:
        """
        Checks x-y array equality
        :return:
        """
        if len(self.x) != len(self.y):
            raise Exception("x-y array Inequality Error")
        self.__n = len(self.x)

    def __calculate_sums(self) -> None:
        """
        Calculates sum of needed variables
        :return: None
        """
        self.__E_x = np.sum(self.x)
        self.__E_y = np.sum(self.y)
        self.__E_xy = np.sum(self.x * self.y)
        self.__E_x_square = np.sum(self.x ** 2)

    def __calculate_slope(self) -> None:
        """
        Calculates model's Slope
        :return: None
        """
        m = (self.__n * self.__E_xy - self.__E_x * self.__E_y) / (self.__n * self.__E_x_square - (self.__E_x) ** 2)
        self.__m = m

    def __calculate_y_intercept(self) -> None:
        """
        Calculates model's y-intercept
        :return: None
        """
        self.__b = (self.__E_y - self.__m * self.__E_x) / self.__n

    def predict_linear_model(self) -> None:
        """
        Calculates Linear Model
        :return: None
        """
        self.__calculate_sums()
        self.__calculate_slope()
        self.__calculate_y_intercept()

        self.__state = True  # Calculated

        self.__y_predicted: ndarray = self.get_model_function()(self.x)

    def calculate_errors(self) -> None:
        """
        Calculates errors
        :return: None
        """

        if self.__state is not True:
            raise Exception("Calculated Model not Found, Predict Model First !")

        self.__mse = np.mean((self.y - self.__y_predicted) ** 2)
        self.__se = np.sum((self.y - self.__y_predicted) ** 2)

    def get_model_function(self) -> Callable[[float | ndarray], float | ndarray]:
        """
        Returns predicted y callable function
        :return:  Callable[[float | ndarray], float | ndarray]
        """
        if self.__state is not True:
            raise Exception("Calculated Model not Found, Predict Model First !")

        def model(x: float | ndarray) -> float | ndarray:
            return self.__m * x + self.__b

        self.__model_function = model

        return model
