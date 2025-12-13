from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# load dataset
iris = load_iris()

X = iris.data      # input features
y = iris.target    # class labels

# split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# create classification model
model = DecisionTreeClassifier()

# train the model (supervised learning happens here)
model.fit(X_train, y_train)

# make predictions
predictions = model.predict(X_test)

# evaluate model
accuracy = accuracy_score(y_test, predictions)
print("accuracy:", accuracy)

# example prediction
# new flower measurements
new_flower = [[5.1, 3.5, 1.4, 0.2]]

prediction = model.predict(new_flower)

print("predicted class:", iris.target_names[prediction[0]])

# how this is supervised learning:
# The model is trained on labeled data (X_train with corresponding y_train labels).
# It learns to map input features to output classes.
# Predictions are made on new, unseen data (X_test and new_flower).

#plot decision tree (optional)
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plot_tree(model, filled=True, feature_names=iris.feature_names, class_names=iris.target_names)
plt.show()

# The decision tree visually represents how the model makes decisions based on input features.
# Each node splits the data based on feature values to classify the iris species.
# This visualization helps understand the learned relationships in the data.
