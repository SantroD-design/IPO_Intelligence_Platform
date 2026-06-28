"""
IPO Master Manager
Professional IPO Data Management Module
"""

import os

from modules.ipo_loader import load_csv
from modules.database import import_dataframe


class IPOMasterManager:

    def __init__(self):

        self.master_file = os.path.join(
            "data",
            "master",
            "ipo_master.csv"
        )

        print("✅ IPO Master Manager Initialized")

    def import_from_csv(self, file_path):

        df = load_csv(file_path)

        if df is None:

            print("❌ CSV Loading Failed")

            return

        import_dataframe(df)

    def update_master_database(self):

        print("\nUpdating IPO Master Database...")

        self.import_from_csv(self.master_file)

        print("✅ Master Database Updated")

    def validate_master_file(self):

        print("\nChecking Master File...")

        if os.path.exists(self.master_file):

            print("✅ Master File Found")

        else:

            print("❌ Master File Missing")

    def show_master_location(self):

        print("\nMaster File Location")

        print(self.master_file)