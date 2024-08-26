import matplotlib.pyplot as plt
import numpy as np

# Data for each university
data = {
    "Duke": {
        "2020-2024": {"NeurIPS": 36, "ICML": 28, "ICLR": 24, "AAAI": 26, "IJCAI": 4, "KDD": 33, "CVPR": 14, "ICCV": 4, "ECCV": 6, "COLT": 1, "MLSys": 2, "ACL": 10, "EMNLP": 5},
        "2014-2019": {"NeurIPS": 18, "ICML": 38, "ICLR": 2, "AAAI": 18, "IJCAI": 5, "KDD": 23, "CVPR": 18, "ICCV": 3, "ECCV": 1, "COLT": 12, "MLSys": 0, "ACL": 13, "EMNLP": 4},
    },
    "Columbia": {
        "2020-2024": {"NeurIPS": 59, "ICML": 26, "ICLR": 27, "AAAI": 29, "IJCAI": 1, "KDD": 2, "CVPR": 23, "ICCV": 8, "ECCV": 12, "COLT": 13, "MLSys": 1, "ACL": 36, "EMNLP": 7},
        "2014-2019": {"NeurIPS": 34, "ICML": 51, "ICLR": 3, "AAAI": 13, "IJCAI": 13, "KDD": 3, "CVPR": 29, "ICCV": 10, "ECCV": 9, "COLT": 8, "MLSys": 0, "ACL": 15, "EMNLP": 16},
    },
    "Cornell": {
        "2020-2024": {"NeurIPS": 63, "ICML": 36, "ICLR": 38, "AAAI": 25, "IJCAI": 9, "KDD": 5, "CVPR": 6, "ICCV": 1, "ECCV": 1, "COLT": 2, "MLSys": 1, "ACL": 7, "EMNLP": 6},
        "2014-2019": {"NeurIPS": 17, "ICML": 42, "ICLR": 1, "AAAI": 36, "IJCAI": 14, "KDD": 7, "CVPR": 6, "ICCV": 0, "ECCV": 1, "COLT": 1, "MLSys": 0, "ACL": 7, "EMNLP": 11},
    },
    "Harvard": {
        "2020-2024": {"NeurIPS": 53, "ICML": 27, "ICLR": 14, "AAAI": 40, "IJCAI": 9, "KDD": 2, "CVPR": 7, "ICCV": 4, "ECCV": 1, "COLT": 4, "MLSys": 0, "ACL": 1, "EMNLP": 0},
        "2014-2019": {"NeurIPS": 14, "ICML": 22, "ICLR": 2, "AAAI": 58, "IJCAI": 36, "KDD": 5, "CVPR": 8, "ICCV": 2, "ECCV": 1, "COLT": 4, "MLSys": 0, "ACL": 3, "EMNLP": 5},
    },
    "JHU": {
        "2020-2024": {"NeurIPS": 43, "ICML": 14, "ICLR": 27, "AAAI": 16, "IJCAI": 4, "KDD": 1, "CVPR": 69, "ICCV": 19, "ECCV": 32, "COLT": 2, "MLSys": 0, "ACL": 50, "EMNLP": 22},
        "2014-2019": {"NeurIPS": 11, "ICML": 17, "ICLR": 1, "AAAI": 29, "IJCAI": 6, "KDD": 0, "CVPR": 62, "ICCV": 25, "ECCV": 20, "COLT": 0, "MLSys": 0, "ACL": 48, "EMNLP": 20},
    },
    "Northwestern": {
        "2020-2024": {"NeurIPS": 29, "ICML": 33, "ICLR": 18, "AAAI": 6, "IJCAI": 2, "KDD": 0, "CVPR": 1, "ICCV": 2, "ECCV": 0, "COLT": 2, "MLSys": 1, "ACL": 7, "EMNLP": 2},
        "2014-2019": {"NeurIPS": 11, "ICML": 13, "ICLR": 0, "AAAI": 13, "IJCAI": 1, "KDD": 2, "CVPR": 1, "ICCV": 0, "ECCV": 0, "COLT": 0, "MLSys": 0, "ACL": 4, "EMNLP": 4},
    },
    "Princeton": {
        "2020-2024": {"NeurIPS": 131, "ICML": 63, "ICLR": 86, "AAAI": 8, "IJCAI": 1, "KDD": 1, "CVPR": 36, "ICCV": 9, "ECCV": 11, "COLT": 21, "MLSys": 1, "ACL": 16, "EMNLP": 15},
        "2014-2019": {"NeurIPS": 33, "ICML": 60, "ICLR": 0, "AAAI": 5, "IJCAI": 2, "KDD": 0, "CVPR": 23, "ICCV": 10, "ECCV": 5, "COLT": 15, "MLSys": 0, "ACL": 7, "EMNLP": 7},
    },
    "PSU": {
        "2020-2024": {"NeurIPS": 37, "ICML": 5, "ICLR": 20, "AAAI": 53, "IJCAI": 15, "KDD": 35, "CVPR": 9, "ICCV": 4, "ECCV": 8, "COLT": 0, "MLSys": 0, "ACL": 29, "EMNLP": 10},
        "2014-2019": {"NeurIPS": 3, "ICML": 5, "ICLR": 0, "AAAI": 29, "IJCAI": 10, "KDD": 23, "CVPR": 11, "ICCV": 1, "ECCV": 3, "COLT": 1, "MLSys": 0, "ACL": 16, "EMNLP": 8},
    },
    "Purdue": {
        "2020-2024": {"NeurIPS": 55, "ICML": 22, "ICLR": 32, "AAAI": 22, "IJCAI": 7, "KDD": 0, "CVPR": 22, "ICCV": 3, "ECCV": 7, "COLT": 3, "MLSys": 0, "ACL": 6, "EMNLP": 0},
        "2014-2019": {"NeurIPS": 10, "ICML": 14, "ICLR": 1, "AAAI": 20, "IJCAI": 9, "KDD": 5, "CVPR": 11, "ICCV": 7, "ECCV": 2, "COLT": 0, "MLSys": 0, "ACL": 7, "EMNLP": 1},
    },
    "Rice University": {
        "2020-2024": {"NeurIPS": 35, "ICML": 24, "ICLR": 22, "AAAI": 18, "IJCAI": 15, "KDD": 11, "CVPR": 13, "ICCV": 6, "ECCV": 9, "COLT": 2, "MLSys": 5, "ACL": 0, "EMNLP": 1},
        "2014-2019": {"NeurIPS": 7, "ICML": 15, "ICLR": 0, "AAAI": 22, "IJCAI": 16, "KDD": 12, "CVPR": 7, "ICCV": 4, "ECCV": 1, "COLT": 0, "MLSys": 0, "ACL": 0, "EMNLP": 0},
    },
    "Stanford": {
        "2020-2024": {"NeurIPS": 192, "ICML": 89, "ICLR": 132, "AAAI": 28, "IJCAI": 6, "KDD": 3, "CVPR": 89, "ICCV": 28, "ECCV": 27, "COLT": 15, "MLSys": 2, "ACL": 65, "EMNLP": 32},
        "2014-2019": {"NeurIPS": 56, "ICML": 57, "ICLR": 2, "AAAI": 25, "IJCAI": 11, "KDD": 6, "CVPR": 74, "ICCV": 28, "ECCV": 22, "COLT": 11, "MLSys": 0, "ACL": 32, "EMNLP": 32},
    },
    "UCLA": {
        "2020-2024": {"NeurIPS": 160, "ICML": 95, "ICLR": 102, "AAAI": 61, "IJCAI": 12, "KDD": 21, "CVPR": 27, "ICCV": 7, "ECCV": 7, "COLT": 5, "MLSys": 0, "ACL": 85, "EMNLP": 24},
        "2014-2019": {"NeurIPS": 35, "ICML": 53, "ICLR": 2, "AAAI": 37, "IJCAI": 39, "KDD": 21, "CVPR": 10, "ICCV": 7, "ECCV": 7, "COLT": 0, "MLSys": 0, "ACL": 15, "EMNLP": 8},
    },
    "UCSB": {
        "2020-2024": {"NeurIPS": 22, "ICML": 15, "ICLR": 27, "AAAI": 11, "IJCAI": 3, "KDD": 3, "CVPR": 11, "ICCV": 3, "ECCV": 3, "COLT": 0, "MLSys": 0, "ACL": 26, "EMNLP": 9},
        "2014-2019": {"NeurIPS": 4, "ICML": 1, "ICLR": 0, "AAAI": 6, "IJCAI": 7, "KDD": 11, "CVPR": 8, "ICCV": 7, "ECCV": 3, "COLT": 0, "MLSys": 0, "ACL": 27, "EMNLP": 17},
    },
    "UIUC": {
        "2020-2024": {"NeurIPS": 134, "ICML": 69, "ICLR": 104, "AAAI": 44, "IJCAI": 9, "KDD": 75, "CVPR": 67, "ICCV": 32, "ECCV": 35, "COLT": 4, "MLSys": 4, "ACL": 83, "EMNLP": 37},
        "2014-2019": {"NeurIPS": 39, "ICML": 31, "ICLR": 1, "AAAI": 34, "IJCAI": 29, "KDD": 77, "CVPR": 72, "ICCV": 30, "ECCV": 36, "COLT": 4, "MLSys": 0, "ACL": 41, "EMNLP": 27},
    },
    "UMD": {
        "2020-2024": {"NeurIPS": 136, "ICML": 74, "ICLR": 109, "AAAI": 77, "IJCAI": 15, "KDD": 10, "CVPR": 69, "ICCV": 44, "ECCV": 37, "COLT": 3, "MLSys": 0, "ACL": 43, "EMNLP": 27},
        "2014-2019": {"NeurIPS": 24, "ICML": 29, "ICLR": 0, "AAAI": 62, "IJCAI": 30, "KDD": 16, "CVPR": 40, "ICCV": 19, "ECCV": 21, "COLT": 1, "MLSys": 0, "ACL": 32, "EMNLP": 26},
    },
    "Univ. of California - Berkeley": {
        "2020-2024": {"NeurIPS": 265, "ICML": 161, "ICLR": 178, "AAAI": 32, "IJCAI": 7, "KDD": 10, "CVPR": 71, "ICCV": 41, "ECCV": 39, "COLT": 23, "MLSys": 21, "ACL": 24, "EMNLP": 12},
        "2014-2019": {"NeurIPS": 79, "ICML": 121, "ICLR": 9, "AAAI": 15, "IJCAI": 18, "KDD": 3, "CVPR": 77, "ICCV": 40, "ECCV": 30, "COLT": 28, "MLSys": 0, "ACL": 11, "EMNLP": 8},
    },
    "Univ. of California - San Diego": {
        "2020-2024": {"NeurIPS": 118, "ICML": 71, "ICLR": 83, "AAAI": 33, "IJCAI": 4, "KDD": 22, "CVPR": 96, "ICCV": 51, "ECCV": 38, "COLT": 29, "MLSys": 0, "ACL": 56, "EMNLP": 27},
        "2014-2019": {"NeurIPS": 40, "ICML": 35, "ICLR": 0, "AAAI": 22, "IJCAI": 16, "KDD": 14, "CVPR": 75, "ICCV": 29, "ECCV": 25, "COLT": 18, "MLSys": 0, "ACL": 30, "EMNLP": 13},
    },
    "University of Pennsylvania": {
        "2020-2024": {"NeurIPS": 39, "ICML": 36, "ICLR": 26, "AAAI": 6, "IJCAI": 1, "KDD": 0, "CVPR": 20, "ICCV": 5, "ECCV": 12, "COLT": 3, "MLSys": 0, "ACL": 45, "EMNLP": 11},
        "2014-2019": {"NeurIPS": 15, "ICML": 23, "ICLR": 0, "AAAI": 14, "IJCAI": 9, "KDD": 2, "CVPR": 32, "ICCV": 12, "ECCV": 11, "COLT": 2, "MLSys": 0, "ACL": 32, "EMNLP": 25},
    },
    "University_of_North_Carolina": {
        "2020-2024": {"NeurIPS": 62, "ICML": 33, "ICLR": 51, "AAAI": 28, "IJCAI": 3, "KDD": 6, "CVPR": 31, "ICCV": 13, "ECCV": 14, "COLT": 0, "MLSys": 0, "ACL": 48, "EMNLP": 13},
        "2014-2019": {"NeurIPS": 6, "ICML": 5, "ICLR": 1, "AAAI": 19, "IJCAI": 2, "KDD": 2, "CVPR": 18, "ICCV": 5, "ECCV": 2, "COLT": 0, "MLSys": 0, "ACL": 17, "EMNLP": 17},
    },
    "USC": {
        "2020-2024": {"NeurIPS": 45, "ICML": 26, "ICLR": 31, "AAAI": 44, "IJCAI": 10, "KDD": 4, "CVPR": 17, "ICCV": 6, "ECCV": 7, "COLT": 8, "MLSys": 2, "ACL": 66, "EMNLP": 12},
        "2014-2019": {"NeurIPS": 14, "ICML": 18, "ICLR": 0, "AAAI": 25, "IJCAI": 20, "KDD": 14, "CVPR": 23, "ICCV": 10, "ECCV": 15, "COLT": 0, "MLSys": 0, "ACL": 14, "EMNLP": 12},
    },
    "UTAustin": {
        "2020-2024": {"NeurIPS": 124, "ICML": 64, "ICLR": 91, "AAAI": 32, "IJCAI": 4, "KDD": 1, "CVPR": 46, "ICCV": 19, "ECCV": 22, "COLT": 18, "MLSys": 0, "ACL": 37, "EMNLP": 16},
        "2014-2019": {"NeurIPS": 26, "ICML": 30, "ICLR": 2, "AAAI": 38, "IJCAI": 23, "KDD": 2, "CVPR": 30, "ICCV": 18, "ECCV": 12, "COLT": 8, "MLSys": 0, "ACL": 17, "EMNLP": 13},
    },
    "UW": {
        "2020-2024": {"NeurIPS": 153, "ICML": 67, "ICLR": 113, "AAAI": 17, "IJCAI": 2, "KDD": 3, "CVPR": 36, "ICCV": 18, "ECCV": 12, "COLT": 19, "MLSys": 1, "ACL": 126, "EMNLP": 54},
        "2014-2019": {"NeurIPS": 42, "ICML": 50, "ICLR": 0, "AAAI": 19, "IJCAI": 8, "KDD": 2, "CVPR": 33, "ICCV": 9, "ECCV": 13, "COLT": 14, "MLSys": 0, "ACL": 73, "EMNLP": 58},
    },
    "UWMadison": {
        "2020-2024": {"NeurIPS": 93, "ICML": 44, "ICLR": 39, "AAAI": 16, "IJCAI": 1, "KDD": 0, "CVPR": 23, "ICCV": 11, "ECCV": 13, "COLT": 27, "MLSys": 9, "ACL": 3, "EMNLP": 0},
        "2014-2019": {"NeurIPS": 24, "ICML": 38, "ICLR": 1, "AAAI": 14, "IJCAI": 4, "KDD": 3, "CVPR": 21, "ICCV": 8, "ECCV": 9, "COLT": 16, "MLSys": 0, "ACL": 2, "EMNLP": 2},
    },
    "Yale": {
        "2020-2024": {"NeurIPS": 60, "ICML": 20, "ICLR": 18, "AAAI": 6, "IJCAI": 2, "KDD": 5, "CVPR": 5, "ICCV": 1, "ECCV": 7, "COLT": 15, "MLSys": 0, "ACL": 12, "EMNLP": 3},
        "2014-2019": {"NeurIPS": 18, "ICML": 20, "ICLR": 0, "AAAI": 8, "IJCAI": 4, "KDD": 2, "CVPR": 3, "ICCV": 1, "ECCV": 0, "COLT": 12, "MLSys": 0, "ACL": 0, "EMNLP": 3},
    },
}

