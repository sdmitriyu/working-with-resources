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

    # Запишем заголовки столбцов в CSV файл
    csvwriter.writerow(['Rank', 'Name', 'Price', 'Market Cap', 'Volume', 'Change'])

    for row in rows[1:101]:  # пропустим заголовок
        cells = row.find_all('td')
        rank = cells[0].text.strip()
        name = cells[1].text.strip()
        price = cells[3].text.strip()
        market_cap = cells[6].text.strip()
        volume = cells[7].text.strip()
        change = cells[8].text.strip()

        csvwriter.writerow([rank, name, price, market_cap, volume, change])

print('Данные успешно записаны в crypto_data.csv')
