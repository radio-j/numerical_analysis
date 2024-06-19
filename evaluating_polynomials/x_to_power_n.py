# computes y = x**n, using binary expansion and the powers of 2 of x

def x_to_the_power_n(x,n):
    m = n
    y = 1
    z = x

    if (m%2):
        y = y * z
    m = m//2
    while (m >= 1):
        z = z*z
        if (m%2):
            y=y*z
        m = m//2
    return y
