import streamlit as st
import pandas as pd
import pickle 
import requests
import json
import dotenv
import os
movies = pickle.load(open("movies.pkl", mode="rb"))
similarity = pickle.load(open("similarity.pkl", mode="rb"))
dotenv.load_dotenv()
def getResponse(id):
    req = requests.get(f"https://api.themoviedb.org/3/movie/{id}", params={"api_key": {os.getenv("API_KEY")}} ).content
    return json.loads(req.decode('utf-8'))

def recommended_movies(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = similarity[index]
        movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
        print(f"Recommendations for '{movies.iloc[index].title}':")
        recommended = []
        for i in movie_list:
            recommended.append(movies.iloc[i[0]])
        return recommended
    except IndexError:
        return []
def main():

    st.title("Movie Reccomendation System")
    value = st.selectbox("Select a movie", movies['title'].values)
    if st.button("Find Reccomended"):
        with st.spinner('Fetching movies from the multiverse...'):
            movie = recommended_movies(value)

            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                data = getResponse(movie[0].id)
                st.image("https://image.tmdb.org/t/p/w500/"+data["poster_path"])
                st.caption(data['title'])
                pass
            with col2:
                data = getResponse(movie[1].id)
                st.image("https://image.tmdb.org/t/p/w500/"+data["poster_path"])
                st.caption(data['title'])
            with col3:
                data = getResponse(movie[2].id)
                st.image("https://image.tmdb.org/t/p/w500/"+data["poster_path"])
                st.caption(data['title'])
            with col4:
                data = getResponse(movie[3].id)
                st.image("https://image.tmdb.org/t/p/w500/"+data["poster_path"])
                st.caption(data['title'])
            with col5:
                data = getResponse(movie[4].id)
                st.image("https://image.tmdb.org/t/p/w500/"+data["poster_path"])
                st.caption(data['title'])

if __name__ == "__main__":
    main()
