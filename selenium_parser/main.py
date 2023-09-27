from parsers import (
    denizbank,
    isbank,
    haremaltin,
    yapikredi,
    tcmb,
    akbank,
    anadolubank,
    kktcmerkezbankasi,
    iktisatbank,
    ing,
    tradingview,
)
from aiogram import Bot, Dispatcher, executor, types
import config
from config import add_current_time_to_rows, update_csv_file
import asyncio

import csv

bot = Bot(token=config.bot_token)
dp = Dispatcher(bot)

text = ""
spread = 10
wh = True


@dp.message_handler(commands=["file"])
async def start(message: types.Message):
    global text
    file = open("пример.csv", "rb")
    await message.answer_document(file)


@dp.message_handler(commands=["percent"])
async def start(message: types.Message):
    await message.answer(
        "В ответ на это сообщение отправьте новое значение для уведомления"
    )


@dp.message_handler(commands=["stop"])
async def start(message: types.Message):
    wh = False
    await message.answer("Бот будет остановлен после завершения процесса")


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    global text, spread, wh
    wh = True
    await message.answer(f"Бот перезапущен спред{spread}")
    while wh:
        rows_to_add = []
        percent = 0
        data = tradingview.main()
        text = ""
        moex = round(1 / float(data[2][0]), 4)
        text += f"Информация\nКурс TRYRUB по MOEX: {moex}\n"
        rows_to_add.extend(add_current_time_to_rows(data))
        rows_to_add.extend(add_current_time_to_rows(yapikredi.main()))
        data = denizbank.main()
        percent = max(percent, round((moex - float(data[16][1])) / moex * 100, 3))
        text += f"DENIZBANK {round((moex - float(data[16][1]))/moex * 100, 3)}%\n"
        rows_to_add.extend(add_current_time_to_rows(data))
        rows_to_add.extend(add_current_time_to_rows(isbank.main()))
        rows_to_add.extend(add_current_time_to_rows(haremaltin.main()))
        data = tcmb.main()
        percent = max(percent, round((moex - float(data[16][1])) / moex * 100, 3))
        text += f"TCMB {round((moex - float(data[17][1]))/moex * 100, 3)}%\n"
        rows_to_add.extend(add_current_time_to_rows(data))  # коряво
        data = akbank.main()
        percent = max(percent, round((moex - float(data[16][1])) / moex * 100, 3))
        text += f"AKBANK {round((moex - float(data[15][2]))/moex * 100, 3)}%\n"
        rows_to_add.extend(add_current_time_to_rows(data))
        rows_to_add.extend(add_current_time_to_rows(anadolubank.main()))
        rows_to_add.extend(add_current_time_to_rows(kktcmerkezbankasi.main()))
        rows_to_add.extend(add_current_time_to_rows(iktisatbank.main()))
        data = ing.main()
        text += f"ING {round((moex - float(data[14][1]))/moex * 100, 3)}%\n"
        rows_to_add.extend(add_current_time_to_rows(data))
        update_csv_file("пример.csv", rows_to_add)

        if percent > spread:
            await message.answer(f"‼️ВНИМАНИЕ‼️ СПРЕД БОЛЬШЕ {spread}%")
            await message.answer(text, disable_notification=False)
        else:
            await message.answer(text, disable_notification=True)
        await asyncio.sleep(450)


@dp.message_handler()
async def start(message: types.Message):
    global spread
    if message.reply_to_message:
        if message.text.isnumeric():
            spread = float(message.text)
            await message.answer("Процент успешно изменен")
        else:
            await message.answer("Неверный формат")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
