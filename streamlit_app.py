import pandas as pd
import streamlit as st
import plotly.express as px

# Load the dataset
df = pd.read_csv('imdb-movies-dataset.csv')

# Filter the dataset
nic_cage_df = df[df['Cast'].str.contains('Nicolas Cage', na=False)]

# make year column of type int take into conseideration there are Na values with None
nic_cage_df['Year'] = nic_cage_df['Year'].fillna(0).astype(int)

# Start Streamlit app
st.title('Nicolas Cage Movies Analysis')
st.write("Ladies and gentlemen, gather 'round for a tale of the man, the myth, the legend—rumored to be a vampire, rumored to be something else entirely... but undeniably, a force to be reckoned with in Hollywood. Yes, we're talking about none other than Nicolas Cage!")


# add image to display in the streamlit from the web
st.image('https://s.yimg.com/ny/api/res/1.2/.7Eg.E7RbApn2tPBVksJvQ--/YXBwaWQ9aGlnaGxhbmRlcjt3PTQyMDtoPTMzMA--/https://media.zenfs.com/en/homerun/feed_manager_auto_publish_494/db3ca12792ae0d4a406dd2150f27ba88', use_column_width=True, width=150)




st.markdown("""
    With an Oscar to his name, a string of blockbuster hits, and a resume as colorful as his iconic facial expressions, Cage has carved out a niche for himself unlike any other. Whether he's stealing the Declaration of Independence or facing off against bees in a bear suit, there's no denying the sheer magnetism of this cinematic chameleon. So grab your popcorn and buckle up as we dive into the wild and wonderful world of Nic Cage, exploring his epic journey through the lens of the IMDb dataset. Get ready for a ride you won't soon forget!
""")


# add image to display in the streamlit from the web
st.image('data:image/jpeg;base64,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', use_column_width=True, width=150)

st.markdown('<h1><b>To the Data</b></h1>', unsafe_allow_html=True)

# add a sub tittle big to denote a new section
st.markdown('<h2><b>Top 3 Movies of the Year</b></h2>', unsafe_allow_html=True)

# Output the number of movies that are rated
num_movies_rated = len(nic_cage_df)
st.write(f"Number of movies in the dataset from Nicolas Cage: {num_movies_rated}")

st.markdown("""
    Following you can have a sneek peak in the world of NC top 3 movies of last years (where there are movies filmed by Nic). Where you will see the rating, review, number of votes and the poster of the movie. So you can have a sense of Nic's work through the years.
""")


# Display the top 10 movies per year given the meta rating. Use a drop down to change the year and make the drop down in descending order. Also display for each movie in the top 10, the average of the rating of users and also the count
# Create a dropdown menu of years
years = nic_cage_df['Year'].unique()
years = sorted(years, reverse=True)
selected_year = st.selectbox('Select a year', years)

# Filter the dataset by the selected year
selected_year_df = nic_cage_df[nic_cage_df['Year'] == selected_year]

# Display the top 3 movies by rating
top3_movies = selected_year_df.nlargest(3, 'Rating')
st.write(top3_movies)

# Display the average rating, count of ratings, and poster image for each movie
for index, row in top3_movies.iterrows():
    st.write(f"Title: {row['Title']}")
    st.write(f"Rating for {row['Title']}: {row['Rating']}")
    st.write(f"Number of votes {row['Title']}: {row['Votes']}")
    st.image(row['Poster'], width=100)
    # Add description and review
    st.write(f"Description for {row['Title']}: {row['Description']}")
    st.write(f"Review for {row['Title']}: {row['Review']}")
    st.write('---------')

# add a sub tittle big to denote a new section
st.markdown('<h2><b>Deep dive</b></h2>', unsafe_allow_html=True)

st.markdown("""
    With a rating averaging north of 10s it is a fact he has had a great acting career.
   
   <b><i> Note: You can place your cursor over the graphs to detail additional label remarks or zoom.</i></b>
""", unsafe_allow_html=True)

# Create a histogram of movie ratings
fig1 = px.histogram(nic_cage_df, x='Rating', color_discrete_sequence=['steelblue'])
fig1.update_layout(xaxis=dict(tickmode='array', tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ticktext=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']))
st.plotly_chart(fig1)


# Of the highest rated movies, which genres are most common?
# Create a bar chart of genres in the top 10% of ratings, add the number of votes in the second axis, also add the name of the movie
# Find the 90th percentile of ratings
rating_threshold = nic_cage_df['Rating'].quantile(0.90)

# Filter the dataset by the 90th percentile of ratings
top10_df = nic_cage_df[nic_cage_df['Rating'] >= rating_threshold]


st.markdown("""
    Breaking down his top scored movies from past decate to date (2010 onwards) we can see that he has been in a variety of genres, but comedy and drama seem to be shared across his major rated ones.
            
    Seems Drama and comedy might be a good start to create a blockbuster movie.
""")

# Create a bar chart of genres and movie name in the top 10% of ratings, color by year
fig3 = px.bar(top10_df, x='Genre', y='Rating', color='Year', title='Genres of Nicolas Cage Movies in the Top 10% of Ratings', text='Title', barmode='group')
fig3.update_layout(yaxis2=dict(title='Votes'))
fig3.update_layout(xaxis=dict(categoryorder='total descending'))
fig3.update_traces(textposition='outside')
fig3.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig3.update_layout(coloraxis=dict(colorscale='Blues'))
st.plotly_chart(fig3)

st.markdown("""
    Lets compare the duration of the movies, maybe there is a correlation between the score of the highest rated and the duration of the movie.
""")

# create a graph that shows the correlation of rating and duration
fig4 = px.scatter(nic_cage_df, x='Rating', y='Duration (min)', title='Rating vs Duration of Nicolas Cage Movies', hover_name='Title')
st.plotly_chart(fig4)


st.markdown("""
    **As expected there is no correlation between quality and duration of movies. We already have a preliminary genre analysis, but lets see as a final check the reviews of the top 3 movies to assert if there is any similarity on style, theme or else that makes a top rated movie what it is.**
""")

# Create a list of the top 3 rated movies and give info such as year, votes, and the review
top3_movies = nic_cage_df.nlargest(3, 'Rating')
for index, row in top3_movies.iterrows():
    st.write(f"Title: {row['Title']}")
    st.write(f"Year: {row['Year']}")
    st.write(f"Votes: {row['Votes']}")
    st.write(f"Review: {row['Review']}")
    st.write('---------')


st.markdown("""
    <h2><b>In summary a pinch of drama funny script and unexpected drifts in movie plot make for a formulae for a block buster with Nicolas Cage.</b></h2>
""", unsafe_allow_html=True)