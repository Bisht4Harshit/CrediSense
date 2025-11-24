import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score,precision_score,recall_score,f1_score,roc_auc_score)
from sklearn.metrics import confusion_matrix, classification_report

DATA_PATH = Path("data/processed/german_credit_clean.csv")

def main():
  print("Starting training....")

  df = pd.read_csv(DATA_PATH)
  print("Loaded processed dataset. Shape:",df.shape)

  X = df.drop("Target",axis=1)
  y = df["Target"]

  X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

  model = LogisticRegression(class_weight="balanced",max_iter=1000)

  model.fit(X_train, y_train)

  y_pred = model.predict(X_test)
  y_proba = model.predict_proba(X_test)[:,1]

  acc = accuracy_score(y_test, y_pred)
  prec = precision_score(y_test, y_pred, pos_label=2)
  rec = recall_score(y_test, y_pred, pos_label=2)
  f1 = f1_score(y_test, y_pred, pos_label=2)
  auc = roc_auc_score((y_test == 2).astype(int), y_proba)

  print("Accuracy", acc)
  print("Precision (Bad=2):",prec)
  print("Recall (Bad=2):", rec)
  print("F1-score (Bad=2):",f1)
  print("ROC-AUC:", auc)

 

 


if __name__ == '__main__':
  main()