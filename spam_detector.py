
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
emails = [
    "Win money now", "Congratulations you won lottery",
    "Free offer just for you", "Click here to claim prize",
    "Meeting scheduled at 10am", "Please review the report",
    "Let's have lunch tomorrow", "Project deadline is tomorrow"
]
labels = [1,1,1,1,0,0,0,0]  
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(emails)
y = labels
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print("Accuracy:", acc)
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Spam Email Detection - Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()