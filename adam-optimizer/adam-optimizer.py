import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    # Write code here
    m, v, grad = np.array(m), np.array(v), np.array(grad)
    m_next = beta1*m + (1 - beta1)*grad
    v_next = beta2*v + (1 - beta2)*grad**2

    bias_corrected_m = m_next/(1 - beta1**t)
    bias_corrected_v = v_next/(1 - beta2**t)
    param_next = param - lr*(bias_corrected_m/(np.sqrt(bias_corrected_v) + eps))

    return (param_next, m_next, v_next)