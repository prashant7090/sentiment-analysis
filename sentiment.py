from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import nltk
from nltk.sentiment import vader

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('statement')

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'This is simplest rest server!'}


    def post(self):
        args = parser.parse_args()
        vaderObj = vader.SentimentIntensityAnalyzer()
        res = vaderObj.polarity_scores(args.statement)
        print res['compound']
        if res['compound'] < 0:
            return {'res' : 'Sentiment is negative'}, 201
        elif res['compound'] > 0:
            return {'res' : 'Sentiment is positive'}, 201
        else:
            return {'res' : 'Sentiment is neutral'}, 201

api.add_resource(HelloWorld, '/sentiment')


if __name__ == '__main__':
    app.run(debug=True)
