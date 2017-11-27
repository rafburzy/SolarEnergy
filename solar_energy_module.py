import numpy as np

# Boltzman's constant [J/K]
k = 1.38e-23

# elementary charge [C]
q = 1.6e-19

def junctionVoltage(Na, Nd, ni, T):
    '''Function calculating a voltage built-in across the p-n juntion.

    Inputs:
    ------------------


    Returns:
    ------------------
    Vbi: float
        Voltage built across the p-n junction in [V] '''

    return k*T/q * np.log(Na*Nd/ni**2)
