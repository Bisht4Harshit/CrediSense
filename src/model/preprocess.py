from pathlib import Path
import pandas as pd
import sys

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
OUT_CSV = PROCESSED_DIR / "german_credit_clean.csv"

COLUMN_NAMES = [
    "Status_existing_checking_account",
    "Duration_months",
    "Credit_history",
    "Purpose",
    "Credit_amount",
    "Savings_account_bonds",
    "Present_employment_since",
    "Installment_rate",
    "Personal_status_and_sex",
    "Debtors_guarantors",
    "Present_residence_since",
    "Property",
    "Age",
    "Other_installment_plans",
    "Housing",
    "Number_existing_credits",
    "Job",
    "Number_people_liable",
    "Telephone",
    "Foreign_worker",
    "Feature_21",
    "Feature_22",
    "Feature_23",
    "Feature_24",
    "Target"
]


def find_raw_file():
    
    main_file = RAW_DIR / "german_credit.csv"
    if main_file.exists():
        return main_file

   
    for f in RAW_DIR.iterdir():
        if f.is_file():
            return f

   
    return None

def main():
    print("Starting preprocess.py")
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    raw_file = find_raw_file()
    if raw_file is None:
        print("ERROR: No raw data file found in data/raw/.")
        print("Please place the UCI german data file into data/raw/ and try again.")
        sys.exit(1)

    print(f"Using raw file: {raw_file}")

    # Read with pandas: variable whitespace separator
    try:
        df = pd.read_csv(raw_file, sep=r'\s+', header=None, engine="python")
    except Exception as e:
        print("Failed to read the raw file. Error:", e)
        sys.exit(1)

    print("Loaded raw data. Shape:", df.shape)

    expected = len(COLUMN_NAMES)
    if df.shape[1] == expected:
       df.columns = COLUMN_NAMES
       print("Assigned all column names.")
    else:
        #if no of col are diff then the list we gave
        n = min(df.shape[1], expected)
        df.columns = COLUMN_NAMES[:n] + [f"col_{i}" for i in range(n, df.shape[1])]
        print(f"Assigned {n} column names; remaining columns named generically.")

    # Removing whitespace from col name
    obj_cols = df.select_dtypes(include=["object"]).columns
    for c in obj_cols:
        df[c] = df[c].astype(str).str.strip()

    # Saving
    try:
        df.to_csv(OUT_CSV, index=False)
        print("Saved cleaned CSV to:", OUT_CSV)
    except Exception as e:
        print("Failed to save cleaned CSV. Error:", e)
        sys.exit(1)

    #verify
    print("Rows:", df.shape[0], "Columns:", df.shape[1])
    print("Preview (first 3 rows):")
    print(df.head(3).to_string(index=False))
    



if __name__ == "__main__":
  main()
