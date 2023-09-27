from . import browser
import time
from bs4 import BeautifulSoup


def main():
    browser.get(
        "http://www.kktcmerkezbankasi.org/tr/veriler/doviz_kurlari/kur_sorgulama"
    )
    time.sleep(5)
    file = open("index.txt", "w", encoding="utf-8")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    print(soup, file=file)
    # Находим все строки в таблице
    rows = soup.select("tbody tr")

    data = [
        [],
        ["http://www.kktcmerkezbankasi.org/tr/veriler/doviz_kurlari/kur_sorgulama"],
    ]

    for row in rows:
        # Извлечение кода валюты из текста
        currency_code = row.select_one("td").text.split("(")[-1].split(")")[0]
        # Извлечение двух числовых значений
        values = [td.text for td in row.select("td")[1:3]]
        data.append([currency_code] + values)

    return data[:13]


if __name__ == "__main__":
    main()
