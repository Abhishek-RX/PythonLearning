import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 5, 6]
y = [5, 8, 8, 6, 20]

# Creating a line plot
plt.plot(x, y, label='Line Chart')  # Adding a label for the line chart

# Creating a bar plot
plt.bar(x, y, alpha=0.5, label='Bar Chart')  # Adding a label for the bar chart

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Chart with Bar Chart')

# Adding a legend
plt.legend()
plt.grid()
# Displaying the plot
plt.show()
plt.pie(y)  # Simple pie chart
plt.show()
plt.pie(x, labels= x , shadow = True, autopct = '%1.1f%%',startangle= 140)
plt.show()

