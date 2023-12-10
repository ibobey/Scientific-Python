from numpy import ndarray

def calc_interp(n: int, x: float, arr_x: ndarray | list, arr_y: ndarray | list) -> float:
    def __L_i(i: int, n: int, x: float, arr_x: list | ndarray) -> float:
        product: float = 1
        for j in range(0, n):
            if j == i:
                continue
            product *= (x - arr_x[j]) / (arr_x[i] - arr_x[j])
        return product

    summ = 0
    for i in range(0, n):
        summ += arr_y[i] * __L_i(x=x, n=n, i=i, arr_x=arr_x)
    return summ