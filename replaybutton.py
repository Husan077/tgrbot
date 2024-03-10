
# button1 = KeyboardButton("kanalga qo'shish")
# button2 = KeyboardButton("turgunoff qilgan saytlar")

# keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1, button2)#
# @dp.message_handler()
# async def kb_answer(message: types.Message):
#     if message.text == "kanalga qo'shish":
#         await message.answer("https://t.me/turgunoff_portfolio")
#     elif message.text == "turgunoff qilgan saytlar":
#         await  message.answer("https://t.me/turgunoff_portfolio")
#     else:
#         await message.answer(f"bizga yozing : {message.text}")



# @dp.message_handler(commands=['start', "help"])
# async def kirish(message: types.Message):
#     await message.reply("Assalomu alaykum\nTurgunoff.uz botiga xush kelibsiz!", reply_markup=keyboard1)
