# tortoiseORM
CRUD Operations in fastAPI using Tortoise ORM in postgresql.

Why was Tortoise ORM built?¶
Python has many existing and mature ORMs, unfortunately they are designed with an opposing paradigm of how I/O gets processed. asyncio is relatively new technology that has a different concurrency model, and the largest change is regarding how I/O is handled.

However, Tortoise ORM is not first attempt of building asyncio ORM, there are many cases of developers attempting to map synchronous python ORMs to the async world, initial attempts did not have a clean API.

Hence we started Tortoise ORM.

Tortoise ORM is designed to be functional, yet familiar, to ease the migration of developers wishing to switch to asyncio.

It also performs well when compared to other Python ORMs, trading places with Pony ORM:



postgres
Using asyncpg: Typically in the form of postgres://postgres:pass@db.host:5432/somedb

Or specifically asyncpg/psycopg using:

psycopg: psycopg://postgres:pass@db.host:5432/somedb

asyncpg: asyncpg://postgres:pass@db.host:5432/somedb
