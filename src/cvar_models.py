import numpy as np

def cvar(losses, var_threshold):
    tail_losses = losses[losses <= var_threshold]
    return tail_losses.mean()
