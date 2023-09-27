from . import browser
import time
from bs4 import BeautifulSoup


def main():
    browser.get("https://webforms.garantibbva.com.tr/currency-convertor/?lang=tr")
    time.sleep(10)
    file = open("index.txt", "w", encoding="utf-8")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    print(browser.page_source, file=file)
    rows = soup.select(".currency-table .row")
    data = []
    for row in rows:
        code = row.select_one("p").text.strip()  # Получение кода валюты, например USD
        name = row.select_one(
            "div.cellCurrText > p"
        ).text.strip()  # Получение названия валюты, например "Amerikan Doları"
        buy_price = row.select_one(
            "div.currencyTableOtherColumns:nth-child(2)"
        ).text.strip()  # Получение цены покупки
        sell_price = row.select_one(
            "div.currencyTableOtherColumns:nth-child(3)"
        ).text.strip()  # Получение цены продажи
        change = row.select_one("div.cell.plus").text.strip()  # Получение изменения

        data.append(f"{code}\n{name} {buy_price} {sell_price} {change}")
    print(data)
    file.close()
    return data


if __name__ == "__main__":
    main()
