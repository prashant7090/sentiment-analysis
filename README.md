*Install pip
>sudo apt-get install python-pip

*Install flask
>sudo pip install flask-restful

*Install nltk
>sudo pip install nltk

*download nltk
  >open python terminal  

  >python

  >import nltk

  >nltk.download('vader_lexicon')

*Start server
>python sentiment.py

*Post Sentiment
>curl http://localhost:5000/sentiment -d "statement=This is a terrifying look at the humanity implicit in hatred. Flawed, but fascinating" -X POST -v


