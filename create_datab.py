import  sqlite3
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
create_datab()