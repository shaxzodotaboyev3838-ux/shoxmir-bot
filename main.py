try:
        bot.edit_message_media(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            media=media,
            reply_markup=get_cake_keyboard(index)
        )
    except Exception:
        pass

@bot.message_handler(func=lambda message: message.text == "🍱 Bento Tortlar")
def bento_tortlar(message):
    inline_kb = types.InlineKeyboardMarkup()
    order_text = "Salom! Men Bento tort buyurtma bermoqchiman."
    order_url = f"https://t.me/{ADMIN_USERNAME}?text={urllib.parse.quote(order_text)}"
    inline_kb.add(types.InlineKeyboardButton("🍱 Bento Buyurtma Berish", url=order_url))
    
    caption = (
        "<b>Bento Tortlar (Ixcham mini tortlar):</b>\n\n"
        "• <b>Sevishganlar uchun:</b> 'Love', bosh harflar (S+B), qizil yurakchali romantik dizaynlar\n"
        "• <b>Tug'ilgan kun uchun:</b> 'Happy Birthday' yozuvli va qizil lentalar bezaqlangan bento tortlar\n"
        "• <b>Shaxsiy yozuv:</b> Istalgan matn va xohishingizga ko'ra shaxsiy dizayn\n\n"
        "💰 <i>Narxi:</i> 80,000 so'm'dan boshlanadi"
    )
    bento_photo = "https://images.unsplash.com/photo-1535141192574-5d4897c13136?w=800"
    bot.send_photo(message.chat.id, photo=bento_photo, caption=caption, parse_mode="HTML", reply_markup=inline_kb)

@bot.message_handler(func=lambda message: message.text == "🍰 Shirinliklar")
def shirinliklar_menu(message):
    text = (
        "<b>Bizning shirinliklarimiz va narxlari:</b>\n\n"
        "🧁 <b>Mevali Kapkeyk:</b> 15,000 so'm (donasi)\n"
        "🍫 <b>Shokoladli Ekler:</b> 10,000 so'm (donasi)\n\n"
        f"Buyurtma berish uchun adminga yozing: @{ADMIN_USERNAME}"
    )
    bot.send_message(message.chat.id, text, parse_mode="HTML")

@bot.message_handler(func=lambda message: message.text == "📞 Aloqa")
def aloqa_menu(message):
    text = (
        "📞 <b>Biz bilan bog'lanish:</b>\n\n"
        f"• Telefon: {PHONE_NUMBER}\n"
        f"• Telegram administrator: @{ADMIN_USERNAME}"
    )
    bot.send_message(message.chat.id, text, parse_mode="HTML")

@bot.message_handler(func=lambda message: message.text == "📍 Joylashuv")
def location_menu(message):
    location_text = (
        "📍 <b>Bizning manzilimiz:</b>\n\n"
        "🍰 <b>Do'kon nomi:</b> Shox mir to'rt va shirinliklari\n"
        "▪️ <b>Viloyat/Tuman:</b> Xorazm viloyati, Yangiariq tumani\n"
        "▪️ <b>Mo'ljal:</b> Bolnitsa yoni, Hazrati G'oyib Ota Jome Masjidi yaqinida\n\n"
        "Sizni qandolatxonamizda kutib qolamiz! ✨"
    )
    bot.send_message(message.chat.id, location_text, parse_mode="HTML")
    try:
        # Yangiariq shaharchasidagi 9JC2+VV kodi bo'yicha aniq koordinatalar
        bot.send_location(message.chat.id, latitude=41.3641, longitude=60.6089)
    except Exception:
        pass

@bot.message_handler(func=lambda message: True)
def fallback_handler(message):
    bot.send_message(message.chat.id, "Iltimos, pastdagi menyu tugmalaridan foydalaning! 👇")

if name == 'main':
    print("To'xtovsiz bot ishga tushdi...")
    while True:
        try:
            bot.polling(non_stop=True, interval=1, timeout=20)
        except Exception as e:
            print(f"Ulanish uzildi, 3 soniyadan keyin qayta ulanadi: {e}")
            time.sleep(3)
