import math
def f(x):
    """
    calculates the area under the curve
    """
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.

    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    # recusion solution
    # if start >= (stop - step):
    #     # base case
    #     return f(start) * step
    # else:
    #     # recursive steps
    #     return (f(start) * step) + radiationExposure(start+step, stop, step)

    # iteration solution
    radiation = 0
    while start < stop:
        radiation += f(start)*step
        start += step
    return radiation
