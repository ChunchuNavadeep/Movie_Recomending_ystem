# 🎬 Movie Recommendation System (Deployed)

## 🌐 Live Demo

👉 https://movielover.streamlit.app

---

## 📌 Overview

This is a **Content-Based Movie Recommendation System** that suggests similar movies based on:

* Genres
* Keywords
* Cast
* Director
* Movie overview

It uses **Natural Language Processing (NLP)** and **cosine similarity** to recommend movies.

---

## 🚀 Features

* 🎯 Recommend top 5 similar movies
* 🧠 Uses TF-IDF + NLP
* 🖼️ Fetches movie posters using TMDB API
* ⚡ Fast performance using caching
* 🌐 Fully deployed using Streamlit

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn (TF-IDF, Cosine Similarity)
* NLTK (text preprocessing)
* Streamlit (UI & deployment)
* TMDB API (posters)

---

## ⚙️ How It Works

### 1. Data Processing

* Merged datasets:

  * `tmdb_5000_movies.csv`
  * `tmdb_5000_credits.csv`
* Extracted:

  * Genres
  * Keywords
  * Top 3 cast members
  * Director

---

### 2. Feature Engineering

* Combined all features into one column → `tags`
* Removed spaces in names

  * Example: `Sam Worthington → SamWorthington`
* Applied:

  * Lowercasing
  * Regex cleaning
  * Stemming

---

### 3. Vectorization

```python
TfidfVectorizer(
    stop_words="english",
    max_features=10000,
    ngram_range=(1,2)
)
```

---

### 4. Similarity Calculation

* Used **cosine similarity** to find similar movies

---

### 5. Recommendation

* Select a movie
* System finds most similar movies
* Displays:

  * Movie titles
  * Posters

---

## 🖥️ UI (Streamlit)

* Dropdown to select movie
* Button to trigger recommendation
* Displays results in 5 columns

---

## 💾 Model Storage

```python
pickle.dump(movie_list, open("movie_list.pkl", "wb"))
pickle.dump(vector, open("vector.pkl", "wb"))
```

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## ⚠️ Limitations

* No user personalization (no collaborative filtering)
* TF-IDF does not understand deep meaning
* Recommendations depend on text similarity only

---

## 🚀 Future Improvements

* 🔥 Add BERT embeddings (better accuracy)
* 🎯 Add "Why recommended" explanation
* 🔍 Add search autocomplete
* 🎚️ Add filters (genre, rating, year)
* ❤️ Add user-based recommendations

---

## 👨‍💻 Author

Built as an ML/NLP project to demonstrate recommendation systems and deployment.

---

## ⭐ Project Highlight

This project demonstrates:

* End-to-end ML pipeline
* NLP preprocessing
* Real-world deployment
* API integration

---

