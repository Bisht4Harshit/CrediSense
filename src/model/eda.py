from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

PLOTS_DIR = Path("reports/plots")
PLOTS_DIR.mkdir(parents=True,exist_ok=True)


Data_Clean = Path("data/processed/german_credit_clean.csv")

def main():
  print("EDA - Loading and basic info")
  if not Data_Clean.exists():
    print("Error: Clean CSV not found at:", Data_Clean)
    return
  

  df = pd.read_csv(Data_Clean)
  print("Loaded clean csv")
  print("Shape",df.shape)
  print("\n--- head (first 5 rows) ---")
  print(df.head().to_string(index=False))
  print("\n--- info ---")
  df.info()
  print("\n--- describe (numeric) ---")
  print(df.describe().transpose())
  print("\n--- Missing values per column ---")
  print(df.isnull().sum())

  print("\n--- Duplicate rows count ---")
  print(df.duplicated().sum())

  print("\n--- Target distribution ---")
  print(df['Target'].value_counts())
  print("\n--- Target distribution (%) ---")
  print(df['Target'].value_counts(normalize=True) * 100)
  print("\n--- Plotting numeric histograms ---")

  numeric_cols = ["Duration_months","Credit_amount"]

  for col in numeric_cols:
    plt.figure()
    df[col].hist(bins=30)
    plt.title(f"Histogram of {col}")
    plt.xlabel(col)
    plt.ylabel("Count")
    plot_path = PLOTS_DIR / f"{col}_hist.png"
    plt.savefig(plot_path)
    plt.close()
    print(f"Saved: {plot_path}")

  print("\n--- Plotting categorical bar charts ---")
  
  top_purpose = df["Purpose"].value_counts().head(10)

  plt.figure()
  top_purpose.plot(kind="bar")
  plt.title("Top 10 Purpose Values")
  plt.xlabel("Purpose Code")
  plt.ylabel("Count")
  plt.tight_layout()
  plt.savefig(PLOTS_DIR / "Purpose_top10.png")
  plt.close()


  cat_cols = [
    "Status_existing_checking_account",
    "Housing",
    "Job",
    "Foreign_worker",
    "Age"
  ]  

  for col in cat_cols:
    plt.figure()
    df[col].value_counts().plot(kind="bar")
    plt.title(f"Value Counts of {col}")
    plt.xlabel(col)
    plt.ylabel("Count")
    plot_path = PLOTS_DIR / f"{col}_bar.png"
    plt.savefig(plot_path)
    plt.close()
    print(f"Saved: {plot_path}")

  print("\n--- Correlation heeatmap ---")

  plt.figure(figsize=(10,8))
  corr = df.corr()
  plt.imshow(corr, cmap="coolwarm",interpolation="nearest")
  plt.colorbar()
  plt.title("Correlation Heatmap")
  plot_path = PLOTS_DIR / "correlation_heatmap.png"
  plt.savefig(plot_path)
  plt.close()
  print(f"Saved: {plot_path}")  



if __name__ == '__main__':
  main()