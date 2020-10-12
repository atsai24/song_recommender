# Your New Favorite Song: A Song Recommender Application

<div class='header'> 
<!-- Your header image here -->

## Sections:
 **[Introduction](#Introduction)**  |
 **[Data](#data)**  |
 **[Modeling](#exploration)**  |
 **[Model](#model)**  |
 **[Takeaways](#takeaways)**  |
 
 ---
 ## Introduction
This recommender application is built on Flask and applies the LightFM algorithm on the Million Song Dataset to rank recommended songs for a user based on the their inputs of their favorite songs. I used AWS S3 Buckets to host large datasets, and an EC2 instance to perform compuatationally heavy data transformations and model fitting.

<sub>[  **[Back to Sections](#sections)** ]</sub>

 ## Data
The data was taken from the [Million Song Dataset](http://millionsongdataset.com/), a dataset put together by Spotify and [LabROSA](https://labrosa.ee.columbia.edu/).
The dataset contains: 

 - Track Metadata: Information on each track including genre (target variable), listen count, composer, creation date.
 
 - User Data: User-Song Interactions, with listen counts for each unique user ID and song ID
 
 - Song Tags: A list of tags associated with each song collected by Last.fm. Tags are keywords or phrases used to describe the song
 

<img src="https://github.com/atsai24/song_recommender/blob/master/img/user_item_metadata_image.png" width = "800" height = "400">
 
 <sub>[  **[Back to Sections](#sections)** ]</sub>
 

## Modeling

<img src="https://github.com/atsai24/song_recommender/blob/master/img/light_fm_logo.png" width = "700" height = "350">

Used LightFM's implicit model to apply both content based and collaborative filtering methods.
  - Content Based Filtering: Applies user's previous preferences to recommend new items similar to those preferences
  
  - Collaborative Filtering: Compares user's taste to other users and recommends items based on the preferences of other similar users
### Item Features

LightFM has an item features parameter to help categorize and compare items. In this case we input song tags as item features.

Most Popular Tags: 

<img src="https://github.com/atsai24/song_recommender/blob/master/img/tag_counts.png" width = "200" height = 350>

Each song has a list of tags associated with it that describe the song. Songs with many overlapping tags are determined to be more similar.

Tag Similarities:

<img src="https://github.com/atsai24/song_recommender/blob/master/img/tag_similarities.png">



<sub>[  **[Back to Sections](#sections)** ]</sub>

### Evaluation

The ROC AUC Score is the probability that a randomly chosen positive item (song a user has listened to) is rated higher than a randomly sampled negative item (song a user has not listened to).

<img src="https://github.com/atsai24/song_recommender/blob/master/img/AUC_example.png">

Final Model AUC Score: 0.92

## Application

The application runs locally and is built on Flask. Code can be found in the src folder.

<p> User is shown the database of songs and may input the song id's for any amount songs that they like.

<img src="https://github.com/atsai24/song_recommender/blob/master/img/flask_app_empty.png">
</p>

<p> The inputs are sent to the trained LightFM model. Since LightFM does not allow for new users, I created a dummy user during the initial model trainging with 0 interactions. The user inputs fill in the preferences for the dummy user and the model is partially refit. The model then predicts the rankings of each song for that user. The application prints the top 5 ranked songs.
</p>
<img src="https://github.com/atsai24/song_recommender/blob/master/img/flask_app_comma_separated.png" width = "600" height = "500"> 


## Technologies

  - Python
  - SQL
  - AWS (EC2, S3)
  - Flask


<sub>[  **[Back to Sections](#sections)** ]</sub>
