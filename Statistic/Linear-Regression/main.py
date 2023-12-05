from numpy import ndarray
import numpy as np
from linreg.LinearRegression import LinearRegression
from pprint import pprint

x: ndarray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y: ndarray = np.array([1, 1, 2, 2, 4, 5, 6, 8.5, 9.1, 10.3])

test = LinearRegression(x=x, y=y)

test.predict_linear_model()
test.calculate_errors()
y_predicted = test.get_model_function()

pprint(list(zip(y, y_predicted(x))))

print(test.MATH_MODELLED_FUNCTION)
print(test.MSE)
print(test.SE)