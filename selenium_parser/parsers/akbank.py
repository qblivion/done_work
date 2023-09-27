from . import browser
import time
from bs4 import BeautifulSoup


def main():
    browser.get("https://www.akbank.com/doviz-kurlari")
    time.sleep(5)
    file = open("index.html", "w", encoding="utf-8")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    print(soup, file=file)
    # Находим все строки в таблице
    currency_data = soup.select(
        ".module620 .some_class"
    )  # Замените 'some_class' на соответствующий класс из HTML

    # Находим все строки в таблице
    rows = soup.find_all("tr")[22:]

    # Пустой список для хранения результатов
    result = [[], ["https://www.akbank.com/doviz-kurlari"]]

    i = 0
    while i < len(rows):
        row = rows[i]
        if row.td and "rs" in row.td.get(
            "class", []
        ):  # Проверяем, содержит ли строка атрибут "rs"
            currency = row.select_one(".curTxt").text

            # Вторая строка в таблице, содержащая значение SATIŞ
            next_row = rows[i + 1]

            # Получаем значения ALIŞ и SATIŞ
            alis_value = float(
                row.find_all("td")[2].text.replace(".", "").replace(",", ".")
            )
            satis_value = float(
                next_row.find_all("td")[1].text.replace(".", "").replace(",", ".")
            )

            result.append([currency, alis_value, satis_value])

            i += 2  # Переходим к следующему блоку из двух строк
        else:
            i += 1
    print(result)
    return result


if __name__ == "__main__":
    main()
