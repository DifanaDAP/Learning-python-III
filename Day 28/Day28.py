# Day 28 : Introduction to machine learning with scikit-learn

# Make sure you have scikit-learn installed:
# pip install scikit-learn


from sklearn.datasets import load_iris, load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# === ML Workflow Function ===
def run_ml_pipeline(data_loader, model_type='knn', test_size=0.2, k=3):
    data = data_loader()
    X = data.data
    y = data.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    if model_type == 'knn':
        model = KNeighborsClassifier(n_neighbors=k)
    elif model_type == 'tree':
        model = DecisionTreeClassifier()
    else:
        raise ValueError("Model type must be either 'knn' or 'tree'")

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print(f"Model: {model.__class__.__name__}, Test Size: {test_size}, Accuracy: {accuracy:.2f}")

    cm = confusion_matrix(y_test, predictions)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=data.target_names, yticklabels=data.target_names)
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')
    plt.show()

    return model

# === Run Experiments ===
model1 = run_ml_pipeline(load_iris, model_type='tree')
model2 = run_ml_pipeline(load_iris, model_type='knn', test_size=0.3, k=5)
model3 = run_ml_pipeline(load_iris, model_type='knn', test_size=0.1, k=7)
model4 = run_ml_pipeline(load_wine, model_type='tree')

# === Save model ===
joblib.dump(model4, "wine_model.joblib")

# === Load model ===
loaded_model = joblib.load("wine_model.joblib")
sample = [[13.0, 2.0, 2.36, 20.0, 120.0, 2.8, 3.2, 0.26, 2.28, 5.64, 1.04, 3.92, 1065.0]]
predicted = loaded_model.predict(sample)
print(f"Prediction for sample: {predicted}")