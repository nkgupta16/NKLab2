import matplotlib.pyplot as plt
import numpy as np

# Creating subplots
fig, axs = plt.subplots(5, 2, figsize=(10, 15))

# Function 1: y = x^2
x = np.linspace(-10, 10, 100)
y = x**2
axs[0, 0].plot(x, y)
axs[0, 0].set_title("y = x^2")


# Function 2: y = 2x + 3
x = np.linspace(-10, 10, 100)
y = 2*x + 3
axs[0, 1].plot(x, y)
axs[0, 1].set_title("y = 2x + 3")


# Function 3: y = 2x
x = np.linspace(-10, 10, 100)
y = 2*x
axs[1, 0].plot(x, y)
axs[1, 0].set_title("y = 2x")


# Function 4: y = x^0.5
x = np.linspace(0, 10, 100)
y = np.sqrt(x)
axs[1, 1].plot(x, y)
axs[1, 1].set_title("y = x^0.5")


# Function 5: y = |x|
x = np.linspace(-10, 10, 100)
y = np.abs(x)
axs[2, 0].plot(x, y)
axs[2, 0].set_title("y = |x|")


# Function 6: y = 1 / x
x = np.linspace(-10, 10, 100)
y = 1 / x
axs[2, 1].plot(x, y)
axs[2, 1].set_title("y = 1 / x")


# Function 7: y = 3x
x = np.linspace(-10, 10, 100)
y = 3*x
axs[3, 0].plot(x, y)
axs[3, 0].set_title("y = 3x")


# Function 8: y = x + 1
x = np.linspace(-10, 10, 100)
y = x + 1
axs[3, 1].plot(x, y)
axs[3, 1].set_title("y = x + 1")


# Function 9: y = x / 2
x = np.linspace(-10, 10, 100)
y = x / 2
axs[4, 0].plot(x, y)
axs[4, 0].set_title("y = x / 2")


# Function 10: y = x / 3
x = np.linspace(-10, 10, 100)
y = x / 3
axs[4, 1].plot(x, y)
axs[4, 1].set_title("y = x / 3")

plt.subplots_adjust(hspace=0.5)
plt.show()
