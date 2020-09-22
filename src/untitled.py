import numpy as np



def sample_recommendation(model, user_ids):

    for user_id in user_ids:
        
        scores = model.predict(user_id, np.arange(10000))

        top_items = songs.iloc[np.argsort(-scores)].title

        print("User %s" % user_id)
        print("     Known positives:")
        
        for x in known_positives[:3]:
            print("        %s" % x)
        
        print("     Recommended:")
        
        for x in top_items[:3]:
            print("        %s" % x)
            
            
if __name__ == '__main__':
    model = read_joblib('s3://a-t-first-bucket/song_recommender_data/light_fm_model.joblib')
    sample_recommendation(model, [76353])