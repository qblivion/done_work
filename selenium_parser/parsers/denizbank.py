from bs4 import BeautifulSoup
import requests
import json


def main():
    url = 'https://www.denizbank.com/api/marketdata/exchanges'
    page = requests.get(url)

    # Десериализация JSON-строки
    data = json.loads(page.text)
    table = [[], ['https://www.denizbank.com/api/marketdata/exchanges'], ["Валюта", "Покупка", "Продажа"]]
    for item in data:
        row = [item["Code"], item["BuyingPrice"], item["SellingPrice"]]
        table.append(row)
    print(table)
    return table

if __name__ == '__main__':
    main()