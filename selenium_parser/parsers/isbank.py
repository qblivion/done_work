from . import browser

import time
from bs4 import BeautifulSoup


def main():
    browser.get("https://www.isbank.com.tr/doviz-kurlari")
    time.sleep(5)
    file = open("index.txt", "w", encoding="utf-8")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    print(soup, file=file)
    data = [
        [],
        ["https://www.isbank.com.tr/doviz-kurlari"],
        ["Валюта", "Покупка", "Продажа"],
    ]
    for j in range(12):
        if j < 10:
            j = "0" + str(j)
        element = soup.find_all(
            "tr",
            id=f"ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73_ctl00_FxRatesRepeater_ctl{j}_fxItem",
        )[0]
        # print(elements, file=file)
        currency = element.find("td").text.strip().split()[0]
        buy_rate = element.find_all("td")[1].text.strip().replace(",", ".").split()[0]
        sell_rate = element.find_all("td")[2].text.strip().replace(",", ".").split()[0]
        print(" ".join(f"{currency} {buy_rate} {sell_rate}".split()), file=file)
        data.append([currency, buy_rate, sell_rate])

    file.close()
    print(data)
    return data


if __name__ == "__main__":
    main()
