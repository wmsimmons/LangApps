import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template, request
from flask_pymongo import PyMongo


app = Flask(__name__)
Bootstrap(app)

app.config['MONGO_DBNAME'] = 'sanna'
app.config['MONGO_URI'] = 'mongodb://sanna:sanna@ds131109.mlab.com:31109/sanna'

mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def home():

    return render_template("/index.html")

@app.route('/word/<word>', methods=['GET', 'POST'])
def wordDisplay(word):
    db = mongo.db.nouns
    entry = db.find_one({"word":word})
    return render_template('word.html', word=word, entry=entry)

@app.route('/results', methods=['GET', 'POST'])
def wordsDisplay():
    word = request.args.get('word')
    return render_template('results.html', word=word)


"""MUST be at end of program"""
if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)	