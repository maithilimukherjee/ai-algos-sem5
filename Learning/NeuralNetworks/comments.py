from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# training data (comments + sentiment labels)
comments = [
    "i love this movie",
    "this is amazing",
    "absolutely fantastic experience",
    "i hate this",
    "worst movie ever",
    "very bad and boring",
    "i enjoyed the film",
    "terrible acting",
    "great storyline",
    "not good at all"
]

# labels: 1 = positive, 0 = negative
labels = [1,1,1,0,0,0,1,0,1,0]

# convert text into numeric features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(comments)

y = labels

# split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# neural network model
model = MLPClassifier(
    hidden_layer_sizes=(5,),   # one hidden layer with 5 neurons
    activation='relu',
    max_iter=1000,
    random_state=42
)

# training (learning happens here)
model.fit(X_train, y_train)

# predictions
predictions = model.predict(X_test)

# accuracy
print("accuracy:", accuracy_score(y_test, predictions))

# new comment prediction
new_comment = ["the movie was really good"]

new_X = vectorizer.transform(new_comment)
sentiment = model.predict(new_X)

if sentiment[0] == 1:
    print("sentiment: positive")
else:
    print("sentiment: negative")

# inputs (x): word counts from comments
# outputs (y): sentiment labels (positive / negative)
# the neural network:
# - computes weighted sums
# - applies activation function
# - calculates error
# - updates weights using backpropagation
# learning is inductive and supervised
