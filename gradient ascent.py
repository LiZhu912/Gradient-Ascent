# Defines a function.
def f(x,y):
    return -(x**2+y**2)+2

# Computes partial derivatives.
def partial_x(f,x,y,h=0.00000001):
    numerator = f(x+h,y) - f(x,y)
    denominator = h
    return numerator/denominator

def partial_y(f,x,y,h=0.00000001):
    numerator = f(x,y+h) - f(x,y)
    denominator = h
    return numerator/denominator

# Computes the gradient of f(x,y).
def calc_gradient(f,x,y):
    return partial_x(f,x,y),partial_y(f,x,y)

# Move a small step towards gradient until magnitude of gradient becomes small.
def gradient_ascent(f,a,b, delta=0.001):
    gradient = calc_gradient(f,a,b)
    while True:
        magnitude = (gradient[0]**2+gradient[1]**2)**(1/2)
        if magnitude<0.001:
            break
        else:
            gradient = calc_gradient(f,a,b)
            a = a + delta*gradient[0]
            b = b + delta*gradient[1]
        
    return "The local max of the function is",str(f(a,b)),"at point",str(a),str(b)

# Test
#print(gradient_ascent(f,3,3))
