from dataclasses import dataclass, field
from numpy import ndarray


@dataclass
class Elements:
    """
    Constants & Variables of Differential Equation
    """
    m: float  # mass (kg)
    p: float  # Density of air (kg/m3)
    A: float  # Area of the Object Exposed to Airflow (m2)
    C_D: float  # Drag Coefficient
    v0: float  # velocity of object (m/s)
    g: float  # gravity (m/s2)
    t: ndarray  # time (s)

