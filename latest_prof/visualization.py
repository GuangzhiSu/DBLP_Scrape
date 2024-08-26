import matplotlib.pyplot as plt
import numpy as np

# Data for visualization
universities = [
    "Caltech", "Columbia_University", "Cornell", "Duke", "Harvard", "JHU", 
    "Northwestern University", "Princeton", "PSU", "Purdue", "Rice University", 
    "Stanford", "UCLA", "UCSB", "UIUC", "UMD", "Univ. of California - Berkeley", 
    "Univ. of California - San Diego", "University of Pennsylvania", "University_of_North_Carolina", 
    "USC", "UTAustin", "UW", "UWMadison", "Yale"
]

latest_five_years = [
    2, 5, 5, 2, 2, 4, 0, 10, 5, 11, 4, 4, 5, 1, 13, 5, 6, 20, 1, 5, 
    8, 5, 9, 12, 11
]

before_five_years = [
    8, 20, 9, 8, 7, 13, 5, 9, 12, 8, 5, 14, 12, 5, 14, 18, 35, 27, 
    8, 7, 13, 13, 14, 5, 5
]

# Create the bar chart
x = np.arange(len(universities))  # Label locations
width = 0.35  # Width of the bars

fig, ax = plt.subplots(figsize=(14, 10))

bars1 = ax.bar(x - width/2, latest_five_years, width, label='2019-2024', color='skyblue')
bars2 = ax.bar(x + width/2, before_five_years, width, label='Before 2019 or No Start Year', color='salmon')

# Add some text for labels, title, and custom x-axis tick labels, etc.
ax.set_xlabel('University', fontsize=14)
ax.set_ylabel('Number of Professors', fontsize=14)
ax.set_title('Professor Joining Summary (2019-2024 vs Before 2019)', fontsize=16)
ax.set_xticks(x)
ax.set_xticklabels(universities, rotation=90, ha="center", fontsize=12)
ax.legend()

# Add value labels on top of the bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(bars1)
add_labels(bars2)

fig.tight_layout()

# Save the figure
output_path = '/home/gs285/DBLP_scrape/latest_prof/professor_joining_summary.png'
plt.savefig(output_path)
plt.close()

print(f"Plot saved to {output_path}")
