from textblob import TextBlob
class SentimentAnalysis:

    def __init__(self, txt=''):
        self.text = txt


    def sentiment(self):
        blob = TextBlob(self.text)
        for sentence in blob.sentences:
            if sentence.sentiment.polarity > 0 :
                return "Positive Behaviour of Sentence"
            elif sentence.sentiment.polarity < 0 :
                return "Negative Behaviour of Sentence"
            elif sentence.sentiment.polarity == 0:
                return "No negative and positive behaviour found"



