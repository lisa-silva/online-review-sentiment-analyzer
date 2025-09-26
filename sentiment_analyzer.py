# This Streamlit application performs sentiment analysis on user-provided text

import streamlit as st
import pandas as pd
from textblob import TextBlob
import nltk # NEW: Import NLTK library
nltk.download('punkt', quiet=True) 
# NEW: Download the required data for TextBlob

# --- Page Configuration ---
st.set_page_config(
    page_title="Online Review Sentiment Analyzer",
    layout="wide"
)

st.title("💡 Online Review Sentiment Analyzer")
st.markdown("Use this tool to analyze the emotional tone (sentiment) of any text or review.")

# --- Analysis Function ---

def analyze_sentiment(text):
    """Calculates sentiment polarity using TextBlob."""
    if not text:
        return 0, "N/A"
    
    # We don't need to specify the source of TextBlob here, as it's a simple example.
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    
    if polarity > 0.1:
        sentiment = "Positive"
    elif polarity < -0.1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
        
    return polarity, sentiment

# --- User Interface ---

# Input box for the user to paste text
user_input = st.text_area(
    "Paste your review or text here:",
    height=200,
    placeholder="e.g., This product is fantastic! I highly recommend it."
)

if user_input:
    # Perform the analysis
    polarity, sentiment_label = analyze_sentiment(user_input)
    
    st.header("Analysis Results")
    
    col1, col2 = st.columns(2)
    
    # Display the final sentiment label
    with col1:
        if sentiment_label == "Positive":
            st.success(f"Sentiment: {sentiment_label} 😄")
        elif sentiment_label == "Negative":
            st.error(f"Sentiment: {sentiment_label} 😡")
        else:
            st.info(f"Sentiment: {sentiment_label} 😐")
            
    # Display the polarity score
    with col2:
        st.metric(label="Polarity Score (-1.0 to 1.0)", value=f"{polarity:.3f}")
        st.caption("Score close to 1.0 is highly positive; score close to -1.0 is highly negative.")
        
    # Optional: Show a breakdown of the TextBlob output
    st.subheader("Raw TextBlob Data")
    st.code(TextBlob(user_input).sentiment)
