# Spam Email Detector

## 📄 Project Overview
Spam Email Detector is a simple machine learning project that classifies emails as **Spam** or **Not Spam**.  
It features a **Tkinter-based GUI** where users can enter email text and instantly check the result.

The model uses **TF-IDF Vectorization** and is trained with a **Naive Bayes classifier** on a real-world email dataset.

---

## 📂 Project Files
| File | Description |
| :--- | :--- |
| `spam.csv` | Dataset containing labeled emails (spam or ham). |
| `train_model.py` | Script to train the model and save the vectorizer. |
| `spam_model.pkl` | Trained Naive Bayes model (saved after training). |
| `vectorizer.pkl` | Trained TF-IDF vectorizer (saved after training). |
| `spam_gui.py` | GUI application to classify emails using the trained model. |

---

## 🚀 How to Run the Project

### 1. Install Required Libraries
Make sure Python is installed. Then install the required libraries:

```bash
pip install pandas scikit-learn nltk joblib
```

### 2. Train the Model
Before using the GUI, train the model by running:

```bash
python train_model.py
```
This will create two files: `spam_model.pkl` and `vectorizer.pkl`.

### 3. Launch the GUI
Now run the GUI to start detecting spam:

```bash
python spam_gui.py
```

---

## 🛠 How It Works
- The `train_model.py` script:
  - Loads and preprocesses the `spam.csv` dataset (lowercasing, removing stopwords and punctuation).
  - Trains a Naive Bayes classifier using TF-IDF features.
  - Saves the trained model and vectorizer.

- The `spam_gui.py` script:
  - Loads the trained model and vectorizer.
  - Provides a GUI for users to input email text.
  - Displays whether the email is **Spam ❌** or **Not Spam ✅**.

---

## 📸 GUI Preview
- Text input box for writing/pasting the email.
- "Check Spam" button to predict.
- Instant result display.

---

## 📚 Technologies Used
- Python
- Tkinter (GUI)
- Pandas
- Scikit-learn
- NLTK
- Joblib
