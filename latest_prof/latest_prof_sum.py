import os
import json

# List of paths to faculty JSON files
faculty_files = [
    "/home/gs285/DBLP_scrape/faculty_information/faculty_Caltech.json",
    "/home/gs285/DBLP_scrape/faculty_information/faculty_Columbia_University.json",
    "/home/gs285/DBLP_scrape/faculty_information/faculty_Cornell.json",
    "/home/gs285/DBLP_scrape/faculty_information/faculty_Duke.json",
    "/home/gs285/DBLP_scrape/faculty_information/faculty_Harvard.json",
    "/home/gs285/DBLP_scrape/faculty_information/faculty_JHU.json",
    "/home/gs285/DBLP_scrape/faculty_information/faculty_Northwestern University.json",
    "/home/gs285/DBLP_scrape/faculty_information/faculty_Princeton.json",
    "/home/gs285/DBLP_scrape/faculty_information/faculty_PSU.json",
    "/home/gs285/DBLP_scrape/faculty_information/faculty_Purdue.json",
    "/home/gs285/DBLP_scrape/faculty_information/faculty_Rice University.json",
    "/home/gs285/DBLP_scrape/faculty_information/faculty_Stanford.json",
    "/home/gs285/DBLP_scrape/faculty_information/faculty_UCLA.json",
    "/home/gs285/DBLP_scrape/faculty_information/faculty_UCSB.json",
    "/home/gs285/DBLP_scrape/faculty_information/faculty_UIUC.json",
    "/home/gs285/DBLP_scrape/faculty_information/faculty_UMD.json",
    "/home/gs285/DBLP_scrape/faculty_information/faculty_Univ. of California - Berkeley.json",
    "/home/gs285/DBLP_scrape/faculty_information/faculty_Univ. of California - San Diego.json",
    "/home/gs285/DBLP_scrape/faculty_information/faculty_University of Pennsylvania.json",
    "/home/gs285/DBLP_scrape/faculty_information/faculty_University_of_North_Carolina.json",
    "/home/gs285/DBLP_scrape/faculty_information/faculty_USC.json",
    "/home/gs285/DBLP_scrape/faculty_information/faculty_UTAustin.json",
    "/home/gs285/DBLP_scrape/faculty_information/faculty_UW.json",
    "/home/gs285/DBLP_scrape/faculty_information/faculty_UWMadison.json",
    "/home/gs285/DBLP_scrape/faculty_information/faculty_Yale.json"
]

# Initialize counters
joined_in_latest_five_years = 0
joined_before_five_years = 0

# Initialize a list to store problematic entries
problematic_entries = []
missing_position_entries = []

# Function to determine if the career sequence is ascending or descending
def is_sequence_ascending(career_list):
    def extract_years(entry):
        years = []
        if 'position' in entry[1] and isinstance(entry[1]['position'], dict):
            for pos in entry[1]['position'].values():
                start_date = pos.get('start')
                if start_date and start_date.split("-")[0].isdigit():
                    year = int(start_date.split("-")[0])
                    years.append(year)
        return years

    first_entry_years = extract_years(career_list[0])
    second_entry_years = extract_years(career_list[1])

    if not first_entry_years or not second_entry_years:
        return True  # Default to ascending if no valid years

    return min(first_entry_years) < min(second_entry_years)

# Iterate over each JSON file
for faculty_file in faculty_files:
    with open(faculty_file, 'r') as file:
        faculty_data = json.load(file)
        # Iterate over each professor in the file
        for professor in faculty_data:
            career = professor.get("career", {})
            if career:
                # Convert the career dictionary to a list
                career_list = list(career.items())
                
                # Determine if the sequence is ascending or descending
                if len(career_list) > 1 and not is_sequence_ascending(career_list):
                    career_list.reverse()

                # Get the last university in the career
                last_university, last_university_info = career_list[-1]

                # Check if the 'position' field exists and is a dictionary
                if 'position' in last_university_info and isinstance(last_university_info['position'], dict):
                    # Extract the year from the start date, handling both "YYYY-MM" and "YYYY" formats
                    start_years = []
                    for pos in last_university_info['position'].values():
                        start_date = pos.get('start')
                        if start_date and start_date.split("-")[0].isdigit():
                            # If the date is in "YYYY-MM" format or "YYYY", extract "YYYY"
                            year = int(start_date.split("-")[0])
                            start_years.append(year)

                    if start_years:
                        earliest_start_year = min(start_years)

                        # Check if the professor joined the university in the latest five years
                        if earliest_start_year >= 2019:
                            joined_in_latest_five_years += 1
                        else:
                            joined_before_five_years += 1
                    else:
                        # If no valid start year, count as joined before five years
                        joined_before_five_years += 1
                else:
                    # Log the problematic entry
                    problematic_entries.append((faculty_file, professor['name']))

# Output the results to a file
output_file_path = "/home/gs285/DBLP_scrape/latest_prof/latest_prof_summary.txt"
with open(output_file_path, 'w') as output_file:
    output_file.write(f"Total number of professors who joined in the latest five years (2019-2024): {joined_in_latest_five_years}\n")
    output_file.write(f"Total number of professors who joined before 2019 or have no start year: {joined_before_five_years}\n")
    # # Log entries with missing 'position'
    # output_file.write("\nEntries with missing 'position':\n")
    # for entry in missing_position_entries:
    #     output_file.write(f"  File: {entry[0]}, Professor: {entry[1]}\n")

    # # Log entries with problematic 'position'
    # output_file.write("\nProblematic entries where 'position' is not a dictionary:\n")
    # for entry in problematic_entries:
    #     output_file.write(f"  File: {entry[0]}, Professor: {entry[1]}\n")

print(f"Professor joining summary saved to {output_file_path}")

if missing_position_entries or problematic_entries:
    print("Some entries had issues with 'position' being missing or not a dictionary. See the output file for details.")
else:
    print("All entries processed successfully without issues.")