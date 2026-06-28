from modules.ipo_loader import load_csv

df = load_csv("data/raw/ipo_master_sample.csv")

if df is not None:

    print("\nFirst Five Records\n")

    print(df.head())