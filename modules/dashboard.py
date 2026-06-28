from modules.database_statistics import database_statistics
from config.constants import APP_VERSION


def show_dashboard():

    print("\n" + "=" * 60)
    print("        IPO INTELLIGENCE PLATFORM")
    print("=" * 60)

    print(f"Application Version : {APP_VERSION}")

    database_statistics()

    print("=" * 60)