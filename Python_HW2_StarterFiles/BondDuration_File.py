import numpy as np

def getBondDuration(y, face, couponRate, m, ppy):
    y_eff = y / ppy
    couponRate_eff = couponRate / ppy
    n = m * ppy
    c = couponRate_eff * face

    t = np.arange(1, n+1)
    cf = np.full(n, c)
    cf[-1] += face

    pvcf = cf / (1 + y_eff) ** t
    pvcf_t = pvcf * t / ppy
    pv = np.sum(pvcf)

    duration = np.sum(pvcf_t) / pv

    return round (duration,2)
