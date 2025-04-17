# Day 29 : Build a simple end-to-end ml model

# make sure the necessary libraries are installed:
# pip install scikit-learn matplotlib seaborn pandas joblib


from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import joblib

# 1. Load dataset
cancer = load_breast_cancer()
X = pd.DataFrame(cancer.data, columns=cancer.feature_names)
y = pd.Series(cancer.target)

# 2. Explore dataset
print("First 5 rows of the dataset:")
print(X.head())
print("\nClass distribution:")
print(y.value_counts())

# 3. Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Predict and Evaluate
y_pred = model.predict(X_test)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', xticklabels=cancer.target_names, yticklabels=cancer.target_names)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

# 6. Save model
joblib.dump(model, "breast_cancer_model.joblib")

# 7. Load model and predict new data
loaded_model = joblib.load("breast_cancer_model.joblib")
sample = [X.iloc[0].values]  # Using the first sample
sample_prediction = loaded_model.predict(sample)
print(f"\nPrediction for sample: {cancer.target_names[sample_prediction][0]}")
