import matplotlib.pyplot as plt

# Data
categories = [
    "Assistant to Assistant",
    "Assistant to Associate",
    "Associate"
]
values = [40, 31, 15]

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(categories, values, color=['skyblue', 'lightgreen', 'salmon'])

# Add title and labels
plt.title('Professor Position Changes', fontsize=16)
plt.xlabel('Career Path', fontsize=14)
plt.ylabel('Number of Professors', fontsize=14)

# Add value labels on top of the bars
for i, value in enumerate(values):
    plt.text(i, value + 0.5, str(value), ha='center', fontsize=12)

# Save the plot
output_path = '/home/gs285/DBLP_scrape/career_change/professor_position_changes.png'
plt.tight_layout()
plt.savefig(output_path)

# Show the plot
plt.show()

print(f"Plot saved to {output_path}")