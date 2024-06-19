import numpy

def nested_polyval(c,x):
    d = np.size(c)
    px = c[d-1]
    for i in range(d-2, -1, -1):
        px = px*x + c[i]
    return px
