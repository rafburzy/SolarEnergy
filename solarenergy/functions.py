import numpy as np

# Boltzman's constant [J/K]
k = 1.38e-23

# elementary charge [C]
q = 1.602e-19

# speed of light [m/s]
c = 2.998e8

# Planck's constant [Js]
h = 6.626e-34

# electrical permability of vaccum [F/m]
epsilon_o = 8.854e-12

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

def deplRegWidth(Na, Nd, Vbi, epsilon_r=11.7):
    '''Function calculating a width of a depletion zone for a p-n juntion.

    Inputs:
    ------------------
    Na: float
        Acceptor carriers concentration [1/cm3]
    Nd: float
        Donor carriers concentration [1/cm3]
    Vbi: float
        voltage built across the junction [V]
    epsilon_r: float
        electrical permability of silicon (11.7 F/m)

    Returns:
    ------------------
    W: float
        Width of a depletion zone [micro m] '''
    Na = Na*1e6
    Nd = Nd*1e6
    return np.sqrt(2*epsilon_r*epsilon_o/q * Vbi * (1/Na + 1/Nd))*1e6

# diffusion current density
def diffCurrentDensity(De, dn, dx):
    '''Function calculating current density due to diffusion

    inputs:
    -------------
    De : diffusity [cm2/s]
    dn : change of carrier concentration [1/cm3]
    dx : distance at which the carriers concentration changes [cm]

    Returns:
    -----------
    J : current density due to diffusion [A/cm2]'''
    return q*De*dn/dx

# diffusion current density
def driftCurrentDensity(n, ne, E):
    '''Function calculating drift current density.

    inputs:
    -----------
    n : density of carrirers [1/cm3]
    ne : mobility of electrons or holes [cm2/Vs]
    E: electric field intensity [V/cm]

    Returns:
    ---------------
    J : drift current density [A/cm2]'''
    return n*q*ne*E

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

def airmass(theta):
    '''Function calculating air mass based on a given angle

    Parameter:
    theta: angle in deg'''
    return 1/np.cos(np.radians(theta))

# Open circuit voltage
def openCirVoltage(Jph, Jo, T):
    '''Function calculating open circuit voltage

    inputs:
    --------------
    Jph: photo-current density [mA/cm2]
    Jo: saturation current density [mA/cm2]
    T : Temperature [K]

    Returns:
    -------------
    Voc : open circuit voltage [V]'''
    return k*T/q * np.log(Jph/Jo + 1)
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
