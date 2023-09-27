from . import browser
import time
from bs4 import BeautifulSoup

def main():
    browser.get('https://www.haremaltin.com')
    time.sleep(5)
    file = open('index.txt', 'w', encoding='utf-8')
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    print(soup, file=file)
    file.close()
    data_list = [[], ['https://www.haremaltin.com'], ['Название', 'Покупка', 'Продажа']]

    for tr in soup.find_all("tr"):
        # Имя
        name_element = tr.select_one(".span-isim")
        if name_element:
            name = name_element.text.strip().split("\n")[0]
        else:
            continue

        # Цена покупки
        alis_element = tr.select_one("[id^=alis__]")
        alis = alis_element.text.strip() if alis_element else ""

        # Цена продажи
        satis_element = tr.select_one("[id^=satis__]")
        satis = satis_element.text.strip() if satis_element else ""

        # Процентное изменение
        percentage_element = tr.select_one("[id^=yuzde__]")
        percentage = percentage_element.text.strip() if percentage_element else ""

        # Добавить данные в список
        data_list.append([name, alis, satis])
    print(data_list)
    return data_list

if __name__ == '__main__':
    main()