from . import browser
import time
from bs4 import BeautifulSoup

def main():
    browser.get('https://www.tcmb.gov.tr/wps/wcm/connect/tr/tcmb+tr/main+page+site+area/bugun')
    time.sleep(5)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    # Находим все строки в tbody
    rows = soup.select('.kurlarTablo tbody tr')
    result = [[], ['https://www.tcmb.gov.tr/wps/wcm/connect/tr/tcmb+tr/main+page+site+area/bugun'],['Валюта','Покупка Факс', 'Продажа Факс', 'Покупка нал', 'Продажа нал']]
    for row in rows:
        kurkodu_element = row.select_one('.kurkodu')
        para_element = row.select_one('.para')
        
        # Если один из элементов не найден, пропускаем эту строку
        if not kurkodu_element or not para_element:
            continue

        # Извлекаем текст из каждой ячейки в строке
        kurkodu = kurkodu_element.text.strip()
        para = para_element.text.strip()
        deger_values = [deger.text.strip() for deger in row.select('.deger')]

        # Добавляем строку в результат
        result.append([kurkodu] + deger_values)
    print(result)
    return result[:25]


if __name__ == '__main__':
    main()