import telebot, sqlite3
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='d1c464b0b83445ae9da3c591f22c9dfc')
list_category = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
list_hello = ("Привет", "Здравствуй", "Hello")

bot = telebot.TeleBot("1763079895:AAHl_i3dg7mnOw1Wiq8Yes-tktPfYFRhWDE", parse_mode=None)

help_message ="Говноновостной бот. /start, зарегаться.\n/add_category *категория* - добавить категорию.\n/delete_category *категория* - удалить категорию.\n/delete_category all - удалить все категории.\nАналогично с keywordsами.\n/get_news - получить новости"


# print (help(newsapi.get_top_headlines))

@bot.message_handler(commands=['help'])
def handle_start_help(message):
    bot.send_message(message.from_user.id,help_message)
    # print(dir(message.from_user))
    bot.reply_to(message, dir(message.from_user))


@bot.message_handler(commands=['start'])
def user_reg(message):
    try:
        user_id = message.from_user.id
        nick = message.from_user.username
        sql_record = f'''INSERT INTO users (id, name) VALUES ({user_id}, "{nick}")'''
        sqlite_connection = sqlite3.connect('news_bot.db')
        cursor = sqlite_connection.cursor()
        cursor.execute(sql_record)
        sqlite_connection.commit()
        cursor.close()
        print("Пользователь зарегистрирован")
        bot.send_message(message.from_user.id, "Пользователь зарегистрирован")
    except:
        print('kakaya to zalupa')
        bot.reply_to(message, 'kakaya to zalupa')


@bot.message_handler(commands=['add_category'])
def add_category(message):
    try:
        message.text.split(" ")
        print(message.text.split(" "))
        if message.text.split(" ")[1] in list_category:
            user_id = message.from_user.id
            print(user_id)
            sql_record_categories = f'''INSERT INTO categories (user_id, name) VALUES ({user_id}, "{message.text.split(" ")[1]}")'''
            sqlite_connection = sqlite3.connect('news_bot.db')
            cursor = sqlite_connection.cursor()
            cursor.execute(sql_record_categories)
            sqlite_connection.commit()
            cursor.close()
            bot.send_message(message.from_user.id, "Категория успешно добавлена")
        else:
            bot.send_message(message.from_user.id,
                             '''Таких категорий нет. Введите категории из списка: business","entertainment","general","health","science","sports","technology"''')
    except:
        print("kakaya to zalupa while adding categories")
        bot.send_message(message.from_user.id, "kakaya to zalupa while adding categories")


@bot.message_handler(commands=['delete_category'])
def delete_category(message):
    try:
        message.text.split(" ")
        print(message.text.split(" "))
        if message.text.split(" ")[1] in list_category:
            user_id = message.from_user.id
            sql_delete_categories = f'''DELETE FROM categories WHERE name = "{message.text.split(" ")[1]}"'''
            sqlite_connection = sqlite3.connect('news_bot.db')
            cursor = sqlite_connection.cursor()
            cursor.execute(sql_delete_categories)
            sqlite_connection.commit()
            cursor.close()
            bot.send_message(message.from_user.id, "Категория удалена")
        elif message.text.split(" ")[1] == "all":
            user_id = message.from_user.id
            sql_delete_categories = f'''DELETE FROM categories WHERE user_id = "{user_id}"'''
            sqlite_connection = sqlite3.connect('news_bot.db')
            cursor = sqlite_connection.cursor()
            cursor.execute(sql_delete_categories)
            sqlite_connection.commit()
            cursor.close()
            bot.send_message(message.from_user.id, "Все категории удалены")
        else:
            bot.send_message(message.from_user.id,
                             '''Таких категорий нет. Введите категории из списка: business","entertainment","general","health","science","sports","technology"''')
    except:
        print("kakaya to zalupa while deleting categories")
        bot.send_message(message.from_user.id, "kakaya to zalupa while deleting categories")


