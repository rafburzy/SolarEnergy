import numpy as np

# Boltzman's constant [J/K]
k = 1.38e-23

# elementary charge [C]
q = 1.6e-19

# speed of light [m/s]
c = 2.998e8

# Planck's constant [Js]
h = 6.63e-34

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

# function showing Planck's law for black body at 5800K
def spectralRadiance(l, T):
    '''Function calculating spectral radiance of a back body at a given temperature

    Inputs:
    ------------
    l: wavelength [m]
    T: temperature [K]

    Returns:
    ------------
    spectral power density [W/(m2 * m)] /power per unit area and unit wavelength'''
    return [2*h*c**2/(j**5) * 1/(np.exp(h*c/(j*k*T))-1) for j in l]

###########################################################
# PV Systems functions
###########################################################

def pv_efficiency(Ump, Imp, H, W):
    '''Function calculating efficiency of a pv cell: max output power per area divided by STU irradiance of 1000 W/m2

    Imputs:
    -----------
    Ump: max power voltage [V]
    Imp: max power current [A]
    H: cell height [m]
    W: cell width [m]

    Returns:
    ------------
    pv cell efficiency [-]'''
    return Ump*Imp/(H*W)/1000
