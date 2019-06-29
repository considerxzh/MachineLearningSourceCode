import math
import numpy as np

def sigmoid(z):
    y = 1/(1+np.exp(-z))
    return y

def sigmoid_Derivation(z):
    y = 1/(1+np.exp(-z))
    return y*(1-y)


