import requests
from bs4 import BeautifulSoup
import csv

url = 'https://coinmarketcap.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', class_='cmc-table')
rows = table.find_all('tr')

with open('crypto_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)

    # Write column headers to CSV file
    csvwriter.writerow(['Rank', 'Name', 'Price', 'Market Cap', 'Volume', 'Change'])

    for row in rows[1:101]:  # skipping the header
        cells = row.find_all('td')

        # Check if there are enough cells to extract data from
        if len(cells) >= 7:
            rank = cells[0].text.strip()

            # Check if '<p>' tag exists before extracting text
            if cells[2].find('p'):
                name = cells[2].find('p').text.strip()
            else:
                name = cells[2].text.strip()

            price = cells[3].text.strip()
            market_cap = cells[4].text.strip()
            volume = cells[5].text.strip()
            change = cells[6].text.strip()

            csvwriter.writerow([rank, name, price, market_cap, volume, change])

print('Data has been successfully written to crypto_data.csv')
