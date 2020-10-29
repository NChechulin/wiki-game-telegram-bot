from core.node import Node
import sqlite3


class Cache:
    DB_FILE = '../cache.db'
    cursor = None

    def __init__(self):
        connection = sqlite3.connect(self.DB_FILE)
        self.cursor = connection.cursor()
