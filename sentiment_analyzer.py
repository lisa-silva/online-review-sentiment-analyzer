import streamlit as st
from textblob import TextBlob

# --- App Configuration and Styling ---
st.set_page_config(
    page_title="Online Review Sentiment Analyzer",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS for a cleaner look and a light-hearted, playful feel.
st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6;
    }
    .main-header {
        color: #2e8b57;
        font-size: 2.5em;
        text-align: center;
        padding-top: 10px;
        padding-bottom: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 1.1em;
        border-radius: 12px;
        border: 2px solid #4CAF50;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: white;
        color: #4CAF50;
    }
    .stTextArea label {
        font-size: 1.2em;
    }
</style>
""", unsafe_allow_html=True)

# --- App Title and Introduction ---
st.markdown("<h1 class='main-header'>Online Review Sentiment Analyzer</h1>", unsafe_allow_html=True)
st.markdown("### Powered by Python & Streamlit")
st.write(
    "Paste any text below—a product review, a comment, or a short message—to analyze its sentiment. "
    "The app will classify the text as positive, negative, or neutral."
)

# --- User Input Area ---
# The text area for the user to paste their content.
user_text = st.text_area("Enter your text here:", height=200)

# --- Sentiment Analysis and Output ---
# Button to trigger the analysis.
if st.button("Analyze Sentiment"):
    if user_text:
        # Create a TextBlob object from the user's input.
        blob = TextBlob(user_text)
        
        # Get the polarity score, which ranges from -1.0 (negative) to 1.0 (positive).
        polarity_score = blob.sentiment.polarity

        # Display the result based on the polarity score.
        if polarity_score > 0.1:
            st.success(f"**Overall Sentiment: Positive 😊**")
            st.write(f"_Polarity Score: {polarity_score:.2f}_")
            st.write(
                "The tone of this text is generally favorable and expressive of a positive emotion or opinion."
            )
        elif polarity_score < -0.1:
            st.error(f"**Overall Sentiment: Negative 😠**")
            st.write(f"_Polarity Score: {polarity_score:.2f}_")
            st.write(
                "The tone of this text is generally critical or unfavorable, expressing a negative emotion or opinion."
            )
        else:
            st.info(f"**Overall Sentiment: Neutral 😐**")
            st.write(f"_Polarity Score: {polarity_score:.2f}_")
            st.write(
                "The tone of this text is largely balanced or unemotional, showing no strong positive or negative bias."
            )
    else:
        st.warning("Please enter some text to analyze!")
