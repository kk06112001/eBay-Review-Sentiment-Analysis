from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import streamlit as st

analyzer = SentimentIntensityAnalyzer()

def analyze_vader_sentiment(text):
    sentiment_score = analyzer.polarity_scores(text)
    compound_score = sentiment_score['compound']
    
    if compound_score >= 0.05:
        return "Positive"
    elif compound_score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

st.title("eBay Reviews Sentiment Analysis")
review_text = st.text_area("Enter Review Text:")

if st.button('Analyze Sentiment'):
    if review_text:
        sentiment = analyze_vader_sentiment(review_text)
        st.write(f"Sentiment: **{sentiment}**")
    else:
        st.write("Please enter some text to analyze.")
