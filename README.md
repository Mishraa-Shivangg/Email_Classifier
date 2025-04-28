Spam Email Detector
Overview
This project is a Spam Email Detector built using Python and a GUI interface with Tkinter. It utilizes a Naive Bayes classifier trained on a dataset of emails, to classify whether an email is spam or not spam. The model uses a TF-IDF vectorizer to transform the email text into a numerical format, which is then used for classification.
Files in the Project
spam.csv: Contains the dataset of labeled emails (spam/ham).
spam_gui.py: Python script that implements the graphical user interface (GUI) using Tkinter.
spam_model.pkl: The trained Naive Bayes model saved in a pickle file.
train_model.py: Script to train the Naive Bayes model and save it along with the vectorizer.
vectorizer.pkl: The trained vectorizer saved in a pickle file.
Project Setup
Prerequisites
Make sure you have the following Python packages installed:
tkinter: For the graphical user interface (GUI).
joblib: To load and save the model and vectorizer.
nltk: Natural Language Toolkit, used for text preprocessing (like stopword removal).
pandas: For data manipulation and loading the dataset.
scikit-learn: For machine learning, used to create and train the Naive Bayes classifier and TF-IDF vectorizer.
You can install the necessary packages with the following commands:
pip install nltk pandas scikit-learn joblib
Running the Project
Train the Model:
First, train the model using the train_model.py script. This will train the Naive Bayes classifier and save the trained model and vectorizer to spam_model.pkl and vectorizer.pkl, respectively.
python train_model.py
Run the GUI:
After training the model, you can launch the GUI by running the spam_gui.py script.
python spam_gui.py
The GUI will allow you to enter the email text and check whether it's spam or not. The result will be displayed below the input box.
How It Works
Training: The train_model.py script loads the spam.csv dataset, preprocesses the text, and trains a Naive Bayes classifier using the TF-IDF representation of the emails.
Prediction: The spam_gui.py script loads the trained model and vectorizer. The user can input email text, which is then processed and classified by the model as either spam or not spam.
Files Description
spam.csv: Contains the dataset with two columns:
v1: The label (ham/spam).
v2: The email message.
train_model.py:
Preprocesses the text (removes punctuation and stopwords).
Splits the dataset into training and test sets.
Trains the Naive Bayes classifier on the training set.
Saves the trained model and vectorizer for later use.
spam_gui.py:
Provides the graphical user interface to input email text and display the classification result (Spam/Not Spam).
spam_model.pkl:
The trained Naive Bayes model used to predict spam or not spam.
vectorizer.pkl:
The trained TF-IDF vectorizer used to convert text to a numerical representation before prediction.
Example Usage
Run the train_model.py to train the model on the dataset:
python train_model.py
After training, run the spam_gui.py to open the GUI:
python spam_gui.py
Enter an email message in the input box and click "Check Spam". The result will be displayed as either Spam ❌ or Not Spam ✅.