# List of conferences for consistent ordering
conferences = ["NeurIPS", "ICML", "ICLR", "AAAI", "IJCAI", "KDD", "CVPR", "ICCV", "ECCV", "COLT", "MLSys", "ACL", "EMNLP"]

# Output directory
output_dir = '/home/gs285/DBLP_scrape/conference_sum'

# Function to create grouped bar charts for each university
def create_bar_chart(data, university, output_dir):
    labels = conferences
    year_ranges = list(data.keys())
    
    x = np.arange(len(labels))  # Label locations
    width = 0.35  # Bar width

    fig, ax = plt.subplots(figsize=(12, 8))
    
    bars1 = ax.bar(x - width/2, [data[year_ranges[0]].get(conf, 0) for conf in labels], width, label=year_ranges[0], color='skyblue')
    bars2 = ax.bar(x + width/2, [data[year_ranges[1]].get(conf, 0) for conf in labels], width, label=year_ranges[1], color='salmon')
    
    # Add some text for labels, title, and custom x-axis tick labels, etc.
    ax.set_xlabel('Conference', fontsize=14)
    ax.set_ylabel('Number of Papers', fontsize=14)
    ax.set_title(f'{university} Conference Paper Counts (2020-2024 vs 2014-2019)', fontsize=16)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=12)
    ax.legend()

    # Add value labels on top of bars
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
    output_path = f"{output_dir}/{university}_conference_summary.png"
    plt.savefig(output_path)
    plt.close()

    print(f"Saved plot for {university} at {output_path}")

# Generate and save bar charts for each university
for university, university_data in data.items():
    create_bar_chart(university_data, university, output_dir)
