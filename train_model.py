import pandas as pd
import nltk
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import joblib

# Download stopwords
nltk.download('stopwords')

# Load dataset
df = pd.read_csv("spam.csv", encoding="latin-1")[["v1", "v2"]]
df.columns = ["label", "message"]

# Convert labels to binary
df["label"] = df["label"].map({"ham": 0, "spam": 1})

# Text preprocessing function
def preprocess(text):
    text = text.lower().translate(str.maketrans("", "", string.punctuation))
    words = [word for word in text.split() if word not in stopwords.words("english")]
    return " ".join(words)

df["message"] = df["message"].apply(preprocess)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(df["message"], df["label"], test_size=0.2, random_state=42)

# Convert text to numerical representation
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train Naïve Bayes classifier
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Save model & vectorizer
joblib.dump(model, "spam_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model trained and saved successfully!")
