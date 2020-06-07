import sqlite3


class Database:

    def __init__(self):
        self.conn = sqlite3.connect("bot.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER)")
        self.conn.commit()

    def add_user(self, id):
        print("Inserted: " + str(id))
        self.cursor.execute("SELECT id FROM users WHERE id=("+str(id)+")")
        if len(self.cursor.fetchall()) == 0:
            self.cursor.execute("INSERT INTO users VALUES(" + str(id) + ")")
            self.conn.commit()


    def deactivate_user(self, id):
        print("Deleted: " + str(id))
        self.cursor.execute("DELETE FROM users WHERE id=" + str(id))
        self.conn.commit()

    def get_active(self):
        self.cursor.execute("SELECT id FROM users")
        items = self.cursor.fetchall()
        result = []
        for item in items:
            result.append(item[0])
        return result
