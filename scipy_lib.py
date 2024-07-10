iimport numpy as np
from scipy.special import jn, yn, jn_zeros, yn_zeros
from scipy.integrate import quad, dblquad, tplquad
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import random as rand
 
def function_defined(x):
    return np.cos(x)
 

def main():
    # example 1: calculate first and second kind bessel functions
    alpha = 0
    x = 0.0
    print("first kind bessel function printed")
    print("J_{}({}) = {}".format(alpha, x, jn(alpha, x)))
    x = 1.0
    print("second kind bessel function")
    print("Y_{}({}) = {}".format(alpha, x, yn(alpha, x)))
    
    # plot four bessel functions
    x = np.linspace(0, 10, 100)
    fig, ax = plt.subplots()
    
    for alpha in range(4):
        ax.plot(x, jn(alpha, x), label=r"J$_{}(x)$".format(alpha))
        ax.legend()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Bessel Functions")
        plt.show()

    # example 2: calculate definite integral to be used in the calculations
    a = 0
    b = 1
    integral_value, absolute_error = quad(function_defined, a, b)
    print("integral value: {} \nabsolute error:{}".format(integral_value, absolute_error))
                    
    # example 3. linear and cubic functions interpolation
    n = np.arange(0, 10)
    x = np.linspace(0, 9, 100)
    # set the actual function
    y_actual = function_defined(x)

    # generate random experiment data
    y_experiment = function_defined(n) + 0.1 * np.random.randn(len(n))
    linear_interpolation = interp1d(n, y_experiment, kind="linear")

    # get linear interpolation
    y_linear_interpolation = linear_interpolation(x)
    cubic_interpolation = interp1d(n, y_experiment, kind="cubic")

    # get cubic interpolation
    y_cubic_interpolation = cubic_interpolation(x)
 
    # plot y actual, experiment, linear and cubic interpolation
    fig, ax = plt.subplots(figsize=(10,4))
    ax.plot(n, y_experiment, "bs", label="experiment data")
    ax.plot(x, y_actual, "k", lw=2, label="actual function")
    ax.plot(x, y_linear_interpolation, "r", label="linear interpolation")
    ax.plot(x, y_cubic_interpolation, "g", label="cubic interpolation")
    ax.legend(loc=3)

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Functons Interpolation Example")

    print("Visually showing the example of the function")
    plt.show()

if __name__ == '__main__':
    main()
