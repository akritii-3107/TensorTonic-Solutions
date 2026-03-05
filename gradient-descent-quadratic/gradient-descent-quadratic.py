def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    xt=x0
    for i in range(steps):
        xt_1=xt-(lr*(2*a*xt + b))
        xt=xt_1
    return xt
    # Write code here
    pass