# No Loops!  All vectorized code.
import numpy as np
def getBondDuration(y, face, couponRate, m, ppy=1):
    t = np.arange(1,m+1)
    dfs = (1 + y)** -np.arange(1,m+1)
    discounted_coupons = sum(face*couponRate*dfs)
    discounted_face = face*dfs[-1]
    bondprice = discounted_coupons+discounted_face
    sum_w = sum(face*couponRate*dfs*t)+ face*dfs[-1]*t[-1]
    return(sum_w/bondprice)

