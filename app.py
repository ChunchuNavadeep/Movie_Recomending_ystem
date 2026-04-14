import streamlit as st
import pickle
import pandas as pd

@st.cache_data
def load_data():
    df = pickle.load(open("movies.pkl", 'rb'))
    similar = pickle.load(open("similar.pkl", 'rb'))
    return df, similar

df, similar = load_data()

def recommend(title):
    if title not in df["title"].values:
        return "Movie not found"

    ind = df.index[df["title"] == title][0]
    scores = similar[ind]

    top_idx = [i for i in scores.argsort()[::-1][1:] if scores[i] > 0.15][:10]
    result = df.iloc[top_idx][["title","rating"]].copy()
    # result["similarity_score"] = similar[ind][top_idx].round(3)

    return result

# UI
st.title("🎬 Movie Recommendation System")

option = st.selectbox("Select a Movie", df["title"].values)

if st.button("Recommend"):
    result = recommend(option)

    if isinstance(result, str):
        st.error(result)
    else:
        st.write("### Top Recommendations:")
        for i, row in result.iterrows():
            st.write(f"🎬 {row['title']}  ⭐ {row['rating']}")