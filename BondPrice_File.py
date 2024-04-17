# No Loops!  All vectorized code.
import numpy as np
def getBondPrice(y, face, couponRate, m, ppy=1):
    dfs = (1 + y)** -np.arange(1,m+1)
    discounted_coupons = sum(face*couponRate*dfs)
    discounted_face = face*dfs[-1]
    return(discounted_coupons+discounted_face)

