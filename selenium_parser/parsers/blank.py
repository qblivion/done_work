from . import browser
import time
from bs4 import BeautifulSoup


def main():
    browser.get("https://www.iktisatbank.com/doviz-kurlari")
    time.sleep(5)
    file = open("index.txt", "w", encoding="utf-8")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    print(soup, file=file)


if __name__ == "__main__":
    main()
