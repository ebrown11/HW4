import numpy
from scipy import stats
import matplotlib.pyplot as plot

#Ethan's section
def P_1a():
    '''This function was made to calculate P(x < 1 |N(0,1): probability x < 1 given a
    normal distribution of x with mean=0, stdDev=1 using a probability density function
    figure and a cumulative density function. '''
    mean, stdDev = 0, 1 # mean and standard deviations of our normal distribution
    probability = stats.norm.cdf(1, loc=mean, scale=stdDev) # calculating the probabilities
    x_values = numpy.linspace(mean - 3 * stdDev, mean + 3 * stdDev, num=1000) # range of x values for our function

    pdf = stats.norm.pdf(x_values, loc=mean, scale=stdDev) # probability density function
    cdf = stats.norm.cdf(x_values, loc=mean, scale=stdDev) # cumulative density function

    plot.figure(figsize = (16,12))

    # plotting the pdf with a standard normal deviation with shaded region for x < 1
    plot.subplot(2, 1, 1)
    plot.plot(x_values, pdf, color='blue', label='PDF')
    plot.fill_between(x_values, pdf, where=(x_values < 1), alpha=0.5)

    # adding arrow for a more in depth visual representation for the user
    annotation = f'(P(x < 1)|N(0,1)) = {probability:.4f}'
    xarrow = -0.5
    yarrow = 0.20
    plot.annotate(annotation, xy=(xarrow, yarrow), xytext=(-2.5, 0.3),
                 arrowprops=dict(facecolor='black', shrink=.01),
                 fontsize=12, color='black')
    plot.title('PDF of N(0,1) with area under curve for x < 1')
    plot.xlabel('x')
    plot.ylabel('f(x)')
    plot.legend()

    # plotting the cdf on a with a rising line leading to our plot point
    plot.subplot(2, 1, 2)
    plot.plot(x_values, cdf, color='green', label='CDF')
    plot.scatter(1, probability, color='black')
    plot.title(f'CDF for N(0,1) = {probability:.4f}')
    plot.xlabel('x')
    plot.ylabel('Probability')
    plot.legend()

    plot.tight_layout()
    plot.show()

#Brandon's section
def P_1b():
    '''This function was made to calculate P(x > mean + 2 * standard deviation): probability given a
    normal distribution of x with mean = 175, stdDev = 3 with a figure for the probability density function
    and cumulative density function.'''
    mean, stdDev = 175, 3 # mean and standard deviations of our normal distribution
    probability = 1- stats.norm.cdf(mean + 2 * stdDev, loc=mean, scale=stdDev) #calculating the probabilities
    x_values = numpy.linspace(mean - 4 * stdDev, mean + 4 * stdDev, 1000) #range of x values for our function

    pdf_values = stats.norm.pdf(x_values, loc=mean, scale=stdDev) #probability density function
    cdf_values = stats.norm.cdf(x_values, loc=mean, scale=stdDev) #cumulative density function

    plot.figure(figsize = (16,12))

    # plotting the pdf with a standard normal deviation with shaded region for x > mean * standard deviation
    plot.subplot(2, 1, 1)
    plot.plot(x_values, pdf_values, color='blue', label='PDF')
    plot.fill_between(x_values, pdf_values, where=(x_values > mean + 2 * stdDev), alpha=0.5)

    # adding arrow for a more in depth visual representation for the user
    annotation = f'(P(x > 1)|N(175,3) = {probability:.4f}'
    xarrow = 181.5
    yarrow = 0.005
    plot.annotate(annotation, xy=(xarrow, yarrow), xytext=(181.50, 0.03),
                 arrowprops=dict(facecolor='black', shrink=.01),
                 fontsize=12, color='black')
    plot.title('PDF of N(175,3)')
    plot.xlabel('x')
    plot.ylabel('f(x)')
    plot.legend()

    # plotting the cdf on a with a rising line leading to our plot point
    plot.subplot(2, 1, 2)
    plot.plot(x_values, cdf_values, color='green', label='CDF')
    plot.fill_between(x_values, cdf_values, color='green', alpha=0.5)
    plot.scatter(mean + 2 * stdDev, 1 - probability, color='black')
    plot.title(f'CDF for N(175,3) = {1 - probability:.4f}')
    plot.xlabel('x')
    plot.ylabel('Probability')
    plot.legend()

    plot.tight_layout()
    plot.show()


print(P_1a())
print(P_1b())