from modules.database import create_database
from modules.database import add_ipo
from modules.database import view_all_ipos
from modules.database import search_ipo
from modules.database import update_listing_price

from modules.menu import display_menu


create_database()

while True:

    choice = display_menu()

    if choice == "1":

        print("\nAdd New IPO")

        company_name = input("Company Name : ")
        symbol = input("Symbol : ")
        exchange = input("Exchange : ")

        issue_price = float(input("Issue Price : "))
        listing_price = float(input("Listing Price : "))

        listing_date = input("Listing Date (YYYY-MM-DD): ")

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

    elif choice == "2":

        view_all_ipos()

    elif choice == "3":

    search_text = input("\nEnter Company Name or Symbol : ")

    results = search_ipo(search_text)

    if len(results) == 0:

        print("\nNo IPO Found.")

    else:

        print("\n" + "=" * 110)

        for row in results:

            listing_gain = ((row[5]-row[4])/row[4])*100

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

            print("-"*110)

    elif choice == "4":

        print("\nThank you for using IPO Intelligence Platform.")

        break

    else:

        print("\nInvalid Choice.")

    input("\nPress Enter to continue...")