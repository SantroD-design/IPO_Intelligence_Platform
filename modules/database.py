import sqlite3
import os


# Database file location
project_root = os.path.dirname(os.path.dirname(__file__))
db_folder = os.path.join(project_root, "database")
db_path = os.path.join(db_folder, "ipo.db")


def create_database():

    conn = sqlite3.connect(db_path)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS IPO_MASTER(
        ipo_id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_name TEXT NOT NULL,
        symbol TEXT NOT NULL,
        exchange TEXT NOT NULL,
        issue_price REAL,
        listing_price REAL,
        listing_date TEXT,
        sector TEXT
    )
    """)

    conn.commit()

    conn.close()

    print("✅ IPO_MASTER table is ready.")


def add_ipo(company_name,
            symbol,
            exchange,
            issue_price,
            listing_price,
            listing_date,
            sector):

    conn = sqlite3.connect(db_path)

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO IPO_MASTER
    (
        company_name,
        symbol,
        exchange,
        issue_price,
        listing_price,
        listing_date,
        sector
    )
    VALUES
    (?, ?, ?, ?, ?, ?, ?)
    """,
    (
        company_name,
        symbol,
        exchange,
        issue_price,
        listing_price,
        listing_date,
        sector
    ))

    conn.commit()

    conn.close()

    print("✅ IPO Added Successfully!")
def view_all_ipos():

    with sqlite3.connect(db_path) as conn:

        cursor = conn.cursor()

        cursor.execute("""
        SELECT
            ipo_id,
            company_name,
            symbol,
            exchange,
            issue_price,
            listing_price,
            listing_date,
            sector
        FROM IPO_MASTER
        ORDER BY ipo_id;
        """)

        rows = cursor.fetchall()

        if len(rows) == 0:
            print("\nNo IPO records found.")
            return

        print("\n" + "=" * 110)
        print(f"{'ID':<5}{'Company':<30}{'Symbol':<12}{'Exchange':<12}{'Issue':>10}{'Listing':>12}")
        print("=" * 110)

        for row in rows:
            print(
                f"{row[0]:<5}"
                f"{row[1]:<30}"
                f"{row[2]:<12}"
                f"{row[3]:<12}"
                f"{row[4]:>10.2f}"
                f"{row[5]:>12.2f}"
            )

        print("=" * 110)
def search_ipo(search_text):

    with sqlite3.connect(db_path) as conn:

        cursor = conn.cursor()

        cursor.execute("""
        SELECT
            ipo_id,
            company_name,
            symbol,
            exchange,
            issue_price,
            listing_price,
            listing_date,
            sector
        FROM IPO_MASTER
        WHERE
            company_name LIKE ?
            OR symbol LIKE ?
        ORDER BY company_name;
        """,
        (
            f"%{search_text}%",
            f"%{search_text}%"
        ))

        rows = cursor.fetchall()

        return rows
def update_listing_price(ipo_id, new_listing_price):

    with sqlite3.connect(db_path) as conn:

        cursor = conn.cursor()

        cursor.execute("""
        UPDATE IPO_MASTER
        SET listing_price = ?
        WHERE ipo_id = ?
        """,
        (
            new_listing_price,
            ipo_id
        ))

        conn.commit()

        if cursor.rowcount == 0:

            print("\n❌ IPO ID not found.")

        else:

            print("\n✅ Listing Price Updated Successfully.")