# Import necessary libraries
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

def train_model():
    
    iris = load_iris()
    X, y = iris.data, iris.target

   
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

   
    svm_clf = SVC(kernel='linear', C=1.0)
    svm_clf.fit(X_train, y_train)

    
    y_pred = svm_clf.predict(X_test)


    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

 
    print(classification_report(y_test, y_pred))

    
    model_dir = 'model'
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    # Save the trained model
    joblib.dump(svm_clf, os.path.join(model_dir, 'model.pkl'))

if __name__ == "__main__":
    train_model()
