import telebot, sqlite3
from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='d1c464b0b83445ae9da3c591f22c9dfc')

list_hello = ("Привет", "Здравствуй", "Hello")

bot = telebot.TeleBot("1763079895:AAHl_i3dg7mnOw1Wiq8Yes-tktPfYFRhWDE", parse_mode=None)

help_message = "123"
def create_datab():
    sqlite_connection = sqlite3.connect('news_bot.db')
    sqlite_create_table_users = '''CREATE TABLE IF NOT EXISTS users (
                                        id INTEGER PRIMARY KEY,
                                        name TEXT NOT NULL)'''
    sqlite_create_table_category = '''CREATE TABLE IF NOT EXISTS categories (
                                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            name TEXT NOT NULL,
                                            user_id INTEGER SECONDARY KEY)'''
    sqlite_create_table_keywords = '''CREATE TABLE IF NOT EXISTS keywords (
                                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            name TEXT NOT NULL,
                                            user_id INTEGER SECONDARY KEY)'''

    cursor = sqlite_connection.cursor()
    print("БД подключена")
    cursor.execute(sqlite_create_table_users)
    cursor.execute(sqlite_create_table_category)
    cursor.execute(sqlite_create_table_keywords)
    sqlite_connection.commit()
    print("Таблицы БД созданы")
    cursor.close()
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.reply_to(message, help_message)

@bot.message_handler(func=lambda message: True)
def answer_to_message(message):
     print(message.from_user.id)
     if message.text in list_hello:
         bot.send_message(message.from_user.id, "И тебе привет!")
create_datab()
bot.polling()


#d1c464b0b83445ae9da3c591f22c9dfc