from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
    score = analyzer.polarity_scores(text)['compound']
    if score > 0.05:
        return "Positive", "😊", "green"
    elif score < -0.05:
        return "Negative", "😞", "red"
    else:
        return "Neutral", "😐", "gray"

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    emoji = None
    color = None
    if request.method == 'POST':
        text = request.form['text']
        sentiment, emoji, color = get_sentiment(text)
    return render_template('index.html', sentiment=sentiment, emoji=emoji, color=color)

if __name__ == "__main__":
    app.run(debug=True)