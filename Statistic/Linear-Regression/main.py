from linreg.LinearRegression import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import ndarray
import pandas as pd
from pandas import DataFrame

"""THEME CUSTOMIZATION"""

sns.set_theme(
    context='notebook',
    style='whitegrid',
    palette='pastel')

"""READ RAW DATA"""

data: DataFrame = pd.read_csv("Experience-Salary.csv")

data.rename(columns=
            {'exp(in months)': "x",
             'salary(in thousands)': "y"}, inplace=True)

""" PREDICTION by linreg module"""

test_linreg: LinearRegression = LinearRegression(x=data.x,
                                                 y=data.y)

test_linreg.predict_linear_model()
y_predicted: ndarray = test_linreg.PREDICTED_Y_VALUES
test_linreg.calculate_errors()

""" PLOTTING """

figure, axes = plt.subplots(figsize=(9, 7.5))
axes.scatter(data.x, data.y, c="r", label="salary", alpha=0.8)
axes.plot(data.x, y_predicted, "k--", label="Model")

axes.set_title("Experience / Salary Regression Analyze")
axes.set_xlabel("experience [m]")
axes.set_ylabel("Salary [$k]")

axes.legend(loc="best")
axes.grid(True, alpha=0.45, ls="-.")
sns.despine()
plt.text(22.5, -3, f'MSE: {round(test_linreg.MSE, 2)}')
plt.figtext(0.5, 0.01, f"{test_linreg.MATH_MODELLED_FUNCTION}", ha="center", fontsize=11, bbox={"facecolor": "orange", "alpha":0.35, "pad":3})
plt.show()

