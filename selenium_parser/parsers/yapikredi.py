from . import browser
import time
from bs4 import BeautifulSoup

def main():
    browser.get('https://www.yapikredi.com.tr/yatirimci-kosesi/doviz-bilgileri')
    time.sleep(5)
    file = open('index.txt', 'w', encoding='utf-8')
    soup = BeautifulSoup(browser.page_source.replace(',', '.'), 'html.parser')
    data_list = [[], ['yapikredi https://www.yapikredi.com.tr/yatirimci-kosesi/doviz-bilgileri'],
                 ['Валюта', 'Покупка', 'Продажа']]
    # Находим все строки <tr> с атрибутом data-expanded="true"
    rows = soup.find_all('tr', attrs={"data-expanded": "true"})


    for row in rows[:15]:
        data_row = []
        for td in row.find_all('td'):
            # Исключаем теги и берем только текст
            data_row.append(td.get_text(strip=True))
        print(data_row)
        data_list.append([data_row[0],data_row[2],data_row[3]])

    print(data_list[:15])
    file.close()
    data = data_list[:15]
    data.append([])
    return data

if __name__ == '__main__':
    main()