def import_dataframe(df):

    with sqlite3.connect(db_path) as conn:

        cursor = conn.cursor()

        imported = 0

        for _, row in df.iterrows():

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
                row["company_name"],
                row["symbol"],
                row["exchange"],
                row["issue_price"],
                row["listing_price"],
                row["listing_date"],
                row["sector"]
            ))

            imported += 1

        conn.commit()

    print(f"\n✅ Successfully Imported {imported} IPO(s).")