# 🎬 Movie Recommendation System (Content-Based)

## 📌 Overview

This project is a **Content-Based Movie Recommendation System** built using the TMDB 5000 Movies dataset.
It recommends movies similar to a selected movie based on **genres, keywords, cast, crew, and overview**.

The system uses:

* **Natural Language Processing (NLP)**
* **TF-IDF Vectorization**
* **Cosine Similarity**

---

## 🚀 Features

* Recommend top 5 similar movies
* Uses movie metadata (not ratings)
* Fast similarity computation
* Clean and optimized preprocessing pipeline
* Ready for integration with UI (Streamlit)

---

## 📂 Dataset

* TMDB 5000 Movies Dataset
* Files used:

  * `tmdb_5000_movies.csv`
  * `tmdb_5000_credits.csv`

---

## ⚙️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* Pickle (for model saving)

---

## 🔧 How It Works

### 1. Data Preprocessing

* Merge movies and credits dataset
* Select important columns:

  * title, overview, genres, keywords, cast, crew
* Convert JSON-like columns into lists
* Extract:

  * Top 3 cast members
  * Director from crew

---

### 2. Feature Engineering

* Combine all features into a single column: `tags`
* Remove spaces from names (e.g., "Sam Worthington" → "SamWorthington")
* Convert list → string
* Apply:

  * Lowercasing
  * Regex cleaning
  * Stemming (PorterStemmer)

---

### 3. Vectorization

* Use **TF-IDF Vectorizer**

```python
TfidfVectorizer(
    stop_words='english',
    max_features=10000,
    ngram_range=(1,2)
)
```

---

### 4. Similarity Computation

* Compute cosine similarity between all movies:

```python
cosine_similarity(vector)
```

---

### 5. Recommendation Logic

* Find selected movie index
* Get similarity scores
* Sort movies by similarity
* Return top 5 recommendations

---

## 🧠 Example

Input:

```text
Gandhi
```

Output:

```text
Gandhi, My Father  
The Wind That Shakes the Barley  
A Passage to India  
Guiana 1838  
Ramanujan  
```

---

## 💾 Saving Model

```python
import pickle

pickle.dump(new, open('movie_list.pkl','wb'))
pickle.dump(vector, open('vector.pkl','wb'))
```

---

## ▶️ How to Run

1. Install dependencies:

```bash
pip install pandas numpy scikit-learn nltk
```

2. Run your Python script or notebook

3. Call:

```python
recommend("Movie Name")
```

---

## ⚠️ Limitations

* Does not use user ratings (no personalization)
* TF-IDF does not capture deep semantic meaning
* Recommendations depend on text similarity only

---

## 🚀 Future Improvements

* Add **BERT embeddings** for better accuracy
* Build **Streamlit UI**
* Add **movie posters using TMDB API**
* Add **genre filtering**
* Hybrid system (content + collaborative filtering)

---

## 👨‍💻 Author

Developed as a Machine Learning / NLP project for learning recommendation systems.

---

## ⭐ Conclusion

This project demonstrates how **text-based similarity** can be used to build a recommendation system from scratch and is a strong foundation for more advanced recommender systems.
