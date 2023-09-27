from . import browser
import time
from bs4 import BeautifulSoup


def main():
    browser.get("https://www.iktisatbank.com/doviz-kurlari")
    time.sleep(5)
    file = open("index.txt", "w", encoding="utf-8")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    print(soup, file=file)
    table = soup.find("table", {"id": "dovizTablo"})

    # Извлекаем данные из таблицы
    rows = table.find("tbody").find_all("tr")[1:]  # Пропускаем заголовочную строку
    data = [[], ["https://www.iktisatbank.com/doviz-kurlari"]]

    for row in rows:
        currency = row.find_all("td")[0].text.strip()
        buy_rate = row.find_all("td")[1].text.strip()
        sell_rate = row.find_all("td")[2].text.strip()

        data.append([currency, buy_rate, sell_rate])

    return data


if __name__ == "__main__":
    main()
