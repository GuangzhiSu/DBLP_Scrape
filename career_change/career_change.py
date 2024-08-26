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
before_assistant_after_assistant_count = 0
before_assistant_after_associate_count = 0
before_associate_count = 0

# Initialize a list to store files with missing 'position'
files_with_missing_position = []


# Function to determine if the career sequence is ascending or descending
def is_sequence_ascending(career_list):
    def extract_year(entry):
        years = []
        for pos in entry['position'].values():
            start_date = pos.get('start')
            if start_date and start_date.split("-")[0].isdigit():
                years.append(int(start_date.split("-")[0]))
        return years
    
    first_entry_years = extract_year(career_list[0][1])
    second_entry_years = extract_year(career_list[1][1])

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
            # Check if the professor has multiple career entries (multiple universities)
            if len(career) > 1:
                try:
                    # Convert the career dictionary to a list, assuming it's already sorted
                    career_list = list(career.items())

                    # Determine if the sequence is ascending or descending
                    if not is_sequence_ascending(career_list):
                        career_list.reverse()

                    # Get the last university before the current one and the current university
                    last_university, last_university_info = career_list[-2]
                    current_university, current_university_info = career_list[-1]

                    last_positions = last_university_info['position']
                    current_positions = current_university_info['position']

                    # Check if the professor's last position was Assistant or Associate Professor
                    if "Assistant Professor" in last_positions:
                        if "Assistant Professor" in current_positions:
                            before_assistant_after_assistant_count += 1
                        elif "Associate Professor" in current_positions:
                            before_assistant_after_associate_count += 1
                    elif "Associate Professor" in last_positions:
                        before_associate_count += 1

                except KeyError as e:
                    # Log the file and professor name if 'position' is missing
                    files_with_missing_position.append((faculty_file, professor['name']))

# Output the results and log of files with issues
output_file_path = "/home/gs285/DBLP_scrape/career_change/professor_position_summary.txt"
with open(output_file_path, 'w') as output_file:
    output_file.write(f"Total number of professors who were Assistant Professors before moving and stayed as Assistant Professors: {before_assistant_after_assistant_count}\n")
    output_file.write(f"Total number of professors who were Assistant Professors before moving and became Associate Professors: {before_assistant_after_associate_count}\n")
    output_file.write(f"Total number of professors who were Associate Professors before moving: {before_associate_count}\n")
    # output_file.write("\nFiles with missing 'position' key:\n")
    # for file, professor_name in files_with_missing_position:
    #     output_file.write(f"  File: {file}, Professor: {professor_name}\n")

print(f"Professor position summary saved to {output_file_path}")

# if files_with_missing_position:
#     print("Some files had missing 'position' data. See the output file for details.")
# else:
#     print("All files processed successfully without missing 'position' data.")
