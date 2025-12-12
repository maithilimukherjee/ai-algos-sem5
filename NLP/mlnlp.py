import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# --- 1. Prepare Data (A Small, Labeled Dataset) ---
# Our data consists of text reviews (features) and their sentiment (labels: 1 for Positive, 0 for Negative)
data = {
    'text': [
        "This movie was great and I loved the acting!",
        "The food was terrible and the service was awful.",
        "A truly wonderful and moving experience.",
        "I will never watch this disappointing film again.",
        "The best performance of the year, absolutely fantastic.",
        "Do not waste your money, a completely boring plot.",
        "The software is fast, reliable, and easy to use.",
        "It's a buggy mess, full of errors, and very slow."
    ],
    'sentiment': [1, 0, 1, 0, 1, 0, 1, 0]
}
df = pd.DataFrame(data)

# Separate features (X) and labels (y)
X = df['text']
y = df['sentiment']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# The test_size=0.3 means 30% of the data is held back for testing (2 reviews in this small example).

# --- 2. Feature Extraction: Convert Text to Numerical Vectors (CountVectorizer) ---
# CountVectorizer converts a collection of text documents to a matrix of token counts.
# This is a common and simple way to represent text for ML.
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train) # Learn vocabulary and transform training data
X_test_vec = vectorizer.transform(X_test)      # Transform test data using the *learned* vocabulary

# 

# --- 3. Model Training (Naive Bayes Classifier) ---
# Naive Bayes is a simple, fast, and often effective algorithm for text classification.
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# --- 4. Evaluate the Model ---
y_pred = model.predict(X_test_vec)
accuracy = accuracy_score(y_test, y_pred)

print(f"Test Accuracy: {accuracy*100:.2f}%\n")

# --- 5. Predict on New, Unseen Text ---
new_text = ["I had a great time, highly recommended!", "That product is awful."]
new_text_vec = vectorizer.transform(new_text)

# Make predictions (1=Positive, 0=Negative)
new_predictions = model.predict(new_text_vec)

print("--- New Predictions ---")
for text, prediction in zip(new_text, new_predictions):
    sentiment = "Positive" if prediction == 1 else "Negative"
    print(f"Text: '{text}' -> Predicted Sentiment: {sentiment}")