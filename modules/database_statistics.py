import sqlite3

from config.settings import DATABASE_PATH


def database_statistics():

    with sqlite3.connect(DATABASE_PATH) as conn:

        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM IPO_MASTER")
        total = cursor.fetchone()[0]

        cursor.execute("""
        SELECT COUNT(*)
        FROM IPO_MASTER
        WHERE exchange LIKE '%SME%'
        """)
        sme = cursor.fetchone()[0]

        mainboard = total - sme

        print("\nDATABASE STATUS")
        print("-" * 30)
        print(f"Total IPOs     : {total}")
        print(f"SME IPOs       : {sme}")
        print(f"Mainboard IPOs : {mainboard}")