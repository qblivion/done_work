import time
import csv

bot_token = "6362745691:AAF0LAXC-BM_Hr_gwXp7b02kZj6sybTmkgQ"


def add_current_time_to_rows(rows):
    current_time = time.strftime("%d.%m.%Y %H:%M")
    for row in rows:
        if len(row) >= 3:
            row.append(current_time)
    return rows


def update_csv_file(filename, new_rows):
    # Шаг 1: Прочитать существующий файл и сохранить его содержимое
    with open(filename, "r", encoding="utf-8") as file:
        current_content = file.readlines()

    # Преобразование new_rows в строки для записи
    new_rows_as_strings = []
    for row in new_rows:
        new_rows_as_strings.append(",".join(map(str, row)) + "\n")

    # Объединение new_rows и current_content
    combined_content = new_rows_as_strings + current_content

    # Шаг 2: Открыть файл для записи и записать объединенное содержимое
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(combined_content)
