from math import pi, exp, sin
 
def f(t, A=1, a=1, omega=2*pi):
    print (A*exp(-a*t)*sin(omega*t))
    return A*exp(-a*t)*sin(omega*t)
    
