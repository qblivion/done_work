import requests
import json


def main():
    url = "https://www.ing.com.tr/ProxyManagement/SiteManagerService_Script.aspx/GetCurrencyRates"

    payload = json.dumps({"date": "2023-09-02T01:26:00.000Z"})
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    data = json.loads(response.text)
    # Преобразуем JSON в двумерный список
    simplified_data = [
        [
            item["CurrencySymbol"],
            item["BuyingEffectiveRate"],
            item["SellingEffectiveRate"],
        ]
        for item in data["d"]
    ]
    simplified_data = [
        [],
        ["https://www.ing.com.tr/tr/bilgi-destek/yatirim/doviz-kurlari"],
    ] + simplified_data
    return simplified_data
