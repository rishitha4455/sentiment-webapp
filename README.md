\# Sentiment Analyzer Web App



A simple \*\*Flask web application\*\* that analyzes the sentiment of text and classifies it as \*\*Positive\*\*, \*\*Negative\*\*, or \*\*Neutral\*\*. It uses \*\*VADER Sentiment Analysis\*\* and provides visual feedback with \*\*emoji and color\*\*.



---



\## Features



\- Enter any text and get sentiment analysis.

\- Color-coded results:

&nbsp; - \*\*Green 😊\*\* → Positive

&nbsp; - \*\*Red 😞\*\* → Negative

&nbsp; - \*\*Gray 😐\*\* → Neutral

\- Lightweight and easy to run locally.

\- Fully open-source and easy to extend.



---



\## Tech Stack



\- \*\*Python 3\*\*

\- \*\*Flask\*\* – Web framework

\- \*\*VADER Sentiment\*\* – For sentiment scoring

\- \*\*HTML\*\* – Front-end interface



---



\## Folder Structure

sentiment\_webapp/

│

├─ app.py # Main Flask application

├─ templates/

│ └─ index.html # HTML template

├─ static/ # Optional CSS/images

├─ requirements.txt # Python dependencies

└─ README.md



---



\## Installation \& Running Locally



1\. Clone the repository



```bash

git clone https://github.com/rishitha4455/sentiment-webapp.git

cd sentiment-webapp

\## Install dependencies:

python -m pip install --upgrade pip

python -m pip install flask vaderSentiment textblob

python -m textblob.download\_corpora



\## Run the app

python app.py



\## Open your browser at



http://127.0.0.1:5000

