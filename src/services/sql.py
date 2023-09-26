import sqlite3
from sqlite3.dbapi2 import Cursor

from src.config import Config


class Database:
    def __init__(self, file) -> None:
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()

    def product_exists(self, product_id) -> bool:
        with self.connection:
            return bool(self.cursor.execute("""SELECT 1 FROM products WHERE product_id=(?)
                        """, (product_id,)).fetchall())

    def get_product(self, product_id) -> list:
        with self.connection:
            return self.cursor.execute("""SELECT * FROM products WHERE product_id=(?)
            """, (product_id,)).fetchall()
