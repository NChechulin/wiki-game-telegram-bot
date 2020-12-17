"""
Cache class for operations with DB
"""


from core.node import Node
import sqlite3
from typing import List


class Cache:
    """
    Cache class for operations with DB
    """

    DB_FILE = "cache.db"
    cursor = None
    conn = None

    def __init__(self: "Cache") -> None:
        self.conn = sqlite3.connect(self.DB_FILE)
        self.cursor = self.conn.cursor()

    def add(self: "Cache", path: List[str]) -> None:
        """
        Adds a bunch of (current, next) pairs in DB
        """
        for i in range(len(path) - 1):
            self.cursor.execute(
                f"INSERT INTO cache VALUES(?, ?)",
                (
                    path[i],
                    path[i + 1],
                ),
            )
        self.conn.commit()

    def in_cache(self: "Cache", title: str) -> bool:
        """
        Checks if a record is in DB
        """
        self.cursor.execute(
            "SELECT EXISTS (SELECT 1 FROM cache WHERE current = ?)", (title,)
        )

        (found,) = self.cursor.fetchone()
        return bool(found)

    def __get_next(self: "Cache", current: str) -> str:
        """
        Returns next step of path from DB
        """
        self.cursor.execute("SELECT next FROM cache WHERE current = ?", (current,))
        res = self.cursor.fetchone()
        return res[0]

    def get(self: "Cache", title: str) -> List[str]:
        """
        Returns full cached path as list of titles
        """
        ans = []
        cur, nxt = title, self.__get_next(title)
        while nxt != "Adolf Hitler":
            cur, nxt = nxt, self.__get_next(nxt)
            ans.append(cur)
        ans.append("Adolf Hitler")
        return ans
