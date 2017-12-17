import numpy as np

# Boltzman's constant [J/K]
k = 1.38e-23

# elementary charge [C]
q = 1.6e-19

def junctionVoltage(Na, Nd, ni, T):
    '''Function calculating a voltage built-in across the p-n juntion.

    Inputs:
    ------------------
    Na: float
        Acceptor carriers concentration [1/cm3]
    Nd: float
        Donor carriers concentration [1/cm3]
    ni: float
        Intrinsic carrier concentration [1/cm3]
    T: float
        Temperature [K]

    Returns:
    ------------------
    Vbi: float
        Voltage built across the p-n junction in [V] '''

    return k*T/q * np.log(Na*Nd/ni**2)

# add function showing Planck's law for black body at 5800K


###########################################################
# PV Systems functions
###########################################################

def pv_efficiency(Ump, Imp, H, W):
    '''Placeholder for help'''
    return Ump*Imp/(H*W)/1000
