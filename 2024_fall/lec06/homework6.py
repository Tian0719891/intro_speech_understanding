import numpy as np

def minimum_Fs(f):
    Fs = 2 * f  # change this line
    return Fs

import math

def omega(f, Fs):
    return 2 * math.pi * f / Fs

import numpy as np

def pure_tone(omega, N):
    return np.array([np.cos(omega * n) for n in range(N)])

