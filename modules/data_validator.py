import pandas as pd


REQUIRED_COLUMNS = [

    "company_name",
    "symbol",
    "exchange",
    "ipo_type",
    "issue_price",
    "listing_price",
    "listing_date",
    "lot_size",
    "issue_size_cr",
    "sector"

]


def validate_columns(df):

    missing = []

    for column in REQUIRED_COLUMNS:

        if column not in df.columns:
            missing.append(column)

    return missing