# 📚 Kindle Book Review Sentiment Analysis

A machine learning project that classifies Amazon Kindle book reviews as **Positive** or **Negative** using Natural Language Processing (NLP) techniques and Logistic Regression.

---

## 📌 Project Overview

This project performs binary sentiment analysis on Kindle book reviews. Each review is labeled based on its star rating — reviews with a rating below 3 are classified as **Negative (0)**, and reviews with a rating of 3 or above are classified as **Positive (1)**. The goal is to automatically predict the sentiment of a review using text-based machine learning.

---

## 📂 Dataset

- **File:** `all_kindle_review.csv`
- **Columns Used:** `reviewText`, `rating`
- The dataset contains customer reviews from Amazon's Kindle store, with star ratings ranging from 1 to 5.

---

## 🔧 Tech Stack

| Category | Tools / Libraries |
|---|---|
| Language | Python |
| Data Handling | Pandas, NumPy |
| NLP | NLTK (Stopwords, WordNetLemmatizer), BeautifulSoup |
| Feature Extraction | Scikit-learn (TF-IDF Vectorizer) |
| ML Model | Scikit-learn (Logistic Regression) |
| Evaluation | Accuracy Score, Classification Report, Confusion Matrix |
| Environment | Jupyter Notebook / Google Colab |

---

## 🔄 Project Workflow

### 1. Data Loading & Exploration
- Loaded the dataset using Pandas
- Selected relevant columns: `reviewText` and `rating`
- Checked for missing values and explored rating distribution

### 2. Data Preprocessing
- **Label Encoding:** Converted ratings to binary labels
  - Rating < 3 → **0 (Negative)**
  - Rating ≥ 3 → **1 (Positive)**

### 3. Text Cleaning Pipeline
Applied the following cleaning steps to the `reviewText` column:
- Converted all text to **lowercase**
- Removed **special characters** using Regex
- Removed **English stopwords** using NLTK
- Removed **URLs** using Regex
- Removed **HTML tags** using BeautifulSoup
- **Lemmatization** using NLTK's `WordNetLemmatizer` to reduce words to their base form

### 4. Feature Extraction
- Applied **TF-IDF Vectorization** with `max_features=5000`
- Fit on training data and transformed both train and test sets

### 5. Model Training
- Split data: **80% Train / 20% Test** (random_state=42)
- Trained a **Logistic Regression** model (`solver='liblinear'`, `C=1.0`)

### 6. Model Evaluation
Evaluated the model using:
- **Accuracy Score**
- **Classification Report** (Precision, Recall, F1-Score)
- **Confusion Matrix**

---

## 📁 Project Structure

```
kindle_book_review_sentiment_analysis/
│
├── kindle_book_review_sentimental_analysis.ipynb   # Main Jupyter Notebook
├── all_kindle_review.csv                           # Dataset (not included in repo)
└── README.md                                       # Project documentation
```

---

## ▶️ How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/kindle-sentiment-analysis.git
   cd kindle-sentiment-analysis
   ```

2. Install required libraries:
   ```bash
   pip install pandas numpy scikit-learn nltk beautifulsoup4 lxml
   ```

3. Download NLTK resources (run once in Python):
   ```python
   import nltk
   nltk.download('stopwords')
   nltk.download('wordnet')
   ```

4. Add the dataset `all_kindle_review.csv` to the project folder.

5. Open and run the notebook:
   ```bash
   jupyter notebook kindle_book_review_sentimental_analysis.ipynb
   ```

---

## 📊 Results

The Logistic Regression model was evaluated on the test set. Results include accuracy, precision, recall, and F1-score for both Positive and Negative classes as shown in the notebook output.

---

## 🙋 Author

**Rushi**
B.E. – Artificial Intelligence & Data Science
MET's Institute of Engineering, Nashik