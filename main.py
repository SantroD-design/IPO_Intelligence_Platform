from modules.database import (
    create_database,
    add_ipo,
    view_all_ipos,
    search_ipo,
    update_listing_price,
    import_dataframe
)

from modules.ipo_loader import load_csv
from modules.menu import display_menu
from modules.dashboard import show_dashboard

def main():

    # Create database if it does not exist
    create_database()
    show_dashboard()
    print("\n==============================================")
    print("      IPO INTELLIGENCE PLATFORM")
    print("==============================================")

    while True:

        choice = display_menu()

        # -------------------------------
        # Add New IPO
        # -------------------------------
        if choice == "1":

            print("\nAdd New IPO")

            company_name = input("Company Name : ")
            symbol = input("Symbol : ")
            exchange = input("Exchange : ")

            issue_price = float(input("Issue Price : "))
            listing_price = float(input("Listing Price : "))

            listing_date = input("Listing Date (YYYY-MM-DD) : ")
            sector = input("Sector : ")

            add_ipo(
                company_name,
                symbol,
                exchange,
                issue_price,
                listing_price,
                listing_date,
                sector
            )

        # -------------------------------
        # View All IPOs
        # -------------------------------
        elif choice == "2":

            view_all_ipos()

        # -------------------------------
        # Search IPO
        # -------------------------------
        elif choice == "3":

            search_text = input("\nEnter Company Name or Symbol : ")

            results = search_ipo(search_text)

            if len(results) == 0:

                print("\nNo IPO Found.")

            else:

                print("\n" + "=" * 110)

                for row in results:

                    listing_gain = ((row[5] - row[4]) / row[4]) * 100

                    print(f"""
ID            : {row[0]}
Company       : {row[1]}
Symbol        : {row[2]}
Exchange      : {row[3]}
Issue Price   : {row[4]:.2f}
Listing Price : {row[5]:.2f}
Listing Gain  : {listing_gain:.2f} %
Listing Date  : {row[6]}
Sector        : {row[7]}
""")

                    print("-" * 110)

        # -------------------------------
        # Update Listing Price
        # -------------------------------
        elif choice == "4":

            try:

                ipo_id = int(input("\nEnter IPO ID : "))
                new_listing_price = float(input("Enter New Listing Price : "))

                update_listing_price(
                    ipo_id,
                    new_listing_price
                )

            except ValueError:

                print("\n❌ Invalid Input.")

        # -------------------------------
        # Import IPO CSV
        # -------------------------------
        elif choice == "5":

            df = load_csv("data/raw/ipo_master_sample.csv")

            if df is not None:

                import_dataframe(df)

        # -------------------------------
        # Exit
        # -------------------------------
        elif choice == "6":

            print("\nThank you for using IPO Intelligence Platform.")
            break

        # -------------------------------
        # Invalid Choice
        # -------------------------------
        else:

            print("\nInvalid Choice.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()