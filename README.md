# Movie Recommendation System
This project builds a movie recommendation system using the IMDb movie dataset. By leveraging movie summaries, crew names, and genres, the system provides recommendations based on content similarity.

# Table of Contents
1. Project Overview
2. Dataset
3. Data Preprocessing
4. Model Building
5. Technologies Used
6. Deployment

# Project Overview
The objective of this project is to create a recommendation system that suggests similar movies based on user selection. Using features like movie summaries, director names, and the first three main crew members (often actors), a comprehensive “tags” feature is constructed to represent each movie’s key details.

# Dataset
The dataset is sourced from IMDb, containing a variety of movie attributes such as genre, ID, title, overview, and crew details. This data provides a foundation for constructing content-based recommendations.

# Data Preprocessing
The following steps are applied to preprocess and structure the data:
 * Feature Engineering: A new feature, tags, is created by combining the movie’s overview, director, and main cast members.
 * Text Processing: Tokenization, stemming, and removal of stopwords and punctuation are applied to standardize the text.
 * Vectorization: The tags text data is converted into numerical features using CountVectorizer from Scikit-Learn, preparing it for similarity measurement.

# Model Building
To compute movie similarities, the Cosine Similarity function from Scikit-Learn is used:
 * Cosine Similarity measures the angle between vectors representing each movie’s tags, providing a similarity score between 0 and 1.
The final model components, including the vectorizer, similarity matrix, and movie dictionary, are saved for deployment.

# Technologies Used
 * Programming Language: Python
 * Data Manipulation: NumPy, Pandas, Ast (for data parsing)
 * Text Vectorization and Similarity Calculation: Scikit-Learn (CountVectorizer and Cosine Similarity)
 * Deployment: Streamlit
This recommendation system effectively displays movies with high content similarity, providing valuable suggestions to users with reliable accuracy.

# Deployment
A user-friendly interface is developed using Streamlit, allowing users to:
 * Select a movie from the dropdown list.
 * View a list of recommended movies based on content similarity with the selected title.
