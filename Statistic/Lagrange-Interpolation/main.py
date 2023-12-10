from lagrangeinterp.LagrangeInterpolation import LagrangeInterp
from lagrangeinterp import calc_interp

test_x: list = [1, 2, 3, 5, 6]
test_y: list = [3.75, 4, 5.25, 19.75, 36]

test = LagrangeInterp(x=test_x, y=test_y)
test_answ_1 = test.calc_interp_for_x_value(x=4.1)
print("Test Ans 1: ", test_answ_1)

test_answ_2 = calc_interp(x=4.1, arr_x=test_x, arr_y=test_y, n=len(test_x))
print("Test Ans 2: ", test_answ_2)
