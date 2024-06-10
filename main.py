import requests
from bs4 import BeautifulSoup
import csv
import datetime


def write_cmc_top():
    url = 'https://coinmarketcap.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим первые 100 криптовалют
    coin_rows = soup.select('.cmc-table-row')
    total_market_cap = sum([float(row.select_one('[data-sort="market_cap"]')['data-sort']) for row in coin_rows[:100]])

    # Записываем данные в CSV файл
    timestamp = datetime.datetime.now().strftime('%H.%M %d.%m.%Y')
    with open(f'{timestamp}.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=' ')
        writer.writerow(['Name', 'MC', 'MP'])

        for row in coin_rows[:100]:
            name = row.select_one('.cmc-table__column-name').get_text(strip=True)
            market_cap = row.select_one('[data-sort="market_cap"]')['data-sort']
            market_percentage = (float(market_cap) / total_market_cap) * 100

            writer.writerow([name, market_cap, f'{market_percentage:.2f}%'])


if __name__ == "__main__":
    write_cmc_top()
