# No Loops!  All vectorized code.
import numpy as np
def FizzBuzz(start, finish):
    numvec = np.arange(start,finish+1)
    objvec = np.array(numvec,dtype = object)
    fizzbuzz = (numvec % 15 == 0)
    objvec[fizzbuzz] = "fizzbuzz"
    buzz = (numvec % 5 == 0) & (numvec % 3 !=0)
    objvec[buzz] = "buzz"
    fizz = (numvec % 3 == 0) & (numvec % 5 !=0)
    objvec[fizz] = "fizz"
    return(objvec)

