import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
from scipy.interpolate import griddata

# Load the Earth texture image
earth_img = Image.open('earth.jpg')

# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create data for the Earth
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

# Map the texture onto the sphere
earth_texture = np.array(earth_img.resize((100, 50)))
earth_texture = earth_texture / 255.0  # Normalize the texture

# Create a meshgrid for the texture coordinates
u_texture = np.linspace(0, 1, earth_texture.shape[1])
v_texture = np.linspace(0, 1, earth_texture.shape[0])
u_texture, v_texture = np.meshgrid(u_texture, v_texture)

# Interpolate the texture to match the shape of the surface
points = np.array([u_texture.flatten(), v_texture.flatten()]).T
values = earth_texture.reshape(-1, 3)
grid_u, grid_v = np.meshgrid(np.linspace(0, 1, x.shape[1]), np.linspace(0, 1, x.shape[0]))
earth_texture_interp = griddata(points, values, (grid_u, grid_v), method='linear')

# Plot the initial Earth with texture
earth = ax.plot_surface(x, y, z, rstride=5, cstride=5, facecolors=earth_texture_interp, alpha=0.6)

# Function to update the plot
def update(frame):
    ax.view_init(elev=10., azim=frame)
    return earth,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=360, interval=20, blit=True)

# Set the axis limits
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])

# Set the axis labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Set the title
ax.set_title('Animated Sci-Fi Earth with Textures')

# Display the plot
plt.show()