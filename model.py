import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("movies_dataset.csv")
titles = [i for i in df['title']]

def get_recommendations(title):
    features = ['title', 'director', 'cast', 'listed_in', 'description']
    for feature in features:
        df[feature] = df[feature].fillna('')
    df['new'] = df['title']+' '+df['director']+' '+df['cast']+' '+df['listed_in']+' '+df['description']
    count = CountVectorizer(stop_words='english')
    count_matrix = count.fit_transform(df['new'])
    cosine_sim = cosine_similarity(count_matrix)
    indices = pd.Series(df.index, index=df['title']).drop_duplicates()
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices]