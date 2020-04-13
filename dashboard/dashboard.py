import streamlit as st
import pandas as pd

st.title("Exploratory Dashboard of Average Comment Polarity estimates for unique listings")

@st.cache
def load_data():
    data =  pd.read_csv('dashboard_df.csv')
    return data

def main():
    data = load_data()

    if st.checkbox('Show Data'):
        data

    size_cols = ['price', 'security_deposit', 'cleaning_fee', 'guests_included', 'extra_people',
                'minimum_nights', 'maximum_nights']
    color_cols = ['review_scores_rating', 'review_scores_accuracy', 'review_scores_cleanliness', 
                 'review_scores_checkin', 'review_scores_communication', 'review_scores_location', 
                 'review_scores_value']
    size = st.sidebar.selectbox("Select Size Metric", size_cols)
    color = st.sidebar.selectbox("Select Color Metric", color_cols)

    neighbourhood = st.sidebar.multiselect("Neighbourhood", data['neighbourhood_cleansed'].unique())

    if neighbourhood:
        data = data[data.neighbourhood_cleansed.isin(neighbourhood)]

    super_host = st.sidebar.multiselect("Is host a superhost", data['host_is_superhost'].unique())
    if super_host:
        data = data[data.host_is_superhost.isin(super_host)]

    st.vega_lite_chart(data,{
        'width':'container',
        'height':400,
        'mark':'circle',
        'encoding':{
            'x':{
                'field':'polarity',
                'type':'quantitative',
                'axis': {'title': 'Polarity'}
            },
            'y':{
                'field':'number_of_reviews',
                'type':'quantitative',
                'axis': {'title': 'Number of Reviews'}
            },
            'size':{
                'field': size,
                'type':'quantitative'
            },
            'color':{
                'field': color,
                'type':'quantitative',}
        }
    }, use_container_width=True)


if __name__ == '__main__':
    main()