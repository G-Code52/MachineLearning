import numpy as np

def Est():
    m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(m)
    print("")
    print(np.amax(m))
    print("")
    print(np.amin(m))
    print("")
    print(np.amin(m, 1))
    