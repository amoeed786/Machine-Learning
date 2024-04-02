from sklearn.datasets import load_breast_cancer, load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

cancer_data = load_breast_cancer()
X_cancer = cancer_data.data
y_cancer = cancer_data.target
iris_data = load_iris()
X_iris = iris_data.data
y_iris = iris_data.target

def preprocess(X):
    scaler = StandardScaler()
    return scaler.fit_transform(X)

def train_and_evaluate(X_train, y_train, X_test, y_test, kernel='rbf', C=1.0, gamma='scale', degree=3):
    svm_model = SVC(kernel=kernel, C=C, gamma=gamma, degree=degree)
    svm_model.fit(X_train, y_train)
    y_pred = svm_model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, average='weighted')
    rec = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    return cm, acc, prec, rec, f1

X_train_cancer, X_test_cancer, y_train_cancer, y_test_cancer = train_test_split(X_cancer, y_cancer, test_size=0.2, random_state=42)
X_train_iris, X_test_iris, y_train_iris, y_test_iris = train_test_split(X_iris, y_iris, test_size=0.2, random_state=42)
X_train_cancer = preprocess(X_train_cancer)
X_test_cancer = preprocess(X_test_cancer)
X_train_iris = preprocess(X_train_iris)
X_test_iris = preprocess(X_test_iris)

kernels = ['linear','rbf']
parameters = [
    {'C': 1},
    {'C': 1, 'degree': 3},
    {'C': 1, 'gamma': 'scale'}
]
results = {}

results['Breast Cancer'] = {}

for kernel, parameter in zip(kernels, parameters):
    cm, acc, prec, rec, f1 = train_and_evaluate(X_train_cancer, y_train_cancer, X_test_cancer, y_test_cancer, kernel=kernel, **parameter)
    results['Breast Cancer'][kernel] = {'Confusion Matrix': cm, 'Accuracy': acc, 'Precision': prec, 'Recall': rec, 'F1-score': f1}
results['Iris'] = {}

for kernel, parameter in zip(kernels, parameters):
    cm, acc, prec, rec, f1 = train_and_evaluate(X_train_iris, y_train_iris, X_test_iris, y_test_iris, kernel=kernel, **parameter)
    results['Iris'][kernel] = {'Confusion Matrix': cm, 'Accuracy': acc, 'Precision': prec, 'Recall': rec, 'F1-score': f1}

for dataset in results:
    print(f"Results for {dataset} dataset:")
    for kernel in results[dataset]:
        print(f"Kernel: {kernel}")
        print("Confusion Matrix:")
        print(results[dataset][kernel]['Confusion Matrix'])
        print("Accuracy:", results[dataset][kernel]['Accuracy'])
        print("Precision:", results[dataset][kernel]['Precision'])
        print("Recall:", results[dataset][kernel]['Recall'])
        print("F1-score:", results[dataset][kernel]['F1-score'])
        print("\n")
