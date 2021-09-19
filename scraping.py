#Web Scraping Tool: Grabbing the Core Curriculum Codes
#Prime website we want to scrape from: 
# For English Language Arts and Literacy (California): url: https://www.cde.ca.gov/be/st/ss/documents/finalelaccssstandards.pdf

# Libraries that will need to be installed in the requirements.txt for this: 
#pip install requests
#pip install html5lib
#pip install bs4 #This is version 4 of BeautifulSoup

import requests
from bs4 import BeautifulSoup
  
ELAcodes = "https://www.cde.ca.gov/be/st/ss/documents/finalelaccssstandards.pdf"
raw_results = requests.get(ELAcodes)
  
soup = BeautifulSoup(raw_results.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
print(soup.prettify())