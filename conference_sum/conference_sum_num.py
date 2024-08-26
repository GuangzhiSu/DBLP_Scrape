import os
import json

def count_papers_in_conferences(university_folders, years):
    # Define the current year and calculate the cutoff year
    current_year = 2024  # Assuming 2024 is the current year for this example
    cutoff_year = current_year - years + 1

    # List of conferences to track
    conferences = [
        "NeurIPS", "ICML", "ICLR", "AAAI", "IJCAI", "KDD",
        "CVPR", "ICCV", "ECCV", "COLT", "MLSys", "ACL", "EMNLP"
    ]

    # Initialize a dictionary to store the results for each university
    university_results = {}

    # Iterate over each university folder
    for folder_path in university_folders:
        # Initialize a dictionary to store counts for this university, split into two periods
        conference_count_latest = {conference: 0 for conference in conferences}
        conference_count_earlier = {conference: 0 for conference in conferences}
        
        # Iterate over all files in the folder
        for filename in os.listdir(folder_path):
            # Check if the file is a JSON file
            if filename.endswith(".json"):
                # Open and load the JSON file
                with open(os.path.join(folder_path, filename), 'r') as file:
                    data = json.load(file)
                    # Iterate over each entry in the JSON file
                    for entry in data:
                        # Get the year and conference_journal from the entry
                        year = int(entry.get("year", 0))
                        conference_journal = entry.get("conference_journal")

                        if conference_journal:
                            # Check if the year falls within the latest 'years' period
                            if cutoff_year <= year <= current_year:
                                if conference_journal.startswith("ECCV"):
                                    conference_count_latest["ECCV"] += 1
                                elif conference_journal.startswith("ACL"):
                                    conference_count_latest["ACL"] += 1
                                elif conference_journal in conference_count_latest:
                                    conference_count_latest[conference_journal] += 1
                            # Check if the year falls within the 2014 to (cutoff_year-1) period
                            elif 2014 <= year < cutoff_year:
                                if conference_journal.startswith("ECCV"):
                                    conference_count_earlier["ECCV"] += 1
                                elif conference_journal.startswith("ACL"):
                                    conference_count_earlier["ACL"] += 1
                                elif conference_journal in conference_count_earlier:
                                    conference_count_earlier[conference_journal] += 1
        
        # Store the results for this university
        university_name = os.path.basename(folder_path)
        university_results[university_name] = {
            f"{cutoff_year}-{current_year}": conference_count_latest,
            f"2014-{cutoff_year-1}": conference_count_earlier
        }

    return university_results

def save_results_to_file(university_results, output_file_path):
    # Save the results to a file
    with open(output_file_path, 'w') as output_file:
        for university, periods in university_results.items():
            output_file.write(f"{university}:\n")
            for period, counts in periods.items():
                output_file.write(f"  {period}:\n")
                for conference, count in counts.items():
                    output_file.write(f"    {conference}: {count}\n")
            output_file.write("\n")

    print(f"Conference summary saved to {output_file_path}")

# List of folder paths for each university
university_folders = [
    "/home/gs285/DBLP_scrape/result/Duke",
    "/home/gs285/DBLP_scrape/result/columbia",
    "/home/gs285/DBLP_scrape/result/Cornell",
    "/home/gs285/DBLP_scrape/result/Harvard",
    "/home/gs285/DBLP_scrape/result/JHU",
    "/home/gs285/DBLP_scrape/result/Northwestern",
    "/home/gs285/DBLP_scrape/result/Princeton",
    "/home/gs285/DBLP_scrape/result/PSU",
    "/home/gs285/DBLP_scrape/result/Purdue",
    "/home/gs285/DBLP_scrape/result/Rice University",
    "/home/gs285/DBLP_scrape/result/Stanford",
    "/home/gs285/DBLP_scrape/result/UCLA",
    "/home/gs285/DBLP_scrape/result/UCSB",
    "/home/gs285/DBLP_scrape/result/UIUC",
    "/home/gs285/DBLP_scrape/result/UMD",
    "/home/gs285/DBLP_scrape/result/Univ. of California - Berkeley",
    "/home/gs285/DBLP_scrape/result/Univ. of California - San Diego",
    "/home/gs285/DBLP_scrape/result/University of Pennsylvania",
    "/home/gs285/DBLP_scrape/result/University_of_North_Carolina",
    "/home/gs285/DBLP_scrape/result/USC",
    "/home/gs285/DBLP_scrape/result/UTAustin",
    "/home/gs285/DBLP_scrape/result/UW",
    "/home/gs285/DBLP_scrape/result/UWMadison",
    "/home/gs285/DBLP_scrape/result/Yale"
]

# Define the number of latest years to consider
latest_years = 5

# Count papers in conferences
university_results = count_papers_in_conferences(university_folders, latest_years)

# Define the output file path
output_file_path = "/home/gs285/DBLP_scrape/conference_sum/conference_summary.txt"

# Save the results to a file
save_results_to_file(university_results, output_file_path)
