def approx_derivative(f, x, delta=1e-6):
    derv = (f(x + delta) - f(x - delta)) / (2 * delta)
    return derv


def approx_derivative_2(f, delta=1e-6):
    return lambda x: approx_derivative(f, x, delta)

