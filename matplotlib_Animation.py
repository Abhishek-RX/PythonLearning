import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Creating a figure and axis
fig, ax = plt.subplots()
line, = ax.plot(x, y, label='Sine Wave')

# Adding labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Animated Sine Wave')
ax.legend()

# Function to update the plot
def update(frame):
    line.set_ydata(np.sin(x + frame / 10.0))  # Update the y-data
    return line,

# Creating the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Displaying the plot
plt.show()