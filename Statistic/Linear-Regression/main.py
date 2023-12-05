from numpy import ndarray
import numpy as np
from linreg.LinReg import LinReg


x: ndarray = np.array([7,4,6,2,1,1,3])
y: ndarray = np.array([2,4,2,5,7,6,5])

test = LinReg(x=x, y =y)

test.calculate_model()

test.show_model()