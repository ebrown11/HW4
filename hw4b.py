import numpy as np, matplotlib.pyplot as plt
from scipy.optimize import fsolve

#Ethan's section
def equation_1(x):
    """
    This defines equation 1. x-3*cos(x)=0
    :param x: This is the variable x.
    :return: The equation value at x.
    """
    return x - 3 * np.cos(x)

def equation_2(x):
    """
    This defines equation 2. cos(2x)*x^3 = 0
    :param x: This is the variable x.
    :return: The equation value at x.
    """
    return np.cos(2 * x) * x**3

#Finding the Roots
def find_roots():
    """
    This will find the roots of the equations by using fsolve.
    :return: The roots of the equations.
    """
#Use initial guesses and fsolve to find the roots of the equations.
initial_guess_1 = [1]
initial_guess_2 = [1]
root_eq_1 = fsolve(equation_1, initial_guess_1)
root_eq_2 = fsolve(equation_2, initial_guess_2)
print("Root of Equation 1:", root_eq_1)
print("Root of Equation 2:", root_eq_2)

#Brandon's section
def intersect(x):
    guesses = np.linspace(-10,10, 1000)#the viewing window
    intersect = fsolve(equation_1, equation_2, guesses)
print("The functions intersect at:", intersect)

#Using matplotlib.pyplot, this will plot the graphs.
x_values = np.linspace(-10,10, 1000)#the viewing window
y_values_1 = equation_1(x_values)
y_values_2 = equation_2(x_values)
plt.plot(x_values, equation_1(x_values), label='x-3*cos(x)')
plt.plot(x_values, equation_2(x_values), label='cos(2x)*x^3')
plt.scatter(root_eq_1, [0], color='black', marker='x', label='Roots of Eq. 1')
plt.scatter(root_eq_2, [0]*len(root_eq_2), color='blue', marker='x', label='Roots of Eq. 2')
plt.axhline(0, color='red', linewidth=0.5, linestyle='--')
plt.legend()
plt.title('Graph of the two Equations')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

