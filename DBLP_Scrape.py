import requests
from bs4 import BeautifulSoup
import json
import os

def get_professor_papers(dblp_url):

    # Send a request to the URL
    response = requests.get(dblp_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the information about the papers
    papers = []
    # Loop through all the <li> elements that have the class 'entry'
    #The <li> tag in HTML stands for "list item." It is used to represent an item in a list.
    for record in soup.find_all('li', class_='entry'):
        paper = {}
        # Paper title
        '''
        he <span> tag is an inline container used in HTML. 
        It doesn't inherently represent anything specific but is often used to group a portion of text or HTML elements for styling or scripting purposes.
        '''
        # paper['title'] = record.find('span', class_='title').text
        # Extract the title of the paper
        title_element = record.find('span', class_='title')
        if title_element:
            paper['title'] = title_element.get_text().strip()
        else:
            paper['title'] = "Unknown"
        

        # Extract the conference/journal name
        conference_element = record.find('span', itemprop='isPartOf')
        if conference_element:
            conference_name_element = conference_element.find('span', itemprop='name')
            if conference_name_element:
                paper['conference_journal'] = conference_name_element.get_text().strip()
            else:
                paper['conference_journal'] = "Unknown"
        else:
            paper['conference_journal'] = "Unknown"

        # Extract the year
        year_element = record.find('span', itemprop='datePublished')
        if year_element:
            paper['year'] = year_element.get_text().strip()
        else:
            paper['year'] = "Unknown"
        
        # Extract the DOI link
        doi_element = record.find('a', href=True)
        if doi_element and 'doi.org' in doi_element['href']:
            paper['doi_link'] = doi_element['href']
        else:
            paper['doi_link'] = "Unknown"

        # Convert year to an integer and check if it's within the last 10 years
        if paper['year'].isdigit():
            year = int(paper['year'])
            if 2014 <= year <= 2024:
                papers.append(paper)
    
    return papers

def save_to_json(data, filename):
    # Define the folder path
    folder_path = '/home/gs285/DBLP_scrape/result/Yale'

    # Create the full file path
    file_path = os.path.join(folder_path, filename)

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


def main():
    with open('/home/gs285/DBLP_scrape/faculty_information/faculty_information/faculty_Yale.json', 'r') as f:
        faculty_data = json.load(f)
    
    for professor in faculty_data:
        dblp_url = professor.get('dblp')
        name = professor.get('name')
        
        if dblp_url:
            print(f"Processing papers for {name}...")
            papers = get_professor_papers(dblp_url)
            if papers:
                save_to_json(papers, f"{name.replace(' ', '_')}_papers.json")
                print(f"Data saved to {name.replace(' ', '_')}_papers.json")
            else:
                print(f"No papers found for {name}.")
        else:
            print(f"No DBLP link found for {name}. Skipping.")

if __name__ == "__main__":
    main()
