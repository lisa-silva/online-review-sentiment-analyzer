# 💡 Online Review Sentiment Analyzer

## Live Application

This project is deployed as a live, interactive web application using **Streamlit**.

👉 [**Try the Live App Here (Your Streamlit URL)**](<PASTE YOUR STREAMLIT URL HERE>)

## Project Overview

This application is designed to quickly evaluate the emotional tone (sentiment) of any given text, such as a customer review, social media comment, or product description. Users paste text into the field, and the application instantly returns a Polarity Score and a clear "Positive," "Negative," or "Neutral" label.

## Technical Skills Demonstrated

This project showcases core Python proficiency in building and deploying a complete, interactive application:

* **Live Deployment:** Successfully deployed a pure Python script to **Streamlit Cloud** for global accessibility.
* **Natural Language Processing (NLP):** Utilized the **`TextBlob`** library to perform efficient sentiment analysis (calculating polarity and subjectivity).
* **Dependency Management:** Correctly configured the deployment environment using **`requirements.txt`** to manage external libraries (`streamlit`, `textblob`, `nltk`).
* **User Interface (UI) Development:** Employed the **`streamlit`** library to create a clean, modern, and responsive web interface using text areas, columns, and metric display elements.
* **Data Handling:** Implemented logical flow control to process user input and return structured analytical data.

## How to Run Locally

If you wish to clone this repository and run the app on your own computer, follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone [YOUR GITHUB REPOSITORY URL HERE]
    cd online-review-sentiment-analyzer
    ```
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the App:**
    ```bash
    streamlit run sentiment_analyzer.py
    ```