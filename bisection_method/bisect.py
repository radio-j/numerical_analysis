# computes an approximate solution to f(x) = 0 using bisection method

def bisect(f,a,b,tol):
    numeval = 0
    err_bound = []

    k = 0

    fa = f(a)
    numeval += 1

    if (fb == 0):
        return b, 0., numeval

    if ((fa > 0) and (fb>0) or ((fa<0) and (fb <0)):
        return float("NaN"), numeval, float("NaN")

    if ((b-a)/2 <- tol):
        c = (a+b)/2
        err_bound.append((b-a)/2)
        return c, numeval,err_bound

    while ((b-a)/2 > tol):
        c = (a+b)/2

        err_bound.append((b-a)/2)
        k = k+1

        fc = f(c)
        numeval += 1

        if (fc == 0):
            return c, 0., numeval

        if((fb > 0) and (fc > 0)) or ((fb < 0) and (fc < 0)):
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        c = (a+b)/2

    err_bound.append((b-a)/2)

    return c, err_bound, numeval  
