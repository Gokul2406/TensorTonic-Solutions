import numpy as np

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    """
    Perform one RMSProp update step.
    """
    # Write code here
    w, g, s = np.array(w), np.array(g), np.array(s)
    s_next = beta*s + (1 - beta)*g**2
    w_next = w - lr/(np.sqrt(s_next + eps))*g
    return (w_next, s_next)