@bot.message_handler(commands=['add_keywords'])
def add_keywords(message):
    try:
        message.text.split(" ")
        print(message.text.split(" "))
        user_id = message.from_user.id
        print(user_id)
        print(message.text.split(" ")[1])
        sql_record_keywords = f'''INSERT INTO keywords(name, user_id) VALUES ("{message.text.split(" ")[1]}",{user_id})'''
        sqlite_connection = sqlite3.connect('news_bot.db')
        cursor = sqlite_connection.cursor()
        cursor.execute(sql_record_keywords)
        sqlite_connection.commit()
        cursor.close()
        bot.send_message(message.from_user.id, "Слово успешно добавлено")
    except:
        print("kakaya to zalupa while adding keywords")
        bot.send_message(message.from_user.id, "kakaya to zalupa while adding keywords")


@bot.message_handler(commands=['delete_keywords'])
def delete_keywords(message):
    try:
        if message.text.split(" ")[1] == "all":
            user_id = message.from_user.id
            sql_delete_categories = f'''DELETE FROM keywords WHERE user_id = {user_id}'''
            sqlite_connection = sqlite3.connect('news_bot.db')
            cursor = sqlite_connection.cursor()
            cursor.execute(sql_delete_categories)
            sqlite_connection.commit()
            cursor.close()
            bot.send_message(message.from_user.id, "Все слова удалены")
        else:
            message.text.split(" ")
            print(message.text.split(" "))
            user_id = message.from_user.id
            print(user_id)
            sql_record_keywords = f'''DELETE FROM keywords WHERE name = "{message.text.split(" ")[1]}"'''
            sqlite_connection = sqlite3.connect('news_bot.db')
            cursor = sqlite_connection.cursor()
            cursor.execute(sql_record_keywords)
            sqlite_connection.commit()
            cursor.close()
            bot.send_message(message.from_user.id, "Слово успешно удалено")
    except:
        print("kakaya to zalupa while deleting keywords")
        bot.send_message(message.from_user.id, "kakaya to zalupa while deleting keywords")


@bot.message_handler(commands=['get_news'])
def get_news(message):
    message.text.split(" ")
    print(message.text.split(" "))
    user_id = message.from_user.id
    sql_get_news_keywords = f'''SELECT name FROM keywords WHERE user_id = {user_id}'''
    sql_get_news_categories = f'''SELECT name FROM categories WHERE user_id = {user_id}'''
    sqlite_connection = sqlite3.connect('news_bot.db')
    cursor = sqlite_connection.cursor()
    cursor.execute(sql_get_news_keywords)
    user_id = cursor.fetchone()
    if user_id is None:
        bot.send_message(message.chat.id, 'Ваш аккаунт не зареган, попробуйте команду /start')
    else:
        cursor.execute(sql_get_news_categories)
        categories = cursor.fetchall()
        sqlite_connection.close()
        sqlite_connection = sqlite3.connect('news_bot.db')
        cursor = sqlite_connection.cursor()
        cursor.execute(sql_get_news_keywords)
        keywords = cursor.fetchall()
        sqlite_connection.close()
        news_url = []
        for cats in categories:
            for key in keywords:
                top_headLines = newsapi.get_top_headlines(category=cats[0], q=key[0], language='ru')
                new_data = top_headLines
                for data in new_data['articles']:
                    news_url.append(data["url"])
        for key in keywords:
            top_headLines = newsapi.get_top_headlines(q=key[0], language='ru')
            new_data = top_headLines
            for data in new_data['articles']:
                news_url.append(data["url"])
        for cats in categories:
            top_headLines = newsapi.get_top_headlines(category=cats[0], language='ru')
            new_data = top_headLines
            for data in new_data['articles']:
                news_url.append(data["url"])
    count = 0
    while count != 10:
        bot.send_message(message.chat.id, news_url[count])
        count += 1


@bot.message_handler(func=lambda message: True)
def answer_to_message(message):
    print(message.from_user.id)
    if message.text in list_hello:
        bot.send_message(message.from_user.id, "И тебе привет!")


bot.polling()

# d1c464b0b83445ae9da3c591f22c9dfc
# businessentertainmentgeneralhealthsciencesportstechnology
