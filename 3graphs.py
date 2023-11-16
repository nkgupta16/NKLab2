import matplotlib.pyplot as plt
import numpy as np

# Sample size
START = -10
STOP = 10
NUM = 100

# Creating subplots
fig, axs = plt.subplots(5, 2, figsize=(10, 15))


# Function to add a plot
def add_plot(func, pos, title='y(x)'):
    x = np.linspace(START, STOP, NUM)
    y = func(x)
    axs[pos].plot(x, y)
    axs[pos].set_title(title)


# Adding plots using the add_plot function
add_plot(lambda x: x ** 2, (0, 0), 'y = x^2')
add_plot(lambda x: 2 * x + 3, (0, 1), 'y = 2x + 3')
add_plot(lambda x: 2 * x, (1, 0), 'y = 2x')
add_plot(lambda x: np.sqrt(x), (1, 1), 'y = x^0.5')
add_plot(lambda x: np.abs(x), (2, 0), 'y = |x|')
add_plot(lambda x: 1 / x, (2, 1), 'y = 1 / x')
add_plot(lambda x: 3 * x, (3, 0), 'y = 3x')
add_plot(lambda x: x + 1, (3, 1), 'y = x + 1')
add_plot(lambda x: x / 2, (4, 0), 'y = x / 2')
add_plot(lambda x: x / 3, (4, 1), 'y = x / 3')

plt.subplots_adjust(hspace=0.5)
plt.show()
