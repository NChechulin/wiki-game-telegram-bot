from core.node import Node
import sqlite3
from typing import List


class Cache:
    DB_FILE = 'cache.db'
    cursor = None
    conn = None

    def __init__(self):
        self.conn = sqlite3.connect(self.DB_FILE)
        self.cursor = self.conn.cursor()

    def add(self, path: List[str]):
        for i in range(len(path) - 1):
            self.cursor.execute(
                f"INSERT INTO cache VALUES(?, ?)",
                (path[i], path[i+1],)
            )
        self.conn.commit()

    def in_cache(self, title) -> bool:
        self.cursor.execute(
            "SELECT EXISTS (SELECT 1 FROM cache WHERE current = ?)",
            (title,)
        )

        found, = self.cursor.fetchone()
        return bool(found)
