Online Review Sentiment Analyzer
Overview

This project is a web-based application built with Streamlit that analyzes the sentiment of any text input, such as product reviews, social media comments, or customer feedback. The application provides an immediate classification of the text as positive, negative, or neutral, along with a numerical polarity score.

This project was developed as a key piece of my data science and digital product design portfolio, demonstrating my ability to build and deploy a functional, data-driven application from end-to-end.
How It Works

The app leverages the TextBlob library, a powerful tool for natural language processing (NLP) in Python. When a user enters text and clicks "Analyze," the app performs the following steps:

    Tokenization: The input text is broken down into individual words or phrases.

    Sentiment Calculation: The polarity of each word is analyzed to determine the overall sentiment score.

    Classification: The final score is used to classify the text into one of three categories:

        Positive: Score greater than 0.1

        Neutral: Score between -0.1 and 0.1

        Negative: Score less than -0.1

Key Features

    Real-time Sentiment Analysis: Get instant feedback on the emotional tone of your text.

    Intuitive UI: A clean, user-friendly interface designed with Streamlit for a seamless experience.

    Categorical Output: Clear classification into positive, negative, or neutral sentiment.

    Polarity Score: Provides a numerical value to quantify the sentiment.

Live Demo

See the application in action here:

Click here to view the live app on Streamlit Cloud
Local Setup & Installation

To run this application on your local machine, follow these simple steps:

    Clone the repository:

    git clone [https://github.com/lisa-silva/online-review-sentiment-analyzer.git](https://github.com/lisa-silva/online-review-sentiment-analyzer.git)

    Install the required libraries:

    pip install -r requirements.txt

    (Note: The requirements.txt file contains streamlit and textblob.)

    Run the application:

    streamlit run sentiment_analyzer.py

The app will automatically open in your default web browser.
Contact

If you have any questions or feedback, feel free to open an issue in this repository or connect with me via my portfolio.