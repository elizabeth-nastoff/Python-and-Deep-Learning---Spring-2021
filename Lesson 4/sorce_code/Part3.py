import pandas as pd
from sklearn.svm import SVC, LinearSVC
from sklearn.model_selection import train_test_split

from sklearn import metrics
from sklearn.metrics import classification_report

data = pd.read_csv("glass.csv")

y = data.Type
X = data.drop('Type', axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearSVC()
model.fit(X, y)

y_pred = model.predict(X_test)

print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("Classification Report: ", classification_report(y_test, y_pred))