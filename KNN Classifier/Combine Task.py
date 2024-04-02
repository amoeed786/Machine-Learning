from sklearn.datasets import load_digits, load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import pandas as pd

digit = load_digits()
X_digit, y_digit = digit.data, digit.target
wine = load_wine()
X_wine, y_wine = wine.data, wine.target
X_train_digit, X_test_digit, y_train_digit, y_test_digit = train_test_split(X_digit, y_digit, test_size=0.2, random_state=42)
X_train_wine, X_test_wine, y_train_wine, y_test_wine = train_test_split(X_wine, y_wine, test_size=0.2, random_state=42)

def evaluate_knn(X_train, X_test, y_train, y_test, k_values, weights):
    results = []
    for k in k_values:
        for weight in weights:
            knn = KNeighborsClassifier(n_neighbors=k, weights=weight)
            knn.fit(X_train, y_train)
            y_pred = knn.predict(X_test)
            acc = accuracy_score(y_test, y_pred)
            prec = precision_score(y_test, y_pred, average='macro')
            rec = recall_score(y_test, y_pred, average='macro')
            f1 = f1_score(y_test, y_pred, average='macro')
            results.append({'K': k, 'Weight': weight, 'Accuracy': acc, 'Precision': prec, 'Recall': rec, 'F1': f1})
    return results

k_values = [3, 5, 7]
weights = ['uniform', 'distance']
results_digit = evaluate_knn(X_train_digit, X_test_digit, y_train_digit, y_test_digit, k_values, weights)
results_wine = evaluate_knn(X_train_wine, X_test_wine, y_train_wine, y_test_wine, k_values, weights)
results_digit_df = pd.DataFrame(results_digit)
results_wine_df = pd.DataFrame(results_wine)
print("Results for digit dataset:")
print(results_digit_df)
print("\nResults for Wine dataset:")
print(results_wine_df)
