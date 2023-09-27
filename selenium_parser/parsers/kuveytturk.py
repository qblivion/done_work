from . import browser
import time
from bs4 import BeautifulSoup


def main():
    browser.get("https://www.iktisatbank.com/doviz-kurlari")
    time.sleep(5)
    file = open("index.txt", "w", encoding="utf-8")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    print(soup, file=file)
    # Находим все блоки с информацией о валютах
    boxes = soup.select(".omegabox .box-borderless")

    # Инициализируем пустой список для хранения результатов
    results = []

    for box in boxes:
        # Извлекаем название валюты
        currency_name = box.h2.get_text(strip=True)

        # Извлекаем цены покупки и продажи
        prices = box.select(".insidebox p")
        if len(prices) >= 2:
            buy_price = (
                prices[0].get_text(strip=True).split()[0]
            )  # первый элемент содержит цену покупки
            sell_price = (
                prices[1].get_text(strip=True).split()[0]
            )  # второй элемент содержит цену продажи
            results.append([currency_name, buy_price, sell_price])
    return results


if __name__ == "__main__":
    main()
