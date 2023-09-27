from . import browser
import time
from bs4 import BeautifulSoup


def main():
    browser.get("https://ru.tradingview.com/chart/?symbol=FX%3AUSDTRY")
    time.sleep(5)
    file = open("index.txt", "w", encoding="utf-8")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    print(soup, file=file)
    selector = "body > div:nth-child(2) > div:nth-child(6) > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(2) > span:nth-child(1) > span:nth-child(1)"

    element = soup.select_one(selector)

    data = [["ДАННЫЕ С БИРЖИ MOEX"]]

    # Извлечение текста из элемента, игнорируя <sup>
    if element:
        price_text = "".join(
            element.stripped_strings
        )  # Объединяем все строки, исключая пробельные символы
        price = float(
            price_text.split("<")[0]
        )  # Извлекаем число перед "<", если оно есть
        print(price)
        data.append([price, "USDTRY"])
    else:
        print("Элемент не найден.")

    browser.get("https://ru.tradingview.com/chart/?symbol=MOEX%3ATRYRUB_TOM")
    time.sleep(5)

    soup = BeautifulSoup(browser.page_source, "html.parser")

    # Используем тот же CSS-селектор
    selector = "body > div:nth-child(2) > div:nth-child(6) > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(2) > span:nth-child(1) > span:nth-child(1)"

    element = soup.select_one(selector)

    # Извлечение текста из элемента
    if element:
        price = float(element.text.strip())  # Извлекаем и преобразуем текст в число
        data.append([price, "TRYRUB"])
        print(price)
    else:
        print("Элемент не найден.")

    browser.get("https://ru.tradingview.com/chart/?symbol=MOEX%3AUSDRUB_TOM")
    time.sleep(5)

    soup = BeautifulSoup(browser.page_source, "html.parser")

    selector = "body > div:nth-child(2) > div:nth-child(6) > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(2) > span:nth-child(1) > span:nth-child(1)"

    element = soup.select_one(selector)

    # Извлечение текста из элемента
    if element:
        price = float(element.text.strip())  # Извлекаем и преобразуем текст в число
        data.append([price, "USDRUB_TOM"])
        print(price)
    else:
        print("Элемент не найден.")

    return data


if __name__ == "__main__":
    main()
