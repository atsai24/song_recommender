from flask import Flask, render_template, request
from joblib_src import read_joblib
import pandas as pd
from random import randint
from recommend_songs import sample_recommendation
from scipy.sparse import load_npz

app = Flask(__name__)
songs = pd.read_csv('data/track_metadata.csv')
songs['ID Number'] = songs.index
song_display = songs[['ID Number','title','artist']]
song_display.columns = ['ID Number','Title', 'Artist']
item_features_ = load_npz('final_feature_matrix.npz')


@app.route("/", methods = ['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('template1.html', column_names=song_display.columns.values, row_data=list(song_display.values.tolist()), zip = zip)
    if request.method== 'POST':
        song_1 = request.form['Song 1']

        
        nums = song_1.split(",")
        matrix = load_npz('csr_matrix_small.npz')
        model = read_joblib('s3://a-t-first-bucket/song_recommender_data/light_fm_model.joblib')

        for num in nums:
            matrix[76353, int(num)] = 0.5
        print('fitting...')
        model.fit_partial(matrix, item_features = item_features_, epochs = 1)
        print('predicting...')
        prediction = sample_recommendation(model, [76353], songs, item_features_)
        return render_template('template1.html',
                                     original_input={'Songs':song_1},
                                     result=prediction,
                                     column_names=song_display.columns.values, row_data=list(song_display.values.tolist()), zip = zip
                                     )



if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True)