import numpy as np
from scipy.stats import chi2

def kupiec_test(breaches, total, alpha):
    failure_rate = breaches / total
    expected = 1 - alpha

    lr = -2 * (
        np.log((1 - expected)**(total - breaches) * expected**breaches)
        - np.log((1 - failure_rate)**(total - breaches) * failure_rate**breaches)
    )

    p_value = 1 - chi2.cdf(lr, df=1)
    return lr, p_value
