def display_menu():

    print("\n" + "=" * 60)
    print("        IPO INTELLIGENCE PLATFORM v1.0")
    print("=" * 60)

    print("\nDATABASE MANAGEMENT")
    print("-" * 30)
    print("1. Add New IPO")
    print("2. View All IPOs")
    print("3. Search IPO")
    print("4. Update Listing Price")

    print("\nDATA IMPORT")
    print("-" * 30)
    print("5. Import Master IPO CSV")
    print("6. Import SME IPO Data")
    print("7. Update Current Market Prices")

    print("\nRESEARCH")
    print("-" * 30)
    print("8. Anchor Investor Analysis")
    print("9. IPO Performance Dashboard")
    print("10. Export to Excel")

    print("\nSYSTEM")
    print("-" * 30)
    print("11. Settings")
    print("12. Database Backup")
    print("13. Exit")

    print("=" * 60)

    return input("Enter your choice : ")