from . import browser
import time
from bs4 import BeautifulSoup


def main():
    browser.get("https://finansmarket.vakifbank.com.tr/doviz")
    time.sleep(5)
    file = open("index.html", "w", encoding="utf-8")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    print(soup, file=file)

    # CSS-селекторы для извлечения информации:
    currency_selector = "div:nth-child(1) > div:nth-child(3) > div > div:nth-child(1) > div > div > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(1) > div > div > span"
    buy_price_selector = "div:nth-child(1) > div:nth-child(3) > div > div:nth-child(1) > div > div > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(2) > div > span"
    sell_price_selector = "div:nth-child(1) > div:nth-child(3) > div > div:nth-child(1) > div > div > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(3) > div > span"

    currency_element = soup.select_one(currency_selector)
    buy_price_element = soup.select_one(buy_price_selector)
    sell_price_element = soup.select_one(sell_price_selector)

    if currency_element and buy_price_element and sell_price_element:
        currency = currency_element.text.strip()
        buy_price = buy_price_element.text.strip().replace(",", ".")
        sell_price = sell_price_element.text.strip().replace(",", ".")
        print(
            f"Валюта: {currency}, Цена покупки: {buy_price}, Цена продажи: {sell_price}"
        )
    else:
        print("Некоторые элементы не найдены.")


if __name__ == "__main__":
    main()
