<<<<<<< HEAD
import streamlit as st
import pickle
import pandas as pd
import requests

movies_list = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_list)
st.title("Movie Recommender System")
similarity = pickle.load(open('similarity.pkl', 'rb'))




recommended = []
recommended_movies_poster = []
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x:x[1])[1:6]
    for i in movie_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended.append(movies.iloc[i[0]].title)
    return recommended, recommended_movies_poster

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=dc12901cb78c63e2b6b48a88b57f342c&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']


selected_movie_name = st.selectbox(""
"Which movie do you want to watch",
                      movies['title'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
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

    with (col5):
        st.text(names[4])
=======
import streamlit as st
import pickle
import pandas as pd
import requests

movies_list = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_list)
st.title("Movie Recommender System")
similarity = pickle.load(open('similarity.pkl', 'rb'))




recommended = []
recommended_movies_poster = []
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x:x[1])[1:6]
    for i in movie_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended.append(movies.iloc[i[0]].title)
    return recommended, recommended_movies_poster

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=dc12901cb78c63e2b6b48a88b57f342c&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']


selected_movie_name = st.selectbox(""
"Which movie do you want to watch",
                      movies['title'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
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

    with (col5):
        st.text(names[4])
>>>>>>> c16ed34 (Initial commit)
        st.image(posters[4])