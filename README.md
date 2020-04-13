# AirbnbRecommend
*Airbnb Recommender System on Boston data using Sentiment Analysis and Collaborative Filtering*

## Motivation
**Goal**: build a Recommendation System with publically available [Airbnb data from Boston](https://www.kaggle.com/airbnb/boston#listings.csv).
This will mean being able to recommend Airbnb listings to users based on their preferences.

So, how do we do that? We'll attack this problem in three parts:
1. Determine user preferences - **Sentiment Analysis**
* Do the necessary text pre-processing steps for each reviewer's comments (including language detection)
* Using [NLTK's Vader](https://www.nltk.org/howto/sentiment.html) lexicon, calculate the compound polarity of each comment

> for our predicted polarity values, I additionally created this [dashboard app](https://airbnb-bos-polarity.herokuapp.com/) with Streamlit and deployed on Heroku

2. Build a recommendation engine - **Collaborative Filtering**
* Once we have the polarities for each reviewer/listing pair, build a utility matrix with reviewer_id on one axis and listing_id on the other
* Predict all polarities (fill in the Nan values of that matrix) using SVD

3. Generate recommendations!
* We can chose the number of top recommendations we want to give a particular user, sorted according to their predicted polarity


## File descriptions
This repository includes:
* `data` folder, including `reviews.csv` and `listings.csv`. 
* `Airbnb_SentimentAnalysis.ipynb` for part 1
* `Airbnb_CollabFiltering` for parts 2 and 3
