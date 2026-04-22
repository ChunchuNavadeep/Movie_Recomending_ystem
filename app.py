import os
import pickle
import streamlit as st
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# Safe file loading (IMPORTANT for deployment)
# -----------------------------
BASE_DIR = os.path.dirname(__file__)

movies_path = os.path.join(BASE_DIR,"movie_list.pkl")
movies = pickle.load(open(movies_path, "rb"))

# -----------------------------
# TF-IDF + Similarity (cached for speed)
# -----------------------------
@st.cache_data
def build_vectors(data):
    tfidf = TfidfVectorizer(
        stop_words="english",
        max_features=10000,
        ngram_range=(1, 2)
    )
    vectors = tfidf.fit_transform(data["tags"]).toarray()
    return vectors

vector = build_vectors(movies)

# -----------------------------
# Poster fetch (safe API handling)
# -----------------------------
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY&language=en-US"
        response = requests.get(url)
        data = response.json()

        poster_path = data.get("poster_path")
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
    except:
        pass

    return "https://via.placeholder.com/500x750?text=No+Image"

# -----------------------------
# Recommendation function
# -----------------------------
def recommend(movie):
    if movie not in movies["title"].values:
        return None, None

    index = movies[movies["title"] == movie].index[0]

    similarity = cosine_similarity([vector[index]], vector)[0]

    distances = sorted(
        list(enumerate(similarity)),
        reverse=True,
        key=lambda x: x[1]
    )

    names = []
    posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        names.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id))

    return names, posters

# -----------------------------
# UI
# -----------------------------
st.title("🎬 Movie Recommender System")

movie_list = movies["title"].values
selected_movie = st.selectbox("Select a movie", movie_list)

if st.button("Show Recommendation"):
    names, posters = recommend(selected_movie)

    if names is None:
        st.error("Movie not found!")
    else:
        cols = st.columns(5)

        for i in range(5):
            with cols[i]:
                st.text(names[i])
                st.image(posters[i])
