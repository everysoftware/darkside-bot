from typing import Mapping, Any

import aiosqlite


class Database:
    file: str

    def __init__(self, file: str) -> None:
        self.file = file

    async def get_product(self, product_id: int) -> Mapping[str, Any] | None:
        async with aiosqlite.connect(self.file) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute(
                    "SELECT * FROM products WHERE product_id=(?)", (product_id,)
            ) as cursor:
                items = await cursor.fetchall()
                if not items:
                    return None
                return items[0]
