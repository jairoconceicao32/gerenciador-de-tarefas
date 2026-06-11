import sqlite3
class Connection:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
        
    def execute(self, query, params=None):
        if params is not None:
            return self.cur.execute(query, params)
        return self.cur.execute(query)

    def commit(self):
        return self.conn.commit()

    def get_id(self):
        return self.cur.lastrowid

    def fetchall(self):
        return self.cur.fetchall()
    
    def fetchone(self):
        return self.cur.fetchone()

    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
        return False

    def close(self):
        return self.conn.close()