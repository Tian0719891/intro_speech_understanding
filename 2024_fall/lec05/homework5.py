import numpy as np
import matplotlib.pyplot as plt

def center_of_gravity(x):
    x = np.array(x)
    weights = np.arange(len(x))
    c = np.dot(weights, x) / np.sum(x)
    c = 0  # change this line
    return c

def matched_identity(x):
    size = len(x)
    I = np.eye(size)
    I =  0 # change this line
    return I

def sine_and_cosine(t_start, t_end, t_steps):
    t = np.linspace(t_start, t_end, t_steps)
    x = np.cos(t)
    y = np.sin(t)
    return t, x, y
