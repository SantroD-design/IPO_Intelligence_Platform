import pandas as pd

from modules.data_validator import validate_columns


def load_csv(file_path):

    try:

        df = pd.read_csv(file_path)

        print("\nCSV Loaded Successfully")

        print(f"Total Records : {len(df)}")

        missing = validate_columns(df)

        if len(missing) > 0:

            print("\nMissing Columns")

            for col in missing:

                print("-", col)

            return None

        print("\nAll Required Columns Present")

        return df

    except Exception as e:

        print("\nError")

        print(e)

        return None