import streamlit as st
import pickle
import pandas as pd
import requests



def fetch_movie_id(movie_id):

    response = requests.get('https://api.themoviedb.org/3/movie/{}?'
                            'api_key=092bd4b75fc851c1f169882d812986fa&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for s in movie_list:
        movie_id = movies.iloc[s[0]].movie_id
        recommended_movies.append(movies.iloc[s[0]].title)
        recommended_movies_poster.append(fetch_movie_id(movie_id))
    return recommended_movies, recommended_movies_poster


movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')
Selected_movie_Name = st.selectbox('How would be like to contact?', movies['title'].values)


if st.button('Recommend'):
    names, posters = recommend(Selected_movie_Name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
