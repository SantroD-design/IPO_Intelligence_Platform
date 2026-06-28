import sqlite3
from datetime import datetime
from config.settings import DATABASE_PATH
from modules.logger import log_info

def get_connection():
    """
    Returns a SQLite database connection.
    """
    return sqlite3.connect(DATABASE_PATH)


def create_database():
    """
    Create IPO_MASTER table if it does not exist.
    """

    with get_connection() as conn:

        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS IPO_MASTER (

            ipo_id INTEGER PRIMARY KEY AUTOINCREMENT,

            company_name TEXT NOT NULL,

            symbol TEXT NOT NULL UNIQUE,

            exchange TEXT,

            ipo_type TEXT,

            issue_price REAL,

            listing_price REAL,

            listing_date TEXT,

            lot_size INTEGER,

            issue_size_cr REAL,

            sector TEXT,

            created_on TEXT,

            updated_on TEXT

        );
        """)

        conn.commit()

    log_info("IPO_MASTER table verified/created.")

    print("✅ IPO_MASTER table is ready.")  

def add_ipo(
    company_name,
    symbol,
    exchange,
    issue_price,
    listing_price,
    listing_date,
    sector,
    ipo_type="SME",
    lot_size=0,
    issue_size_cr=0
):
    """
    Add a new IPO record.
    """

    try:

        with get_connection() as conn:

            cursor = conn.cursor()

            # Check duplicate symbol
            cursor.execute(
                "SELECT ipo_id FROM IPO_MASTER WHERE symbol = ?",
                (symbol,)
            )

            if cursor.fetchone():

                print(f"\n⚠ IPO with symbol '{symbol}' already exists.")
                return

            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            cursor.execute("""
                INSERT INTO IPO_MASTER
                (
                    company_name,
                    symbol,
                    exchange,
                    ipo_type,
                    issue_price,
                    listing_price,
                    listing_date,
                    lot_size,
                    issue_size_cr,
                    sector,
                    created_on,
                    updated_on
                )
                VALUES
                (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                company_name,
                symbol,
                exchange,
                ipo_type,
                issue_price,
                listing_price,
                listing_date,
                lot_size,
                issue_size_cr,
                sector,
                now,
                now
            ))

            conn.commit()

            print("\n✅ IPO Added Successfully!")

    except Exception as e:

        print("\n❌ Error while adding IPO")
        print(e)

def view_all_ipos():
    """
    Display all IPOs.
    """

    try:

        with get_connection() as conn:

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
                ORDER BY company_name
            """)

            rows = cursor.fetchall()

            if not rows:

                print("\nNo IPO records found.")
                return

            print("\n" + "=" * 120)

            print(
                f"{'ID':<5}"
                f"{'Company':<30}"
                f"{'Symbol':<12}"
                f"{'Exchange':<12}"
                f"{'Issue':>12}"
                f"{'Listing':>12}"
                f"{'Gain %':>10}"
            )

            print("=" * 120)

            for row in rows:

                gain = 0

                if row[4] and row[5]:

                    gain = ((row[5] - row[4]) / row[4]) * 100

                print(
                    f"{row[0]:<5}"
                    f"{row[1]:<30}"
                    f"{row[2]:<12}"
                    f"{row[3]:<12}"
                    f"{row[4]:>12.2f}"
                    f"{row[5]:>12.2f}"
                    f"{gain:>9.2f}%"
                )

            print("=" * 120)

            print(f"\nTotal IPOs : {len(rows)}")

    except Exception as e:

        print("\n❌ Error while viewing IPOs")
        print(e)

def search_ipo(search_text):
    """
    Search IPO by company name or symbol.
    """

    try:

        with get_connection() as conn:

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
                ORDER BY company_name
            """,
            (
                f"%{search_text}%",
                f"%{search_text}%"
            ))

            return cursor.fetchall()

    except Exception as e:

        print("\n❌ Error while searching IPO")
        print(e)

        return []

def update_listing_price(ipo_id, new_listing_price):
    """
    Update listing price.
    """

    try:

        with get_connection() as conn:

            cursor = conn.cursor()

            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            cursor.execute("""
                UPDATE IPO_MASTER
                SET
                    listing_price = ?,
                    updated_on = ?
                WHERE ipo_id = ?
            """,
            (
                new_listing_price,
                now,
                ipo_id
            ))

            conn.commit()

            if cursor.rowcount == 0:

                print("\n❌ IPO ID not found.")

            else:

                print("\n✅ Listing Price Updated Successfully.")


        log_info(
            f"Listing price updated for IPO ID {ipo_id} to {new_listing_price}"
        )

    except Exception as e:

        print("\n❌ Error while updating listing price")
        print(e)

def import_dataframe(df):
    """
    Import IPO records from a Pandas DataFrame into IPO_MASTER.

    Duplicate records are skipped based on the IPO symbol.
    """

    try:

        with get_connection() as conn:

            cursor = conn.cursor()
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            imported = 0
            skipped = 0

           
            for _, row in df.iterrows():

                
                cursor.execute(
                    "SELECT COUNT(*) FROM IPO_MASTER WHERE symbol=?",
                    (row["symbol"],)
                )
                exists = cursor.fetchone()[0]
                if exists:
                    skipped += 1
                    continue

             
                cursor.execute("""
                    INSERT INTO IPO_MASTER
                    (
                        company_name,
                        symbol,
                        exchange,
                        ipo_type,
                        issue_price,
                        listing_price,
                        listing_date,
                        lot_size,
                        issue_size_cr,
                        sector,
                        created_on,
                        updated_on
                    )
                    VALUES
                    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    row["company_name"],
                    row["symbol"],
                    row["exchange"],
                    row.get("ipo_type", "SME"),
                    float(row["issue_price"]),
                    float(row["listing_price"]),
                    row["listing_date"],
                    int(row.get("lot_size", 0)),
                    float(row.get("issue_size_cr", 0)),
                    row["sector"],
                    
                ))

                imported += 1

            conn.commit()

            print("\n======================================")
            print("      IMPORT SUMMARY")
            print("======================================")
            print(f"Imported Records : {imported}")
            print(f"Skipped Records  : {skipped}")
            print("======================================")

            log_info(f"Imported Records: {imported}")
            log_info(f"Skipped Records: {skipped}")

    except Exception as e:

        print("\n❌ Error importing IPO data")
        print(e)