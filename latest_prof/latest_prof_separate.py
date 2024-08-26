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

# Output file path
output_file_path = "/home/gs285/DBLP_scrape/latest_prof/all_universities_professor_summary.txt"

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

# Open the output file once and append all university data to it
with open(output_file_path, 'w') as output_file:
    # Iterate over each JSON file
    for faculty_file in faculty_files:
        joined_in_latest_five_years = 0
        joined_before_five_years = 0

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

        # Determine the university name based on the file name
        university_name = os.path.splitext(os.path.basename(faculty_file))[0].replace("faculty_", "")

        # Write the university's summary to the output file
        output_file.write(f"University: {university_name}\n")
        output_file.write(f"Total number of professors who joined in the latest five years (2019-2024): {joined_in_latest_five_years}\n")
        output_file.write(f"Total number of professors who joined before 2019 or have no start year: {joined_before_five_years}\n")
        output_file.write("\n")

print(f"All universities' professor joining summary saved to {output_file_path}")
