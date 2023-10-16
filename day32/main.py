import requests
import html
from bs4 import BeautifulSoup

# 1. Make an HTTP GET request and retrieve the web page content
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)_per_capita'
response = requests.get(url)
print("hello")
# Check for a successful request
dict={}
if response.status_code == 200:
    html = response.text

    # 2. Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # 3. Locate the table you want to scrape
    table = soup.findAll('table')
    table=table[1]


    if table:
        # 4. Extract data from the table
        for row in table.find_all('tr'):
            columns = row.find_all('td')
            # print(columns)
            if columns:
                dict[columns[0].get_text(strip=True).replace("\u202f*","")] = columns[2].get_text(strip=True).replace("\u202f*","")




    else:
        print("Table not found on the page.")
    for key, value in dict.items():
        print(key, value)


else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")


