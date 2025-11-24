from pathlib import Path
import pandas as pd
import joblib 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, classification_report)
from sklearn.metrics import precision_recall_curve

DATA_PATH = Path("data/processed/german_credit_clean.csv")
MODEL_DIR = Path("models")
MODEL_DIR.mkdir(parents=True, exist_ok=True)
MODEL_OUT = MODEL_DIR / "rf_model.pkl"

RF_PARAMS = {"n_estimators":200, "max_depth":5, "min_samples_leaf":2, "class_weight":"balanced","random_state":42, "n_jobs":-1}

def load_data(path=DATA_PATH):
  if not path.exists():
    raise FileNotFoundError(f"  Cleaned CSV not found:{path}")
  df = pd.read_csv(path)
  return df

def main():
  print("Random Forest - start")
  df = load_data()
  print("Loaded shape:", df.shape)
  print(df.head(3).to_string(index=False))

  X = df.drop("Target", axis=1)
  y = df["Target"]

  X_train, X_test, y_train , y_test = train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

  print("Train shape:",X_train.shape,"Test shape:", X_test.shape)

  rf = RandomForestClassifier(**RF_PARAMS)
  print("Fitting Random Forest...")
  rf.fit(X_train, y_train)
  print("Model fitted")
  



  y_pred = rf.predict(X_test)

  y_test_bad = (y_test==2).astype(int)

  print("RF classes:", rf.classes_)
  y_proba_bad = rf.predict_proba(X_test)[:, list(rf.classes_).index(2)]

  y_true_bad = (y_test == 2).astype(int)
  
  precision_vals, recall_vals, thresholds = precision_recall_curve(y_true_bad, y_proba_bad)

 

   
  print("\nConfusion Matrix (rows=true, cols=pred):")
  print(confusion_matrix(y_test, y_pred))
  print("\n Classification Report:")
  print(classification_report(y_test, y_pred, digits=4)) 

  importances = rf.feature_importances_
  feat_names = X.columns.to_list()
  fi = sorted(zip(feat_names, importances), key=lambda x: x[1], reverse=True)
  print("\nTop 10 feature importances:")
  for name, val in fi[:10]:
    print(f"{name:30s}{val:.4f}")

  joblib.dump(rf, MODEL_OUT)
  print(f"\nSaved Random Foreest to: {MODEL_OUT}")  
if __name__ == '__main__':
  main()