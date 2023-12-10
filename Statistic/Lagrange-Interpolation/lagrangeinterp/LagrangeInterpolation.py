from numpy import ndarray


class LagrangeInterp:
    __arr_x: ndarray | list
    __arr_y: ndarray | list
    __n: int
    __array_length: int

    @property
    def N(self) -> int:
        return self.__n

    @N.setter
    def N(self, value) -> None:
        if value > self.__n or value < 0:
            print("Cannot assign custom value for 'n', default value assigned")
        else:
            self.__n = value

    def __init__(self, x, y):
        self.__arr_x = x
        self.__arr_y = y
        self.__setup()

    def __setup(self) -> None:
        if len(self.__arr_x) != len(self.__arr_y):
            raise Exception("Array must be same length!")

        if len(self.__arr_x) <= 1:
            raise Exception("Dimension cannot supported!")

        self.__n = int(len(self.__arr_x))
        self.__array_length = len(self.__arr_x)

    def calc_interp_for_x_value(self, x: float) -> float:
        summ: float = 0
        for i in range(0, self.__n):
            summ += self.__arr_y[i] * self.__L_i(x=x, i=i)
        return summ

    def __L_i(self, i: int, x: float) -> float:
        product: float = 1
        for j in range(0, self.__n):
            if j == i:
                continue
            product *= (x - self.__arr_x[j]) / (self.__arr_x[i] - self.__arr_x[j])
        return product

