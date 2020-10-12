import numpy as np
from joblib_src import *
from io import BytesIO
import lightfm
from lightfm import LightFM
import pandas as pd
from scipy.sparse import load_npz

def sample_recommendation(model, user_ids, songs, item_features, nums):

    for user_id in user_ids:
        
        scores = model.predict(user_id, np.delete(np.arange(10000),nums), item_features=item_features)

        top_titles = songs.iloc[np.argsort(-scores)].title
        top_artists = songs.iloc[np.argsort(-scores)].artist
        
        print("User %s" % user_id)
        print("Top Recommendations:")
        
        for title, artist in zip(top_titles[:5], top_artists[:5]):
            print("        %s" % title + ", " +artist)
    return zip(top_titles[:5], top_artists[:5])
            
            
if __name__ == '__main__':
    model = read_joblib('s3://a-t-first-bucket/song_recommender_data/light_fm_model.joblib')
    print('Reading Data')
    matrix = load_npz('csr_matrix_small.npz')
    matrix[76353,4] = 10
    matrix[76353, 47] = 10
    model.fit_partial(matrix)
    print('Reading Songs')
    songs = pd.read_csv('data/track_metadata.csv')
    print(songs.iloc[[3,1,2]])
    sample_recommendation(model, [76353], songs)