from . import browser
import time
from bs4 import BeautifulSoup
import time


def main():
    browser.get("https://www.anadolubank.com.tr/doviz-kurlari")
    time.sleep(5)
    file = open("index.txt", "w", encoding="utf-8")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    print(soup, file=file)
    # Находим все строки в первом tbody
    rows = soup.select("div.col-12.mb-5 tbody.tdFirstElPL40 tr")

    data = [[], ["https://www.anadolubank.com.tr/doviz-kurlari"]]

    for row in rows:
        # Извлекаем название валюты
        currency_name = row.find("td").text.strip()
        # Извлекаем числовые значения
        numbers = [
            float(td.text.strip().replace(",", ".")) for td in row.find_all("td")[1:3]
        ]
        data.append([currency_name] + numbers)

    print(data)
    return data


if __name__ == "__main__":
    main()
